# SNMP MIB module (SL-SNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-SNTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:08 2025
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

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slSntp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlSntpConfig_ObjectIdentity = ObjectIdentity
slSntpConfig = _SlSntpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1)
)


class _SlSntpConfigMode_Type(Integer32):
    """Custom type slSntpConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("unicast", 2),
          ("broadcast", 3))
    )


_SlSntpConfigMode_Type.__name__ = "Integer32"
_SlSntpConfigMode_Object = MibScalar
slSntpConfigMode = _SlSntpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 1),
    _SlSntpConfigMode_Type()
)
slSntpConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSntpConfigMode.setStatus("current")


class _SlSntpConfigPollInterval_Type(Integer32):
    """Custom type slSntpConfigPollInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_SlSntpConfigPollInterval_Type.__name__ = "Integer32"
_SlSntpConfigPollInterval_Object = MibScalar
slSntpConfigPollInterval = _SlSntpConfigPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 2),
    _SlSntpConfigPollInterval_Type()
)
slSntpConfigPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSntpConfigPollInterval.setStatus("current")


class _SlSntpConfigRetryCount_Type(Integer32):
    """Custom type slSntpConfigRetryCount based on Integer32"""
    defaultValue = 3


_SlSntpConfigRetryCount_Type.__name__ = "Integer32"
_SlSntpConfigRetryCount_Object = MibScalar
slSntpConfigRetryCount = _SlSntpConfigRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 3),
    _SlSntpConfigRetryCount_Type()
)
slSntpConfigRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSntpConfigRetryCount.setStatus("current")


class _SlSntpConfigTimeZone_Type(Integer32):
    """Custom type slSntpConfigTimeZone based on Integer32"""
    defaultValue = 0


_SlSntpConfigTimeZone_Type.__name__ = "Integer32"
_SlSntpConfigTimeZone_Object = MibScalar
slSntpConfigTimeZone = _SlSntpConfigTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 4),
    _SlSntpConfigTimeZone_Type()
)
slSntpConfigTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSntpConfigTimeZone.setStatus("current")


class _SlSntpConfigDayLightSaving_Type(TruthValue):
    """Custom type slSntpConfigDayLightSaving based on TruthValue"""
    defaultValue = 2


_SlSntpConfigDayLightSaving_Type.__name__ = "TruthValue"
_SlSntpConfigDayLightSaving_Object = MibScalar
slSntpConfigDayLightSaving = _SlSntpConfigDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 5),
    _SlSntpConfigDayLightSaving_Type()
)
slSntpConfigDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSntpConfigDayLightSaving.setStatus("current")


class _SlSntpConfigFractTimeZone_Type(Integer32):
    """Custom type slSntpConfigFractTimeZone based on Integer32"""
    defaultValue = 0


_SlSntpConfigFractTimeZone_Type.__name__ = "Integer32"
_SlSntpConfigFractTimeZone_Object = MibScalar
slSntpConfigFractTimeZone = _SlSntpConfigFractTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 6),
    _SlSntpConfigFractTimeZone_Type()
)
slSntpConfigFractTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSntpConfigFractTimeZone.setStatus("current")
_SlSntpConfigTable_Object = MibTable
slSntpConfigTable = _SlSntpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10)
)
if mibBuilder.loadTexts:
    slSntpConfigTable.setStatus("current")
_SlSntpConfigEntry_Object = MibTableRow
slSntpConfigEntry = _SlSntpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1)
)
slSntpConfigEntry.setIndexNames(
    (0, "SL-SNTP-MIB", "slSntpConfigAddress"),
)
if mibBuilder.loadTexts:
    slSntpConfigEntry.setStatus("current")
_SlSntpConfigAddress_Type = IpAddress
_SlSntpConfigAddress_Object = MibTableColumn
slSntpConfigAddress = _SlSntpConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 1),
    _SlSntpConfigAddress_Type()
)
slSntpConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSntpConfigAddress.setStatus("current")


class _SlSntpConfigVersion_Type(Integer32):
    """Custom type slSntpConfigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_SlSntpConfigVersion_Type.__name__ = "Integer32"
_SlSntpConfigVersion_Object = MibTableColumn
slSntpConfigVersion = _SlSntpConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 2),
    _SlSntpConfigVersion_Type()
)
slSntpConfigVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSntpConfigVersion.setStatus("current")


class _SlSntpConfigPriority_Type(Integer32):
    """Custom type slSntpConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlSntpConfigPriority_Type.__name__ = "Integer32"
