# SNMP MIB module (CIENA-6500R-INVENTORY-AMPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-6500R-INVENTORY-AMPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:17 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(rlsInventoryAmps,) = mibBuilder.importSymbols(
    "CIENA-6500R-INVENTORY-MIB",
    "rlsInventoryAmps")

(AdminState,
 OrlState) = mibBuilder.importSymbols(
    "CIENA-6500R-TYPES-MIB",
    "AdminState",
    "OrlState")

(DisplayString128,
 DisplayString32) = mibBuilder.importSymbols(
    "CIENA-PRO-TYPES-MIB",
    "DisplayString128",
    "DisplayString32")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaRlsInventoryAmpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaRlsInventoryAmpsMIB.setRevisions(
        ("2020-09-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlsInventoryAmpsTable_Object = MibTable
rlsInventoryAmpsTable = _RlsInventoryAmpsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rlsInventoryAmpsTable.setStatus("current")
_RlsInventoryAmpsEntry_Object = MibTableRow
rlsInventoryAmpsEntry = _RlsInventoryAmpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1)
)
rlsInventoryAmpsEntry.setIndexNames(
    (0, "CIENA-6500R-INVENTORY-AMPS-MIB", "rlsInventoryAmpsSlotName"),
    (0, "CIENA-6500R-INVENTORY-AMPS-MIB", "rlsInventoryAmpsName"),
)
if mibBuilder.loadTexts:
    rlsInventoryAmpsEntry.setStatus("current")
_RlsInventoryAmpsSlotName_Type = DisplayString32
_RlsInventoryAmpsSlotName_Object = MibTableColumn
rlsInventoryAmpsSlotName = _RlsInventoryAmpsSlotName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 1),
    _RlsInventoryAmpsSlotName_Type()
)
rlsInventoryAmpsSlotName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlsInventoryAmpsSlotName.setStatus("current")
_RlsInventoryAmpsName_Type = DisplayString128
_RlsInventoryAmpsName_Object = MibTableColumn
rlsInventoryAmpsName = _RlsInventoryAmpsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 2),
    _RlsInventoryAmpsName_Type()
)
rlsInventoryAmpsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlsInventoryAmpsName.setStatus("current")


class _RlsInventoryAmpsAmpMode_Type(Integer32):
    """Custom type rlsInventoryAmpsAmpMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("power", 1),
          ("gain", 2),
          ("gainclamp", 3))
    )


_RlsInventoryAmpsAmpMode_Type.__name__ = "Integer32"
_RlsInventoryAmpsAmpMode_Object = MibTableColumn
rlsInventoryAmpsAmpMode = _RlsInventoryAmpsAmpMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 3),
    _RlsInventoryAmpsAmpMode_Type()
)
rlsInventoryAmpsAmpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsAmpMode.setStatus("current")


class _RlsInventoryAmpsState_Type(Integer32):
    """Custom type rlsInventoryAmpsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unkown", 0),
          ("shutoff", 1),
          ("apr", 2),
          ("normal", 3),
          ("clamped", 4))
    )


_RlsInventoryAmpsState_Type.__name__ = "Integer32"
_RlsInventoryAmpsState_Object = MibTableColumn
rlsInventoryAmpsState = _RlsInventoryAmpsState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 4),
    _RlsInventoryAmpsState_Type()
)
rlsInventoryAmpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsState.setStatus("current")


class _RlsInventoryAmpsGainMode_Type(Integer32):
    """Custom type rlsInventoryAmpsGainMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_RlsInventoryAmpsGainMode_Type.__name__ = "Integer32"
_RlsInventoryAmpsGainMode_Object = MibTableColumn
rlsInventoryAmpsGainMode = _RlsInventoryAmpsGainMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 5),
    _RlsInventoryAmpsGainMode_Type()
)
rlsInventoryAmpsGainMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsGainMode.setStatus("current")


class _RlsInventoryAmpsForcedShutdown_Type(Integer32):
    """Custom type rlsInventoryAmpsForcedShutdown based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_RlsInventoryAmpsForcedShutdown_Type.__name__ = "Integer32"
