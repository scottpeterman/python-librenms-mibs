# SNMP MIB module (SL-EDFA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-EDFA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:46 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slEdfa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EdfaConfig_ObjectIdentity = ObjectIdentity
edfaConfig = _EdfaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1)
)
_EdfaConfigTable_Object = MibTable
edfaConfigTable = _EdfaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    edfaConfigTable.setStatus("current")
_EdfaConfigEntry_Object = MibTableRow
edfaConfigEntry = _EdfaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1)
)
edfaConfigEntry.setIndexNames(
    (0, "SL-EDFA-MIB", "edfaIfIndex"),
)
if mibBuilder.loadTexts:
    edfaConfigEntry.setStatus("current")
_EdfaIfIndex_Type = InterfaceIndex
_EdfaIfIndex_Object = MibTableColumn
edfaIfIndex = _EdfaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 1),
    _EdfaIfIndex_Type()
)
edfaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaIfIndex.setStatus("current")
_EdfaPumpTemp_Type = Integer32
_EdfaPumpTemp_Object = MibTableColumn
edfaPumpTemp = _EdfaPumpTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 2),
    _EdfaPumpTemp_Type()
)
edfaPumpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPumpTemp.setStatus("current")
_EdfaRxPower_Type = Integer32
_EdfaRxPower_Object = MibTableColumn
edfaRxPower = _EdfaRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 3),
    _EdfaRxPower_Type()
)
edfaRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaRxPower.setStatus("current")


class _EdfaPumpAdminStatus_Type(Integer32):
    """Custom type edfaPumpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("restart", 3))
    )


_EdfaPumpAdminStatus_Type.__name__ = "Integer32"
_EdfaPumpAdminStatus_Object = MibTableColumn
edfaPumpAdminStatus = _EdfaPumpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 4),
    _EdfaPumpAdminStatus_Type()
)
edfaPumpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaPumpAdminStatus.setStatus("current")


class _EdfaPumpOperStatus_Type(Integer32):
    """Custom type edfaPumpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("restart", 3),
          ("unknown", 4))
    )


_EdfaPumpOperStatus_Type.__name__ = "Integer32"
_EdfaPumpOperStatus_Object = MibTableColumn
edfaPumpOperStatus = _EdfaPumpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 5),
    _EdfaPumpOperStatus_Type()
)
edfaPumpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPumpOperStatus.setStatus("current")


class _EdfaStatus_Type(Integer32):
    """Custom type edfaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_EdfaStatus_Type.__name__ = "Integer32"
_EdfaStatus_Object = MibTableColumn
edfaStatus = _EdfaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 6),
    _EdfaStatus_Type()
)
edfaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaStatus.setStatus("current")
_EdfaVoa_Type = Integer32
_EdfaVoa_Object = MibTableColumn
edfaVoa = _EdfaVoa_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 7),
    _EdfaVoa_Type()
)
edfaVoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaVoa.setStatus("current")
_EdfaAutomaticMode_Type = TruthValue
_EdfaAutomaticMode_Object = MibTableColumn
edfaAutomaticMode = _EdfaAutomaticMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 8),
    _EdfaAutomaticMode_Type()
)
edfaAutomaticMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaAutomaticMode.setStatus("current")


class _EdfaAdminControlMode_Type(Integer32):
    """Custom type edfaAdminControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apc", 1),
          ("agc", 2))
    )


_EdfaAdminControlMode_Type.__name__ = "Integer32"
_EdfaAdminControlMode_Object = MibTableColumn
edfaAdminControlMode = _EdfaAdminControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 9),
    _EdfaAdminControlMode_Type()
)
edfaAdminControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaAdminControlMode.setStatus("current")