_SlSntpConfigPriority_Object = MibTableColumn
slSntpConfigPriority = _SlSntpConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 3),
    _SlSntpConfigPriority_Type()
)
slSntpConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSntpConfigPriority.setStatus("current")
_SlSntpConfigRowStatus_Type = RowStatus
_SlSntpConfigRowStatus_Object = MibTableColumn
slSntpConfigRowStatus = _SlSntpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 4),
    _SlSntpConfigRowStatus_Type()
)
slSntpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSntpConfigRowStatus.setStatus("current")


class _SlSntpConfigMaxVariance_Type(Integer32):
    """Custom type slSntpConfigMaxVariance based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200000),
    )


_SlSntpConfigMaxVariance_Type.__name__ = "Integer32"
_SlSntpConfigMaxVariance_Object = MibTableColumn
slSntpConfigMaxVariance = _SlSntpConfigMaxVariance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 5),
    _SlSntpConfigMaxVariance_Type()
)
slSntpConfigMaxVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSntpConfigMaxVariance.setStatus("current")
_SlSntpConfigVariance_Type = Integer32
_SlSntpConfigVariance_Object = MibTableColumn
slSntpConfigVariance = _SlSntpConfigVariance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 6),
    _SlSntpConfigVariance_Type()
)
slSntpConfigVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSntpConfigVariance.setStatus("current")


class _SlSntpConfigVarianceDetectEnable_Type(TruthValue):
    """Custom type slSntpConfigVarianceDetectEnable based on TruthValue"""
    defaultValue = 2


_SlSntpConfigVarianceDetectEnable_Type.__name__ = "TruthValue"
_SlSntpConfigVarianceDetectEnable_Object = MibTableColumn
slSntpConfigVarianceDetectEnable = _SlSntpConfigVarianceDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 7),
    _SlSntpConfigVarianceDetectEnable_Type()
)
slSntpConfigVarianceDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSntpConfigVarianceDetectEnable.setStatus("current")


class _SlSntpConfigServerStatus_Type(Integer32):
    """Custom type slSntpConfigServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disconnected", 1),
          ("connected", 2))
    )


_SlSntpConfigServerStatus_Type.__name__ = "Integer32"
_SlSntpConfigServerStatus_Object = MibTableColumn
slSntpConfigServerStatus = _SlSntpConfigServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 1, 10, 1, 8),
    _SlSntpConfigServerStatus_Type()
)
slSntpConfigServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSntpConfigServerStatus.setStatus("current")
_SlSntpTraps_ObjectIdentity = ObjectIdentity
slSntpTraps = _SlSntpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2)
)

# Managed Objects groups


# Notification objects

slSntpPeerFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2, 1)
)
slSntpPeerFailureTrap.setObjects(
    ("SL-SNTP-MIB", "slSntpConfigAddress")
)
if mibBuilder.loadTexts:
    slSntpPeerFailureTrap.setStatus(
        "current"
    )

slSntpConfigVarianceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 21, 2, 2)
)
slSntpConfigVarianceTrap.setObjects(
      *(("SL-SNTP-MIB", "slSntpConfigAddress"),
        ("SL-SNTP-MIB", "slSntpConfigMaxVariance"),
        ("SL-SNTP-MIB", "slSntpConfigVariance"))
)
if mibBuilder.loadTexts:
    slSntpConfigVarianceTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-SNTP-MIB",
    **{"slSntp": slSntp,
       "slSntpConfig": slSntpConfig,
       "slSntpConfigMode": slSntpConfigMode,
       "slSntpConfigPollInterval": slSntpConfigPollInterval,
       "slSntpConfigRetryCount": slSntpConfigRetryCount,
       "slSntpConfigTimeZone": slSntpConfigTimeZone,
       "slSntpConfigDayLightSaving": slSntpConfigDayLightSaving,
       "slSntpConfigFractTimeZone": slSntpConfigFractTimeZone,
       "slSntpConfigTable": slSntpConfigTable,
       "slSntpConfigEntry": slSntpConfigEntry,
       "slSntpConfigAddress": slSntpConfigAddress,
       "slSntpConfigVersion": slSntpConfigVersion,
       "slSntpConfigPriority": slSntpConfigPriority,
       "slSntpConfigRowStatus": slSntpConfigRowStatus,
       "slSntpConfigMaxVariance": slSntpConfigMaxVariance,
       "slSntpConfigVariance": slSntpConfigVariance,
       "slSntpConfigVarianceDetectEnable": slSntpConfigVarianceDetectEnable,
       "slSntpConfigServerStatus": slSntpConfigServerStatus,
       "slSntpTraps": slSntpTraps,
       "slSntpPeerFailureTrap": slSntpPeerFailureTrap,
       "slSntpConfigVarianceTrap": slSntpConfigVarianceTrap}
)