_RlsInventoryAmpsForcedShutdown_Object = MibTableColumn
rlsInventoryAmpsForcedShutdown = _RlsInventoryAmpsForcedShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 6),
    _RlsInventoryAmpsForcedShutdown_Type()
)
rlsInventoryAmpsForcedShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsForcedShutdown.setStatus("current")
_RlsInventoryAmpsTargetGain_Type = DisplayString32
_RlsInventoryAmpsTargetGain_Object = MibTableColumn
rlsInventoryAmpsTargetGain = _RlsInventoryAmpsTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 7),
    _RlsInventoryAmpsTargetGain_Type()
)
rlsInventoryAmpsTargetGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGain.setStatus("current")
_RlsInventoryAmpsBaselineTargetGain_Type = DisplayString32
_RlsInventoryAmpsBaselineTargetGain_Object = MibTableColumn
rlsInventoryAmpsBaselineTargetGain = _RlsInventoryAmpsBaselineTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 8),
    _RlsInventoryAmpsBaselineTargetGain_Type()
)
rlsInventoryAmpsBaselineTargetGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsBaselineTargetGain.setStatus("current")
_RlsInventoryAmpsBaselineTimestamp_Type = DisplayString32
_RlsInventoryAmpsBaselineTimestamp_Object = MibTableColumn
rlsInventoryAmpsBaselineTimestamp = _RlsInventoryAmpsBaselineTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 9),
    _RlsInventoryAmpsBaselineTimestamp_Type()
)
rlsInventoryAmpsBaselineTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsBaselineTimestamp.setStatus("current")
_RlsInventoryAmpsTargetGainRangesLowMin_Type = DisplayString32
_RlsInventoryAmpsTargetGainRangesLowMin_Object = MibTableColumn
rlsInventoryAmpsTargetGainRangesLowMin = _RlsInventoryAmpsTargetGainRangesLowMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 10),
    _RlsInventoryAmpsTargetGainRangesLowMin_Type()
)
rlsInventoryAmpsTargetGainRangesLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGainRangesLowMin.setStatus("current")
_RlsInventoryAmpsTargetGainRangesLowMax_Type = DisplayString32
_RlsInventoryAmpsTargetGainRangesLowMax_Object = MibTableColumn
rlsInventoryAmpsTargetGainRangesLowMax = _RlsInventoryAmpsTargetGainRangesLowMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 11),
    _RlsInventoryAmpsTargetGainRangesLowMax_Type()
)
rlsInventoryAmpsTargetGainRangesLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGainRangesLowMax.setStatus("current")
_RlsInventoryAmpsTargetGainRangesHighMin_Type = DisplayString32
_RlsInventoryAmpsTargetGainRangesHighMin_Object = MibTableColumn
rlsInventoryAmpsTargetGainRangesHighMin = _RlsInventoryAmpsTargetGainRangesHighMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 12),
    _RlsInventoryAmpsTargetGainRangesHighMin_Type()
)
rlsInventoryAmpsTargetGainRangesHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGainRangesHighMin.setStatus("current")
_RlsInventoryAmpsTargetGainRangesHighMax_Type = DisplayString32
_RlsInventoryAmpsTargetGainRangesHighMax_Object = MibTableColumn
rlsInventoryAmpsTargetGainRangesHighMax = _RlsInventoryAmpsTargetGainRangesHighMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 13),
    _RlsInventoryAmpsTargetGainRangesHighMax_Type()
)
rlsInventoryAmpsTargetGainRangesHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGainRangesHighMax.setStatus("current")
_RlsInventoryAmpsTargetPower_Type = DisplayString32
_RlsInventoryAmpsTargetPower_Object = MibTableColumn
rlsInventoryAmpsTargetPower = _RlsInventoryAmpsTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 14),
    _RlsInventoryAmpsTargetPower_Type()
)
rlsInventoryAmpsTargetPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetPower.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetPower.setUnits("dBm")
_RlsInventoryAmpsTargetPowerRangesMin_Type = DisplayString32
_RlsInventoryAmpsTargetPowerRangesMin_Object = MibTableColumn
rlsInventoryAmpsTargetPowerRangesMin = _RlsInventoryAmpsTargetPowerRangesMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 15),
    _RlsInventoryAmpsTargetPowerRangesMin_Type()
)
rlsInventoryAmpsTargetPowerRangesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetPowerRangesMin.setStatus("current")
_RlsInventoryAmpsTargetPowerRangesMax_Type = DisplayString32
_RlsInventoryAmpsTargetPowerRangesMax_Object = MibTableColumn
rlsInventoryAmpsTargetPowerRangesMax = _RlsInventoryAmpsTargetPowerRangesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 16),
    _RlsInventoryAmpsTargetPowerRangesMax_Type()
)
rlsInventoryAmpsTargetPowerRangesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetPowerRangesMax.setStatus("current")
_RlsInventoryAmpsTargetGainTilt_Type = DisplayString32
_RlsInventoryAmpsTargetGainTilt_Object = MibTableColumn
rlsInventoryAmpsTargetGainTilt = _RlsInventoryAmpsTargetGainTilt_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 17),
    _RlsInventoryAmpsTargetGainTilt_Type()
)
rlsInventoryAmpsTargetGainTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGainTilt.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGainTilt.setUnits("dB")
_RlsInventoryAmpsTargetGainTiltRangesMin_Type = DisplayString32
_RlsInventoryAmpsTargetGainTiltRangesMin_Object = MibTableColumn
rlsInventoryAmpsTargetGainTiltRangesMin = _RlsInventoryAmpsTargetGainTiltRangesMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 18),
    _RlsInventoryAmpsTargetGainTiltRangesMin_Type()
)
rlsInventoryAmpsTargetGainTiltRangesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGainTiltRangesMin.setStatus("current")
_RlsInventoryAmpsTargetGainTiltRangesMax_Type = DisplayString32
_RlsInventoryAmpsTargetGainTiltRangesMax_Object = MibTableColumn
rlsInventoryAmpsTargetGainTiltRangesMax = _RlsInventoryAmpsTargetGainTiltRangesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 19),
    _RlsInventoryAmpsTargetGainTiltRangesMax_Type()
)
rlsInventoryAmpsTargetGainTiltRangesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsTargetGainTiltRangesMax.setStatus("current")
_RlsInventoryAmpsShutoffThreshold_Type = DisplayString32
_RlsInventoryAmpsShutoffThreshold_Object = MibTableColumn
rlsInventoryAmpsShutoffThreshold = _RlsInventoryAmpsShutoffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 20),
    _RlsInventoryAmpsShutoffThreshold_Type()
)
rlsInventoryAmpsShutoffThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsShutoffThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsShutoffThreshold.setUnits("dBm")
_RlsInventoryAmpsShutoffThresholdRangesMin_Type = DisplayString32
_RlsInventoryAmpsShutoffThresholdRangesMin_Object = MibTableColumn
rlsInventoryAmpsShutoffThresholdRangesMin = _RlsInventoryAmpsShutoffThresholdRangesMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 21),
    _RlsInventoryAmpsShutoffThresholdRangesMin_Type()
)
rlsInventoryAmpsShutoffThresholdRangesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsShutoffThresholdRangesMin.setStatus("current")
_RlsInventoryAmpsShutoffThresholdRangesMax_Type = DisplayString32
_RlsInventoryAmpsShutoffThresholdRangesMax_Object = MibTableColumn
rlsInventoryAmpsShutoffThresholdRangesMax = _RlsInventoryAmpsShutoffThresholdRangesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 22),
    _RlsInventoryAmpsShutoffThresholdRangesMax_Type()
)
rlsInventoryAmpsShutoffThresholdRangesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsShutoffThresholdRangesMax.setStatus("current")
_RlsInventoryAmpsShutoffHysteresis_Type = DisplayString32
_RlsInventoryAmpsShutoffHysteresis_Object = MibTableColumn
rlsInventoryAmpsShutoffHysteresis = _RlsInventoryAmpsShutoffHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 23),
    _RlsInventoryAmpsShutoffHysteresis_Type()
)
rlsInventoryAmpsShutoffHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsShutoffHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsShutoffHysteresis.setUnits("dB")
_RlsInventoryAmpsInputLosThreshold_Type = DisplayString32
_RlsInventoryAmpsInputLosThreshold_Object = MibTableColumn
rlsInventoryAmpsInputLosThreshold = _RlsInventoryAmpsInputLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 24),
    _RlsInventoryAmpsInputLosThreshold_Type()
)
rlsInventoryAmpsInputLosThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInputLosThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInputLosThreshold.setUnits("dBm")
_RlsInventoryAmpsInputLosThresholdRangesMin_Type = DisplayString32
_RlsInventoryAmpsInputLosThresholdRangesMin_Object = MibTableColumn
rlsInventoryAmpsInputLosThresholdRangesMin = _RlsInventoryAmpsInputLosThresholdRangesMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 25),
    _RlsInventoryAmpsInputLosThresholdRangesMin_Type()
)
rlsInventoryAmpsInputLosThresholdRangesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInputLosThresholdRangesMin.setStatus("current")
_RlsInventoryAmpsInputLosThresholdRangesMax_Type = DisplayString32
_RlsInventoryAmpsInputLosThresholdRangesMax_Object = MibTableColumn
rlsInventoryAmpsInputLosThresholdRangesMax = _RlsInventoryAmpsInputLosThresholdRangesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 26),
    _RlsInventoryAmpsInputLosThresholdRangesMax_Type()
)
rlsInventoryAmpsInputLosThresholdRangesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInputLosThresholdRangesMax.setStatus("current")