class _EdfaOperControlMode_Type(Integer32):
    """Custom type edfaOperControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apc", 1),
          ("agc", 2))
    )


_EdfaOperControlMode_Type.__name__ = "Integer32"
_EdfaOperControlMode_Object = MibTableColumn
edfaOperControlMode = _EdfaOperControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 10),
    _EdfaOperControlMode_Type()
)
edfaOperControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaOperControlMode.setStatus("current")
_EdfaAdminGain_Type = Integer32
_EdfaAdminGain_Object = MibTableColumn
edfaAdminGain = _EdfaAdminGain_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 11),
    _EdfaAdminGain_Type()
)
edfaAdminGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaAdminGain.setStatus("current")
_EdfaOperGain_Type = Integer32
_EdfaOperGain_Object = MibTableColumn
edfaOperGain = _EdfaOperGain_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 12),
    _EdfaOperGain_Type()
)
edfaOperGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaOperGain.setStatus("current")
_EdfaAdminOutputPower_Type = Integer32
_EdfaAdminOutputPower_Object = MibTableColumn
edfaAdminOutputPower = _EdfaAdminOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 13),
    _EdfaAdminOutputPower_Type()
)
edfaAdminOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaAdminOutputPower.setStatus("current")
_EdfaOperOutputPower_Type = Integer32
_EdfaOperOutputPower_Object = MibTableColumn
edfaOperOutputPower = _EdfaOperOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 14),
    _EdfaOperOutputPower_Type()
)
edfaOperOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaOperOutputPower.setStatus("current")
_EdfaChannelsNumber_Type = Integer32
_EdfaChannelsNumber_Object = MibTableColumn
edfaChannelsNumber = _EdfaChannelsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 15),
    _EdfaChannelsNumber_Type()
)
edfaChannelsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaChannelsNumber.setStatus("current")
_EdfaTotalChannelsNumber_Type = Integer32
_EdfaTotalChannelsNumber_Object = MibTableColumn
edfaTotalChannelsNumber = _EdfaTotalChannelsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 16),
    _EdfaTotalChannelsNumber_Type()
)
edfaTotalChannelsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaTotalChannelsNumber.setStatus("current")
_EdfaEyeSafetyMode_Type = TruthValue
_EdfaEyeSafetyMode_Object = MibTableColumn
edfaEyeSafetyMode = _EdfaEyeSafetyMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 17),
    _EdfaEyeSafetyMode_Type()
)
edfaEyeSafetyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaEyeSafetyMode.setStatus("current")
_EdfaShutDownLipEnable_Type = TruthValue
_EdfaShutDownLipEnable_Object = MibTableColumn
edfaShutDownLipEnable = _EdfaShutDownLipEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 18),
    _EdfaShutDownLipEnable_Type()
)
edfaShutDownLipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaShutDownLipEnable.setStatus("current")
_EdfaAutoPowerUpLipEnable_Type = TruthValue
_EdfaAutoPowerUpLipEnable_Object = MibTableColumn
edfaAutoPowerUpLipEnable = _EdfaAutoPowerUpLipEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 19),
    _EdfaAutoPowerUpLipEnable_Type()
)
edfaAutoPowerUpLipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaAutoPowerUpLipEnable.setStatus("current")
_EdfaMaxGain_Type = Integer32
_EdfaMaxGain_Object = MibTableColumn
edfaMaxGain = _EdfaMaxGain_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 20),
    _EdfaMaxGain_Type()
)
edfaMaxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaMaxGain.setStatus("current")
_EdfaGainInFrom_Type = Integer32
_EdfaGainInFrom_Object = MibTableColumn
edfaGainInFrom = _EdfaGainInFrom_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 21),
    _EdfaGainInFrom_Type()
)
edfaGainInFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaGainInFrom.setStatus("current")
_EdfaGainInTo_Type = Integer32
_EdfaGainInTo_Object = MibTableColumn
edfaGainInTo = _EdfaGainInTo_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 22),
    _EdfaGainInTo_Type()
)
edfaGainInTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaGainInTo.setStatus("current")
_EdfaGainOutFrom_Type = Integer32
_EdfaGainOutFrom_Object = MibTableColumn
edfaGainOutFrom = _EdfaGainOutFrom_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 23),
    _EdfaGainOutFrom_Type()
)
edfaGainOutFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaGainOutFrom.setStatus("current")
_EdfaGainOutTo_Type = Integer32
_EdfaGainOutTo_Object = MibTableColumn
edfaGainOutTo = _EdfaGainOutTo_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 24),
    _EdfaGainOutTo_Type()
)
edfaGainOutTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaGainOutTo.setStatus("current")
_EdfaPowerInFrom_Type = Integer32
_EdfaPowerInFrom_Object = MibTableColumn
edfaPowerInFrom = _EdfaPowerInFrom_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 25),
    _EdfaPowerInFrom_Type()
)
edfaPowerInFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPowerInFrom.setStatus("current")
_EdfaPowerInTo_Type = Integer32
_EdfaPowerInTo_Object = MibTableColumn
edfaPowerInTo = _EdfaPowerInTo_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 26),
    _EdfaPowerInTo_Type()
)
edfaPowerInTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPowerInTo.setStatus("current")
_EdfaPowerOutFrom_Type = Integer32
_EdfaPowerOutFrom_Object = MibTableColumn
edfaPowerOutFrom = _EdfaPowerOutFrom_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 27),
    _EdfaPowerOutFrom_Type()
)
edfaPowerOutFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPowerOutFrom.setStatus("current")
_EdfaPowerOutTo_Type = Integer32
_EdfaPowerOutTo_Object = MibTableColumn
edfaPowerOutTo = _EdfaPowerOutTo_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 28),
    _EdfaPowerOutTo_Type()
)
edfaPowerOutTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaPowerOutTo.setStatus("current")
_EdfaFromChannel_Type = Integer32
_EdfaFromChannel_Object = MibTableColumn
edfaFromChannel = _EdfaFromChannel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 29),
    _EdfaFromChannel_Type()
)
edfaFromChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaFromChannel.setStatus("current")
_EdfaToChannel_Type = Integer32
_EdfaToChannel_Object = MibTableColumn
edfaToChannel = _EdfaToChannel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 30),
    _EdfaToChannel_Type()
)
edfaToChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaToChannel.setStatus("current")
_EdfaOscChannel_Type = Integer32
_EdfaOscChannel_Object = MibTableColumn
edfaOscChannel = _EdfaOscChannel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 31),
    _EdfaOscChannel_Type()
)
edfaOscChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaOscChannel.setStatus("current")


class _EdfaRedBlueType_Type(Integer32):
    """Custom type edfaRedBlueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("red", 1),
          ("blue", 2),
          ("none", 3))
    )


