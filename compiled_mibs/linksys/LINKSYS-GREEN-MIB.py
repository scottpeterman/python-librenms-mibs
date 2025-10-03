# SNMP MIB module (LINKSYS-GREEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-GREEN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:09:13 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

rlGreenEth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134)
)
if mibBuilder.loadTexts:
    rlGreenEth.setRevisions(
        ("2008-08-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlGreenSavingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("energyDetect", 1),
          ("shortReach", 2))
    )



class NonOperReasonType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("np", 1),
          ("lt", 2),
          ("lu", 3),
          ("ls", 4),
          ("ll", 5),
          ("er", 6),
          ("ld", 7),
          ("unknown", 8))
    )



# MIB Managed Objects in the order of their OIDs

_RlGreenEthEnergyDetectEnable_Type = TruthValue
_RlGreenEthEnergyDetectEnable_Object = MibScalar
rlGreenEthEnergyDetectEnable = _RlGreenEthEnergyDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 1),
    _RlGreenEthEnergyDetectEnable_Type()
)
rlGreenEthEnergyDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGreenEthEnergyDetectEnable.setStatus("current")
_RlGreenEthShortReachEnable_Type = TruthValue
_RlGreenEthShortReachEnable_Object = MibScalar
rlGreenEthShortReachEnable = _RlGreenEthShortReachEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 2),
    _RlGreenEthShortReachEnable_Type()
)
rlGreenEthShortReachEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGreenEthShortReachEnable.setStatus("current")
_RlGreenEthCurrentEnergyConsumption_Type = Unsigned32
_RlGreenEthCurrentEnergyConsumption_Object = MibScalar
rlGreenEthCurrentEnergyConsumption = _RlGreenEthCurrentEnergyConsumption_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 3),
    _RlGreenEthCurrentEnergyConsumption_Type()
)
rlGreenEthCurrentEnergyConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGreenEthCurrentEnergyConsumption.setStatus("current")
if mibBuilder.loadTexts:
    rlGreenEthCurrentEnergyConsumption.setUnits("mWatt")
_RlGreenEthCurrentMaxEnergyConsumption_Type = Unsigned32
_RlGreenEthCurrentMaxEnergyConsumption_Object = MibScalar
rlGreenEthCurrentMaxEnergyConsumption = _RlGreenEthCurrentMaxEnergyConsumption_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 4),
    _RlGreenEthCurrentMaxEnergyConsumption_Type()
)
rlGreenEthCurrentMaxEnergyConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGreenEthCurrentMaxEnergyConsumption.setStatus("current")
if mibBuilder.loadTexts:
    rlGreenEthCurrentMaxEnergyConsumption.setUnits("mWatt")
_RlGreenEthCumulativePowerSaveMeter_Type = Unsigned32
_RlGreenEthCumulativePowerSaveMeter_Object = MibScalar
rlGreenEthCumulativePowerSaveMeter = _RlGreenEthCumulativePowerSaveMeter_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 5),
    _RlGreenEthCumulativePowerSaveMeter_Type()
)
rlGreenEthCumulativePowerSaveMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGreenEthCumulativePowerSaveMeter.setStatus("current")
if mibBuilder.loadTexts:
    rlGreenEthCumulativePowerSaveMeter.setUnits("Watt*Hour")