class _RlsInventoryAmpsInputLosHysteresis_Type(DisplayString32):
    """Custom type rlsInventoryAmpsInputLosHysteresis based on DisplayString32"""
    defaultValue = OctetString("3")


_RlsInventoryAmpsInputLosHysteresis_Type.__name__ = "DisplayString32"
_RlsInventoryAmpsInputLosHysteresis_Object = MibTableColumn
rlsInventoryAmpsInputLosHysteresis = _RlsInventoryAmpsInputLosHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 27),
    _RlsInventoryAmpsInputLosHysteresis_Type()
)
rlsInventoryAmpsInputLosHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInputLosHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInputLosHysteresis.setUnits("dB")
_RlsInventoryAmpsOrlThreshold_Type = DisplayString32
_RlsInventoryAmpsOrlThreshold_Object = MibTableColumn
rlsInventoryAmpsOrlThreshold = _RlsInventoryAmpsOrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 28),
    _RlsInventoryAmpsOrlThreshold_Type()
)
rlsInventoryAmpsOrlThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOrlThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOrlThreshold.setUnits("dB")
_RlsInventoryAmpsOrlThresholdRangesMin_Type = DisplayString32
_RlsInventoryAmpsOrlThresholdRangesMin_Object = MibTableColumn
rlsInventoryAmpsOrlThresholdRangesMin = _RlsInventoryAmpsOrlThresholdRangesMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 29),
    _RlsInventoryAmpsOrlThresholdRangesMin_Type()
)
rlsInventoryAmpsOrlThresholdRangesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOrlThresholdRangesMin.setStatus("current")
_RlsInventoryAmpsOrlThresholdRangesMax_Type = DisplayString32
_RlsInventoryAmpsOrlThresholdRangesMax_Object = MibTableColumn
rlsInventoryAmpsOrlThresholdRangesMax = _RlsInventoryAmpsOrlThresholdRangesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 30),
    _RlsInventoryAmpsOrlThresholdRangesMax_Type()
)
rlsInventoryAmpsOrlThresholdRangesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOrlThresholdRangesMax.setStatus("current")