_EdfaRedBlueType_Type.__name__ = "Integer32"
_EdfaRedBlueType_Object = MibTableColumn
edfaRedBlueType = _EdfaRedBlueType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 32),
    _EdfaRedBlueType_Type()
)
edfaRedBlueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaRedBlueType.setStatus("current")


class _EdfaRole_Type(Integer32):
    """Custom type edfaRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("booster", 1),
          ("boosterInline", 2),
          ("preamp", 3),
          ("inline", 4),
          ("raman", 5),
          ("other", 6))
    )


_EdfaRole_Type.__name__ = "Integer32"
_EdfaRole_Object = MibTableColumn
edfaRole = _EdfaRole_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 33),
    _EdfaRole_Type()
)
edfaRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaRole.setStatus("current")
_EdfaFreeDescription_Type = DisplayString
_EdfaFreeDescription_Object = MibTableColumn
edfaFreeDescription = _EdfaFreeDescription_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 34),
    _EdfaFreeDescription_Type()
)
edfaFreeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaFreeDescription.setStatus("current")
_EdfaConfigSafetyThreshold_Type = Integer32
_EdfaConfigSafetyThreshold_Object = MibTableColumn
edfaConfigSafetyThreshold = _EdfaConfigSafetyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 1, 1, 1, 35),
    _EdfaConfigSafetyThreshold_Type()
)
edfaConfigSafetyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfaConfigSafetyThreshold.setStatus("current")
_EdfaTraps_ObjectIdentity = ObjectIdentity
edfaTraps = _EdfaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 2)
)
_EdfaTraps0_ObjectIdentity = ObjectIdentity
edfaTraps0 = _EdfaTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 0)
)

# Managed Objects groups


# Notification objects

edfaStatusChange0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 0, 1)
)
edfaStatusChange0.setObjects(
      *(("SL-EDFA-MIB", "edfaIfIndex"),
        ("SL-EDFA-MIB", "edfaStatus"))
)
if mibBuilder.loadTexts:
    edfaStatusChange0.setStatus(
        "current"
    )

edfaControlModeChange0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 0, 2)
)
edfaControlModeChange0.setObjects(
      *(("SL-EDFA-MIB", "edfaIfIndex"),
        ("SL-EDFA-MIB", "edfaOperControlMode"))
)
if mibBuilder.loadTexts:
    edfaControlModeChange0.setStatus(
        "current"
    )

edfaStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 1)
)
edfaStatusChange.setObjects(
      *(("SL-EDFA-MIB", "edfaIfIndex"),
        ("SL-EDFA-MIB", "edfaStatus"))
)
if mibBuilder.loadTexts:
    edfaStatusChange.setStatus(
        "current"
    )

edfaControlModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 9, 2, 2)
)
edfaControlModeChange.setObjects(
      *(("SL-EDFA-MIB", "edfaIfIndex"),
        ("SL-EDFA-MIB", "edfaOperControlMode"))
)
if mibBuilder.loadTexts:
    edfaControlModeChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-EDFA-MIB",
    **{"slEdfa": slEdfa,
       "edfaConfig": edfaConfig,
       "edfaConfigTable": edfaConfigTable,
       "edfaConfigEntry": edfaConfigEntry,
       "edfaIfIndex": edfaIfIndex,
       "edfaPumpTemp": edfaPumpTemp,
       "edfaRxPower": edfaRxPower,
       "edfaPumpAdminStatus": edfaPumpAdminStatus,
       "edfaPumpOperStatus": edfaPumpOperStatus,
       "edfaStatus": edfaStatus,
       "edfaVoa": edfaVoa,
       "edfaAutomaticMode": edfaAutomaticMode,
       "edfaAdminControlMode": edfaAdminControlMode,
       "edfaOperControlMode": edfaOperControlMode,
       "edfaAdminGain": edfaAdminGain,
       "edfaOperGain": edfaOperGain,
       "edfaAdminOutputPower": edfaAdminOutputPower,
       "edfaOperOutputPower": edfaOperOutputPower,
       "edfaChannelsNumber": edfaChannelsNumber,
       "edfaTotalChannelsNumber": edfaTotalChannelsNumber,
       "edfaEyeSafetyMode": edfaEyeSafetyMode,
       "edfaShutDownLipEnable": edfaShutDownLipEnable,
       "edfaAutoPowerUpLipEnable": edfaAutoPowerUpLipEnable,
       "edfaMaxGain": edfaMaxGain,
       "edfaGainInFrom": edfaGainInFrom,
       "edfaGainInTo": edfaGainInTo,
       "edfaGainOutFrom": edfaGainOutFrom,
       "edfaGainOutTo": edfaGainOutTo,
       "edfaPowerInFrom": edfaPowerInFrom,
       "edfaPowerInTo": edfaPowerInTo,
       "edfaPowerOutFrom": edfaPowerOutFrom,
       "edfaPowerOutTo": edfaPowerOutTo,
       "edfaFromChannel": edfaFromChannel,
       "edfaToChannel": edfaToChannel,
       "edfaOscChannel": edfaOscChannel,
       "edfaRedBlueType": edfaRedBlueType,
       "edfaRole": edfaRole,
       "edfaFreeDescription": edfaFreeDescription,
       "edfaConfigSafetyThreshold": edfaConfigSafetyThreshold,
       "edfaTraps": edfaTraps,
       "edfaTraps0": edfaTraps0,
       "edfaStatusChange0": edfaStatusChange0,
       "edfaControlModeChange0": edfaControlModeChange0,
       "edfaStatusChange": edfaStatusChange,
       "edfaControlModeChange": edfaControlModeChange}
)