class _RlGreenEthShortReachThreshold_Type(Unsigned32):
    """Custom type rlGreenEthShortReachThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )


_RlGreenEthShortReachThreshold_Type.__name__ = "Unsigned32"
_RlGreenEthShortReachThreshold_Object = MibScalar
rlGreenEthShortReachThreshold = _RlGreenEthShortReachThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 6),
    _RlGreenEthShortReachThreshold_Type()
)
rlGreenEthShortReachThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGreenEthShortReachThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rlGreenEthShortReachThreshold.setUnits("meter")


class _RlGreenEthCumulativePowerSaveMeterReset_Type(TruthValue):
    """Custom type rlGreenEthCumulativePowerSaveMeterReset based on TruthValue"""
    defaultValue = 2


_RlGreenEthCumulativePowerSaveMeterReset_Type.__name__ = "TruthValue"
_RlGreenEthCumulativePowerSaveMeterReset_Object = MibScalar
rlGreenEthCumulativePowerSaveMeterReset = _RlGreenEthCumulativePowerSaveMeterReset_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 7),
    _RlGreenEthCumulativePowerSaveMeterReset_Type()
)
rlGreenEthCumulativePowerSaveMeterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGreenEthCumulativePowerSaveMeterReset.setStatus("current")
_RlGreenEthPortTable_Object = MibTable
rlGreenEthPortTable = _RlGreenEthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8)
)
if mibBuilder.loadTexts:
    rlGreenEthPortTable.setStatus("current")
_RlGreenEthPortEntry_Object = MibTableRow
rlGreenEthPortEntry = _RlGreenEthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1)
)
rlGreenEthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "LINKSYS-GREEN-MIB", "rlGreenEthPortSavingTypeValue"),
)
if mibBuilder.loadTexts:
    rlGreenEthPortEntry.setStatus("current")
_RlGreenEthPortSavingTypeValue_Type = RlGreenSavingType
_RlGreenEthPortSavingTypeValue_Object = MibTableColumn
rlGreenEthPortSavingTypeValue = _RlGreenEthPortSavingTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1, 1),
    _RlGreenEthPortSavingTypeValue_Type()
)
rlGreenEthPortSavingTypeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlGreenEthPortSavingTypeValue.setStatus("current")
_RlGreenEthPortAdminState_Type = TruthValue
_RlGreenEthPortAdminState_Object = MibTableColumn
rlGreenEthPortAdminState = _RlGreenEthPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1, 2),
    _RlGreenEthPortAdminState_Type()
)
rlGreenEthPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGreenEthPortAdminState.setStatus("current")
_RlGreenEthPortOperState_Type = TruthValue
_RlGreenEthPortOperState_Object = MibTableColumn
rlGreenEthPortOperState = _RlGreenEthPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1, 3),
    _RlGreenEthPortOperState_Type()
)
rlGreenEthPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGreenEthPortOperState.setStatus("current")
_RlGreenEthPortNonOperReason_Type = NonOperReasonType
_RlGreenEthPortNonOperReason_Object = MibTableColumn
rlGreenEthPortNonOperReason = _RlGreenEthPortNonOperReason_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1, 4),
    _RlGreenEthPortNonOperReason_Type()
)
rlGreenEthPortNonOperReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGreenEthPortNonOperReason.setStatus("current")


class _RlGreenEthForceShortReachIfIndexList_Type(PortList):
    """Custom type rlGreenEthForceShortReachIfIndexList based on PortList"""
    defaultHexValue = ""


_RlGreenEthForceShortReachIfIndexList_Type.__name__ = "PortList"
_RlGreenEthForceShortReachIfIndexList_Object = MibScalar
rlGreenEthForceShortReachIfIndexList = _RlGreenEthForceShortReachIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 9),
    _RlGreenEthForceShortReachIfIndexList_Type()
)
rlGreenEthForceShortReachIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGreenEthForceShortReachIfIndexList.setStatus("current")


class _RlGreenEthMaskLedStatus_Type(Integer32):
    """Custom type rlGreenEthMaskLedStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RlGreenEthMaskLedStatus_Type.__name__ = "Integer32"
_RlGreenEthMaskLedStatus_Object = MibScalar
rlGreenEthMaskLedStatus = _RlGreenEthMaskLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 10),
    _RlGreenEthMaskLedStatus_Type()
)
rlGreenEthMaskLedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGreenEthMaskLedStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-GREEN-MIB",
    **{"RlGreenSavingType": RlGreenSavingType,
       "NonOperReasonType": NonOperReasonType,
       "rlGreenEth": rlGreenEth,
       "rlGreenEthEnergyDetectEnable": rlGreenEthEnergyDetectEnable,
       "rlGreenEthShortReachEnable": rlGreenEthShortReachEnable,
       "rlGreenEthCurrentEnergyConsumption": rlGreenEthCurrentEnergyConsumption,
       "rlGreenEthCurrentMaxEnergyConsumption": rlGreenEthCurrentMaxEnergyConsumption,
       "rlGreenEthCumulativePowerSaveMeter": rlGreenEthCumulativePowerSaveMeter,
       "rlGreenEthShortReachThreshold": rlGreenEthShortReachThreshold,
       "rlGreenEthCumulativePowerSaveMeterReset": rlGreenEthCumulativePowerSaveMeterReset,
       "rlGreenEthPortTable": rlGreenEthPortTable,
       "rlGreenEthPortEntry": rlGreenEthPortEntry,
       "rlGreenEthPortSavingTypeValue": rlGreenEthPortSavingTypeValue,
       "rlGreenEthPortAdminState": rlGreenEthPortAdminState,
       "rlGreenEthPortOperState": rlGreenEthPortOperState,
       "rlGreenEthPortNonOperReason": rlGreenEthPortNonOperReason,
       "rlGreenEthForceShortReachIfIndexList": rlGreenEthForceShortReachIfIndexList,
       "rlGreenEthMaskLedStatus": rlGreenEthMaskLedStatus}
)