class _RlsInventoryAmpsLowOrlHysteresis_Type(DisplayString32):
    """Custom type rlsInventoryAmpsLowOrlHysteresis based on DisplayString32"""
    defaultValue = OctetString("3")


_RlsInventoryAmpsLowOrlHysteresis_Type.__name__ = "DisplayString32"
_RlsInventoryAmpsLowOrlHysteresis_Object = MibTableColumn
rlsInventoryAmpsLowOrlHysteresis = _RlsInventoryAmpsLowOrlHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 31),
    _RlsInventoryAmpsLowOrlHysteresis_Type()
)
rlsInventoryAmpsLowOrlHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsLowOrlHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsLowOrlHysteresis.setUnits("dB")
_RlsInventoryAmpsOrlState_Type = OrlState
_RlsInventoryAmpsOrlState_Object = MibTableColumn
rlsInventoryAmpsOrlState = _RlsInventoryAmpsOrlState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 32),
    _RlsInventoryAmpsOrlState_Type()
)
rlsInventoryAmpsOrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOrlState.setStatus("current")
_RlsInventoryAmpsGainOffset_Type = DisplayString32
_RlsInventoryAmpsGainOffset_Object = MibTableColumn
rlsInventoryAmpsGainOffset = _RlsInventoryAmpsGainOffset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 33),
    _RlsInventoryAmpsGainOffset_Type()
)
rlsInventoryAmpsGainOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsGainOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsGainOffset.setUnits("dB")
_RlsInventoryAmpsGainOffsetRangesMin_Type = DisplayString32
_RlsInventoryAmpsGainOffsetRangesMin_Object = MibTableColumn
rlsInventoryAmpsGainOffsetRangesMin = _RlsInventoryAmpsGainOffsetRangesMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 34),
    _RlsInventoryAmpsGainOffsetRangesMin_Type()
)
rlsInventoryAmpsGainOffsetRangesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsGainOffsetRangesMin.setStatus("current")
_RlsInventoryAmpsGainOffsetRangesMax_Type = DisplayString32
_RlsInventoryAmpsGainOffsetRangesMax_Object = MibTableColumn
rlsInventoryAmpsGainOffsetRangesMax = _RlsInventoryAmpsGainOffsetRangesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 35),
    _RlsInventoryAmpsGainOffsetRangesMax_Type()
)
rlsInventoryAmpsGainOffsetRangesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsGainOffsetRangesMax.setStatus("current")
_RlsInventoryAmpsGain_Type = DisplayString32
_RlsInventoryAmpsGain_Object = MibTableColumn
rlsInventoryAmpsGain = _RlsInventoryAmpsGain_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 36),
    _RlsInventoryAmpsGain_Type()
)
rlsInventoryAmpsGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsGain.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsGain.setUnits("dB")
_RlsInventoryAmpsMaxTargetPower_Type = DisplayString32
_RlsInventoryAmpsMaxTargetPower_Object = MibTableColumn
rlsInventoryAmpsMaxTargetPower = _RlsInventoryAmpsMaxTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 37),
    _RlsInventoryAmpsMaxTargetPower_Type()
)
rlsInventoryAmpsMaxTargetPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsMaxTargetPower.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsMaxTargetPower.setUnits("dBm")
_RlsInventoryAmpsMaxTargetPowerRangesMin_Type = DisplayString32
_RlsInventoryAmpsMaxTargetPowerRangesMin_Object = MibTableColumn
rlsInventoryAmpsMaxTargetPowerRangesMin = _RlsInventoryAmpsMaxTargetPowerRangesMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 38),
    _RlsInventoryAmpsMaxTargetPowerRangesMin_Type()
)
rlsInventoryAmpsMaxTargetPowerRangesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsMaxTargetPowerRangesMin.setStatus("current")
_RlsInventoryAmpsMaxTargetPowerRangesMax_Type = DisplayString32
_RlsInventoryAmpsMaxTargetPowerRangesMax_Object = MibTableColumn
rlsInventoryAmpsMaxTargetPowerRangesMax = _RlsInventoryAmpsMaxTargetPowerRangesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 39),
    _RlsInventoryAmpsMaxTargetPowerRangesMax_Type()
)
rlsInventoryAmpsMaxTargetPowerRangesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsMaxTargetPowerRangesMax.setStatus("current")
_RlsInventoryAmpsAprThreshold_Type = DisplayString32
_RlsInventoryAmpsAprThreshold_Object = MibTableColumn
rlsInventoryAmpsAprThreshold = _RlsInventoryAmpsAprThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 40),
    _RlsInventoryAmpsAprThreshold_Type()
)
rlsInventoryAmpsAprThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsAprThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsAprThreshold.setUnits("dBm")
_RlsInventoryAmpsAprHysteresis_Type = DisplayString32
_RlsInventoryAmpsAprHysteresis_Object = MibTableColumn
rlsInventoryAmpsAprHysteresis = _RlsInventoryAmpsAprHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 41),
    _RlsInventoryAmpsAprHysteresis_Type()
)
rlsInventoryAmpsAprHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsAprHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsAprHysteresis.setUnits("dB")
_RlsInventoryAmpsForceApr_Type = TruthValue
_RlsInventoryAmpsForceApr_Object = MibTableColumn
rlsInventoryAmpsForceApr = _RlsInventoryAmpsForceApr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 42),
    _RlsInventoryAmpsForceApr_Type()
)
rlsInventoryAmpsForceApr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsForceApr.setStatus("current")
_RlsInventoryAmpsAprPowerLevel_Type = DisplayString32
_RlsInventoryAmpsAprPowerLevel_Object = MibTableColumn
rlsInventoryAmpsAprPowerLevel = _RlsInventoryAmpsAprPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 43),
    _RlsInventoryAmpsAprPowerLevel_Type()
)
rlsInventoryAmpsAprPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsAprPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsAprPowerLevel.setUnits("dBm")
_RlsInventoryAmpsOverloadThresholdsInputPsdLowGain_Type = DisplayString32
_RlsInventoryAmpsOverloadThresholdsInputPsdLowGain_Object = MibTableColumn
rlsInventoryAmpsOverloadThresholdsInputPsdLowGain = _RlsInventoryAmpsOverloadThresholdsInputPsdLowGain_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 44),
    _RlsInventoryAmpsOverloadThresholdsInputPsdLowGain_Type()
)
rlsInventoryAmpsOverloadThresholdsInputPsdLowGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOverloadThresholdsInputPsdLowGain.setStatus("current")
_RlsInventoryAmpsOverloadThresholdsInputPsdHighGain_Type = DisplayString32
_RlsInventoryAmpsOverloadThresholdsInputPsdHighGain_Object = MibTableColumn
rlsInventoryAmpsOverloadThresholdsInputPsdHighGain = _RlsInventoryAmpsOverloadThresholdsInputPsdHighGain_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 45),
    _RlsInventoryAmpsOverloadThresholdsInputPsdHighGain_Type()
)
rlsInventoryAmpsOverloadThresholdsInputPsdHighGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOverloadThresholdsInputPsdHighGain.setStatus("current")
_RlsInventoryAmpsAdminState_Type = AdminState
_RlsInventoryAmpsAdminState_Object = MibTableColumn
rlsInventoryAmpsAdminState = _RlsInventoryAmpsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 46),
    _RlsInventoryAmpsAdminState_Type()
)
rlsInventoryAmpsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsAdminState.setStatus("current")


class _RlsInventoryAmpsServiceState_Type(Integer32):
    """Custom type rlsInventoryAmpsServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("idle", 2))
    )


_RlsInventoryAmpsServiceState_Type.__name__ = "Integer32"
_RlsInventoryAmpsServiceState_Object = MibTableColumn
rlsInventoryAmpsServiceState = _RlsInventoryAmpsServiceState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 47),
    _RlsInventoryAmpsServiceState_Type()
)
rlsInventoryAmpsServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsServiceState.setStatus("current")
_RlsInventoryAmpsInCurrPower_Type = DisplayString32
_RlsInventoryAmpsInCurrPower_Object = MibTableColumn
rlsInventoryAmpsInCurrPower = _RlsInventoryAmpsInCurrPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 48),
    _RlsInventoryAmpsInCurrPower_Type()
)
rlsInventoryAmpsInCurrPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInCurrPower.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInCurrPower.setUnits("dBm")
_RlsInventoryAmpsInMinPower_Type = DisplayString32
_RlsInventoryAmpsInMinPower_Object = MibTableColumn
rlsInventoryAmpsInMinPower = _RlsInventoryAmpsInMinPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 49),
    _RlsInventoryAmpsInMinPower_Type()
)
rlsInventoryAmpsInMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInMinPower.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInMinPower.setUnits("dBm")
_RlsInventoryAmpsInMaxPower_Type = DisplayString32
_RlsInventoryAmpsInMaxPower_Object = MibTableColumn
rlsInventoryAmpsInMaxPower = _RlsInventoryAmpsInMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 50),
    _RlsInventoryAmpsInMaxPower_Type()
)
rlsInventoryAmpsInMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsInMaxPower.setUnits("dBm")
_RlsInventoryAmpsOutCurrPower_Type = DisplayString32
_RlsInventoryAmpsOutCurrPower_Object = MibTableColumn
rlsInventoryAmpsOutCurrPower = _RlsInventoryAmpsOutCurrPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 51),
    _RlsInventoryAmpsOutCurrPower_Type()
)
rlsInventoryAmpsOutCurrPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOutCurrPower.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOutCurrPower.setUnits("dBm")
_RlsInventoryAmpsOutMinPower_Type = DisplayString32
_RlsInventoryAmpsOutMinPower_Object = MibTableColumn
rlsInventoryAmpsOutMinPower = _RlsInventoryAmpsOutMinPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 52),
    _RlsInventoryAmpsOutMinPower_Type()
)
rlsInventoryAmpsOutMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOutMinPower.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOutMinPower.setUnits("dBm")
_RlsInventoryAmpsOutMaxPower_Type = DisplayString32
_RlsInventoryAmpsOutMaxPower_Object = MibTableColumn
rlsInventoryAmpsOutMaxPower = _RlsInventoryAmpsOutMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 53),
    _RlsInventoryAmpsOutMaxPower_Type()
)
rlsInventoryAmpsOutMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOutMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOutMaxPower.setUnits("dBm")
_RlsInventoryAmpsOpticalReturnLoss_Type = DisplayString32
_RlsInventoryAmpsOpticalReturnLoss_Object = MibTableColumn
rlsInventoryAmpsOpticalReturnLoss = _RlsInventoryAmpsOpticalReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 54),
    _RlsInventoryAmpsOpticalReturnLoss_Type()
)
rlsInventoryAmpsOpticalReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOpticalReturnLoss.setStatus("current")
if mibBuilder.loadTexts:
    rlsInventoryAmpsOpticalReturnLoss.setUnits("dB")
_RlsInventoryAmpsDiagnosticInputLossSignal_Type = TruthValue
_RlsInventoryAmpsDiagnosticInputLossSignal_Object = MibTableColumn
rlsInventoryAmpsDiagnosticInputLossSignal = _RlsInventoryAmpsDiagnosticInputLossSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 55),
    _RlsInventoryAmpsDiagnosticInputLossSignal_Type()
)
rlsInventoryAmpsDiagnosticInputLossSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDiagnosticInputLossSignal.setStatus("current")
_RlsInventoryAmpsDiagnosticShutoffThresholdCrossed_Type = TruthValue
_RlsInventoryAmpsDiagnosticShutoffThresholdCrossed_Object = MibTableColumn
rlsInventoryAmpsDiagnosticShutoffThresholdCrossed = _RlsInventoryAmpsDiagnosticShutoffThresholdCrossed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 56),
    _RlsInventoryAmpsDiagnosticShutoffThresholdCrossed_Type()
)
rlsInventoryAmpsDiagnosticShutoffThresholdCrossed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDiagnosticShutoffThresholdCrossed.setStatus("current")
_RlsInventoryAmpsDignosticAutomaticShutoff_Type = TruthValue
_RlsInventoryAmpsDignosticAutomaticShutoff_Object = MibTableColumn
rlsInventoryAmpsDignosticAutomaticShutoff = _RlsInventoryAmpsDignosticAutomaticShutoff_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 57),
    _RlsInventoryAmpsDignosticAutomaticShutoff_Type()
)
rlsInventoryAmpsDignosticAutomaticShutoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDignosticAutomaticShutoff.setStatus("current")
_RlsInventoryAmpsDiagnosticAutomaticPowerReductionActive_Type = TruthValue
_RlsInventoryAmpsDiagnosticAutomaticPowerReductionActive_Object = MibTableColumn
rlsInventoryAmpsDiagnosticAutomaticPowerReductionActive = _RlsInventoryAmpsDiagnosticAutomaticPowerReductionActive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 58),
    _RlsInventoryAmpsDiagnosticAutomaticPowerReductionActive_Type()
)
rlsInventoryAmpsDiagnosticAutomaticPowerReductionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDiagnosticAutomaticPowerReductionActive.setStatus("current")
_RlsInventoryAmpsDignosticParentFailed_Type = TruthValue
_RlsInventoryAmpsDignosticParentFailed_Object = MibTableColumn
rlsInventoryAmpsDignosticParentFailed = _RlsInventoryAmpsDignosticParentFailed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 59),
    _RlsInventoryAmpsDignosticParentFailed_Type()
)
rlsInventoryAmpsDignosticParentFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDignosticParentFailed.setStatus("current")
_RlsInventoryAmpsDignosticOpticalLineFailed_Type = TruthValue
_RlsInventoryAmpsDignosticOpticalLineFailed_Object = MibTableColumn
rlsInventoryAmpsDignosticOpticalLineFailed = _RlsInventoryAmpsDignosticOpticalLineFailed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 60),
    _RlsInventoryAmpsDignosticOpticalLineFailed_Type()
)
rlsInventoryAmpsDignosticOpticalLineFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDignosticOpticalLineFailed.setStatus("current")
_RlsInventoryAmpsDignosticLowOpticalReturnLoss_Type = TruthValue
_RlsInventoryAmpsDignosticLowOpticalReturnLoss_Object = MibTableColumn
rlsInventoryAmpsDignosticLowOpticalReturnLoss = _RlsInventoryAmpsDignosticLowOpticalReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 61),
    _RlsInventoryAmpsDignosticLowOpticalReturnLoss_Type()
)
rlsInventoryAmpsDignosticLowOpticalReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDignosticLowOpticalReturnLoss.setStatus("current")
_RlsInventoryAmpsDignosticLossOfSignal_Type = TruthValue
_RlsInventoryAmpsDignosticLossOfSignal_Object = MibTableColumn
rlsInventoryAmpsDignosticLossOfSignal = _RlsInventoryAmpsDignosticLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 62),
    _RlsInventoryAmpsDignosticLossOfSignal_Type()
)
rlsInventoryAmpsDignosticLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDignosticLossOfSignal.setStatus("current")
_RlsInventoryAmpsDignosticInputOpticalOverload_Type = TruthValue
_RlsInventoryAmpsDignosticInputOpticalOverload_Object = MibTableColumn
rlsInventoryAmpsDignosticInputOpticalOverload = _RlsInventoryAmpsDignosticInputOpticalOverload_Object(
    (1, 3, 6, 1, 4, 1, 1271, 4, 1, 1, 1, 2, 1, 1, 1, 63),
    _RlsInventoryAmpsDignosticInputOpticalOverload_Type()
)
rlsInventoryAmpsDignosticInputOpticalOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlsInventoryAmpsDignosticInputOpticalOverload.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-6500R-INVENTORY-AMPS-MIB",
    **{"cienaRlsInventoryAmpsMIB": cienaRlsInventoryAmpsMIB,
       "rlsInventoryAmpsTable": rlsInventoryAmpsTable,
       "rlsInventoryAmpsEntry": rlsInventoryAmpsEntry,
       "rlsInventoryAmpsSlotName": rlsInventoryAmpsSlotName,
       "rlsInventoryAmpsName": rlsInventoryAmpsName,
       "rlsInventoryAmpsAmpMode": rlsInventoryAmpsAmpMode,
       "rlsInventoryAmpsState": rlsInventoryAmpsState,
       "rlsInventoryAmpsGainMode": rlsInventoryAmpsGainMode,
       "rlsInventoryAmpsForcedShutdown": rlsInventoryAmpsForcedShutdown,
       "rlsInventoryAmpsTargetGain": rlsInventoryAmpsTargetGain,
       "rlsInventoryAmpsBaselineTargetGain": rlsInventoryAmpsBaselineTargetGain,
       "rlsInventoryAmpsBaselineTimestamp": rlsInventoryAmpsBaselineTimestamp,
       "rlsInventoryAmpsTargetGainRangesLowMin": rlsInventoryAmpsTargetGainRangesLowMin,
       "rlsInventoryAmpsTargetGainRangesLowMax": rlsInventoryAmpsTargetGainRangesLowMax,
       "rlsInventoryAmpsTargetGainRangesHighMin": rlsInventoryAmpsTargetGainRangesHighMin,
       "rlsInventoryAmpsTargetGainRangesHighMax": rlsInventoryAmpsTargetGainRangesHighMax,
       "rlsInventoryAmpsTargetPower": rlsInventoryAmpsTargetPower,
       "rlsInventoryAmpsTargetPowerRangesMin": rlsInventoryAmpsTargetPowerRangesMin,
       "rlsInventoryAmpsTargetPowerRangesMax": rlsInventoryAmpsTargetPowerRangesMax,
       "rlsInventoryAmpsTargetGainTilt": rlsInventoryAmpsTargetGainTilt,
       "rlsInventoryAmpsTargetGainTiltRangesMin": rlsInventoryAmpsTargetGainTiltRangesMin,
       "rlsInventoryAmpsTargetGainTiltRangesMax": rlsInventoryAmpsTargetGainTiltRangesMax,
       "rlsInventoryAmpsShutoffThreshold": rlsInventoryAmpsShutoffThreshold,
       "rlsInventoryAmpsShutoffThresholdRangesMin": rlsInventoryAmpsShutoffThresholdRangesMin,
       "rlsInventoryAmpsShutoffThresholdRangesMax": rlsInventoryAmpsShutoffThresholdRangesMax,
       "rlsInventoryAmpsShutoffHysteresis": rlsInventoryAmpsShutoffHysteresis,
       "rlsInventoryAmpsInputLosThreshold": rlsInventoryAmpsInputLosThreshold,
       "rlsInventoryAmpsInputLosThresholdRangesMin": rlsInventoryAmpsInputLosThresholdRangesMin,
       "rlsInventoryAmpsInputLosThresholdRangesMax": rlsInventoryAmpsInputLosThresholdRangesMax,
       "rlsInventoryAmpsInputLosHysteresis": rlsInventoryAmpsInputLosHysteresis,
       "rlsInventoryAmpsOrlThreshold": rlsInventoryAmpsOrlThreshold,
       "rlsInventoryAmpsOrlThresholdRangesMin": rlsInventoryAmpsOrlThresholdRangesMin,
       "rlsInventoryAmpsOrlThresholdRangesMax": rlsInventoryAmpsOrlThresholdRangesMax,
       "rlsInventoryAmpsLowOrlHysteresis": rlsInventoryAmpsLowOrlHysteresis,
       "rlsInventoryAmpsOrlState": rlsInventoryAmpsOrlState,
       "rlsInventoryAmpsGainOffset": rlsInventoryAmpsGainOffset,
       "rlsInventoryAmpsGainOffsetRangesMin": rlsInventoryAmpsGainOffsetRangesMin,
       "rlsInventoryAmpsGainOffsetRangesMax": rlsInventoryAmpsGainOffsetRangesMax,
       "rlsInventoryAmpsGain": rlsInventoryAmpsGain,
       "rlsInventoryAmpsMaxTargetPower": rlsInventoryAmpsMaxTargetPower,
       "rlsInventoryAmpsMaxTargetPowerRangesMin": rlsInventoryAmpsMaxTargetPowerRangesMin,
       "rlsInventoryAmpsMaxTargetPowerRangesMax": rlsInventoryAmpsMaxTargetPowerRangesMax,
       "rlsInventoryAmpsAprThreshold": rlsInventoryAmpsAprThreshold,
       "rlsInventoryAmpsAprHysteresis": rlsInventoryAmpsAprHysteresis,
       "rlsInventoryAmpsForceApr": rlsInventoryAmpsForceApr,
       "rlsInventoryAmpsAprPowerLevel": rlsInventoryAmpsAprPowerLevel,
       "rlsInventoryAmpsOverloadThresholdsInputPsdLowGain": rlsInventoryAmpsOverloadThresholdsInputPsdLowGain,
       "rlsInventoryAmpsOverloadThresholdsInputPsdHighGain": rlsInventoryAmpsOverloadThresholdsInputPsdHighGain,
       "rlsInventoryAmpsAdminState": rlsInventoryAmpsAdminState,
       "rlsInventoryAmpsServiceState": rlsInventoryAmpsServiceState,
       "rlsInventoryAmpsInCurrPower": rlsInventoryAmpsInCurrPower,
       "rlsInventoryAmpsInMinPower": rlsInventoryAmpsInMinPower,
       "rlsInventoryAmpsInMaxPower": rlsInventoryAmpsInMaxPower,
       "rlsInventoryAmpsOutCurrPower": rlsInventoryAmpsOutCurrPower,
       "rlsInventoryAmpsOutMinPower": rlsInventoryAmpsOutMinPower,
       "rlsInventoryAmpsOutMaxPower": rlsInventoryAmpsOutMaxPower,
       "rlsInventoryAmpsOpticalReturnLoss": rlsInventoryAmpsOpticalReturnLoss,
       "rlsInventoryAmpsDiagnosticInputLossSignal": rlsInventoryAmpsDiagnosticInputLossSignal,
       "rlsInventoryAmpsDiagnosticShutoffThresholdCrossed": rlsInventoryAmpsDiagnosticShutoffThresholdCrossed,
       "rlsInventoryAmpsDignosticAutomaticShutoff": rlsInventoryAmpsDignosticAutomaticShutoff,
       "rlsInventoryAmpsDiagnosticAutomaticPowerReductionActive": rlsInventoryAmpsDiagnosticAutomaticPowerReductionActive,
       "rlsInventoryAmpsDignosticParentFailed": rlsInventoryAmpsDignosticParentFailed,
       "rlsInventoryAmpsDignosticOpticalLineFailed": rlsInventoryAmpsDignosticOpticalLineFailed,
       "rlsInventoryAmpsDignosticLowOpticalReturnLoss": rlsInventoryAmpsDignosticLowOpticalReturnLoss,
       "rlsInventoryAmpsDignosticLossOfSignal": rlsInventoryAmpsDignosticLossOfSignal,
       "rlsInventoryAmpsDignosticInputOpticalOverload": rlsInventoryAmpsDignosticInputOpticalOverload}
)
