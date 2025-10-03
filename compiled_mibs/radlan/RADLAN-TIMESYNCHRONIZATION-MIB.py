# SNMP MIB module (RADLAN-TIMESYNCHRONIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\radlan\RADLAN-TIMESYNCHRONIZATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:44 2025
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(TruthValue,) = mibBuilder.importSymbols(
    "RADLAN-SNMPv2",
    "TruthValue")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY

rlTimeSynchronization = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 92)
)
if mibBuilder.loadTexts:
    rlTimeSynchronization.setRevisions(
        ("2003-11-23 00:24",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NTPTimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class NTPSignedTimeValue(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class NTPStratum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_RlTimeSyncMethodMode_ObjectIdentity = ObjectIdentity
rlTimeSyncMethodMode = _RlTimeSyncMethodMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 92, 1)
)
_RlTimeSyncMibVersion_Type = Integer32
_RlTimeSyncMibVersion_Object = MibScalar
rlTimeSyncMibVersion = _RlTimeSyncMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 1),
    _RlTimeSyncMibVersion_Type()
)
rlTimeSyncMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTimeSyncMibVersion.setStatus("current")


class _RndTimeSyncManagedTime_Type(DisplayString):
    """Custom type rndTimeSyncManagedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RndTimeSyncManagedTime_Type.__name__ = "DisplayString"
_RndTimeSyncManagedTime_Object = MibScalar
rndTimeSyncManagedTime = _RndTimeSyncManagedTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 2),
    _RndTimeSyncManagedTime_Type()
)
rndTimeSyncManagedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndTimeSyncManagedTime.setStatus("current")


class _RndTimeSyncManagedDate_Type(DisplayString):
    """Custom type rndTimeSyncManagedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RndTimeSyncManagedDate_Type.__name__ = "DisplayString"
_RndTimeSyncManagedDate_Object = MibScalar
rndTimeSyncManagedDate = _RndTimeSyncManagedDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 3),
    _RndTimeSyncManagedDate_Type()
)
rndTimeSyncManagedDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndTimeSyncManagedDate.setStatus("current")


class _RndTimeSyncManagedDateTime_Type(DisplayString):
    """Custom type rndTimeSyncManagedDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_RndTimeSyncManagedDateTime_Type.__name__ = "DisplayString"
_RndTimeSyncManagedDateTime_Object = MibScalar
rndTimeSyncManagedDateTime = _RndTimeSyncManagedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 4),
    _RndTimeSyncManagedDateTime_Type()
)
rndTimeSyncManagedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndTimeSyncManagedDateTime.setStatus("current")


class _RlTimeSyncMethod_Type(Integer32):
    """Custom type rlTimeSyncMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sntp", 2),
          ("ntp", 3))
    )


_RlTimeSyncMethod_Type.__name__ = "Integer32"
_RlTimeSyncMethod_Object = MibScalar
rlTimeSyncMethod = _RlTimeSyncMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 5),
    _RlTimeSyncMethod_Type()
)
rlTimeSyncMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeSyncMethod.setStatus("current")


class _RlTimeZone_Type(DisplayString):
    """Custom type rlTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RlTimeZone_Type.__name__ = "DisplayString"
_RlTimeZone_Object = MibScalar
rlTimeZone = _RlTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 6),
    _RlTimeZone_Type()
)
rlTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZone.setStatus("current")


class _RlTimeZoneCode_Type(DisplayString):
    """Custom type rlTimeZoneCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlTimeZoneCode_Type.__name__ = "DisplayString"
_RlTimeZoneCode_Object = MibScalar
rlTimeZoneCode = _RlTimeZoneCode_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 7),
    _RlTimeZoneCode_Type()
)
rlTimeZoneCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneCode.setStatus("current")


class _RlDaylightSavingTimeMode_Type(Integer32):
    """Custom type rlDaylightSavingTimeMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("recurring", 1),
          ("date", 2),
          ("none", 3))
    )


_RlDaylightSavingTimeMode_Type.__name__ = "Integer32"
_RlDaylightSavingTimeMode_Object = MibScalar
rlDaylightSavingTimeMode = _RlDaylightSavingTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 8),
    _RlDaylightSavingTimeMode_Type()
)
rlDaylightSavingTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeMode.setStatus("current")


class _RlDaylightSavingTimeStart_Type(OctetString):
    """Custom type rlDaylightSavingTimeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_RlDaylightSavingTimeStart_Type.__name__ = "OctetString"
_RlDaylightSavingTimeStart_Object = MibScalar
rlDaylightSavingTimeStart = _RlDaylightSavingTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 9),
    _RlDaylightSavingTimeStart_Type()
)
rlDaylightSavingTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeStart.setStatus("current")


class _RlDaylightSavingTimeEnd_Type(OctetString):
    """Custom type rlDaylightSavingTimeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_RlDaylightSavingTimeEnd_Type.__name__ = "OctetString"
_RlDaylightSavingTimeEnd_Object = MibScalar
rlDaylightSavingTimeEnd = _RlDaylightSavingTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 10),
    _RlDaylightSavingTimeEnd_Type()
)
rlDaylightSavingTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeEnd.setStatus("current")


class _RlDaylightSavingTimeOffset_Type(Integer32):
    """Custom type rlDaylightSavingTimeOffset based on Integer32"""
    defaultValue = 60


_RlDaylightSavingTimeOffset_Type.__name__ = "Integer32"
_RlDaylightSavingTimeOffset_Object = MibScalar
rlDaylightSavingTimeOffset = _RlDaylightSavingTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 11),
    _RlDaylightSavingTimeOffset_Type()
)
rlDaylightSavingTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeOffset.setStatus("current")


class _RlDaylightSavingTimeCode_Type(DisplayString):
    """Custom type rlDaylightSavingTimeCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlDaylightSavingTimeCode_Type.__name__ = "DisplayString"
_RlDaylightSavingTimeCode_Object = MibScalar
rlDaylightSavingTimeCode = _RlDaylightSavingTimeCode_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 12),
    _RlDaylightSavingTimeCode_Type()
)
rlDaylightSavingTimeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeCode.setStatus("current")
_RlTZDSTOffset_Type = Integer32
_RlTZDSTOffset_Object = MibScalar
rlTZDSTOffset = _RlTZDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 1, 13),
    _RlTZDSTOffset_Type()
)
rlTZDSTOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTZDSTOffset.setStatus("current")
_RlSntpNtpClient_ObjectIdentity = ObjectIdentity
rlSntpNtpClient = _RlSntpNtpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 92, 2)
)
_RlSntpNtpConfig_ObjectIdentity = ObjectIdentity
rlSntpNtpConfig = _RlSntpNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1)
)
_RlSntpNtpMibVersion_Type = Integer32
_RlSntpNtpMibVersion_Object = MibScalar
rlSntpNtpMibVersion = _RlSntpNtpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 1),
    _RlSntpNtpMibVersion_Type()
)
rlSntpNtpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpMibVersion.setStatus("current")


class _RlSntpNtpConfigMode_Type(Integer32):
    """Custom type rlSntpNtpConfigMode based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("unicast", 2),
          ("anycast", 3),
          ("multicast", 4),
          ("unicastAnycast", 5),
          ("unicastMulticast", 6),
          ("anycastMulticast", 7),
          ("unicastAnycastMulticast", 8))
    )


_RlSntpNtpConfigMode_Type.__name__ = "Integer32"
_RlSntpNtpConfigMode_Object = MibScalar
rlSntpNtpConfigMode = _RlSntpNtpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 2),
    _RlSntpNtpConfigMode_Type()
)
rlSntpNtpConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigMode.setStatus("current")
_RlSntpNtpConfigSysStratum_Type = NTPStratum
_RlSntpNtpConfigSysStratum_Object = MibScalar
rlSntpNtpConfigSysStratum = _RlSntpNtpConfigSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 3),
    _RlSntpNtpConfigSysStratum_Type()
)
rlSntpNtpConfigSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSysStratum.setStatus("current")


class _RlSntpNtpConfigPollInterval_Type(Integer32):
    """Custom type rlSntpNtpConfigPollInterval based on Integer32"""
    defaultValue = 1024


_RlSntpNtpConfigPollInterval_Type.__name__ = "Integer32"
_RlSntpNtpConfigPollInterval_Object = MibScalar
rlSntpNtpConfigPollInterval = _RlSntpNtpConfigPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 4),
    _RlSntpNtpConfigPollInterval_Type()
)
rlSntpNtpConfigPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPollInterval.setStatus("current")
_RlSntpNtpConfigPrimaryPollSrvAddr_Type = IpAddress
_RlSntpNtpConfigPrimaryPollSrvAddr_Object = MibScalar
rlSntpNtpConfigPrimaryPollSrvAddr = _RlSntpNtpConfigPrimaryPollSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 5),
    _RlSntpNtpConfigPrimaryPollSrvAddr_Type()
)
rlSntpNtpConfigPrimaryPollSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPrimaryPollSrvAddr.setStatus("current")
_RlSntpNtpConfigPrimaryPollSrvMrid_Type = Integer32
_RlSntpNtpConfigPrimaryPollSrvMrid_Object = MibScalar
rlSntpNtpConfigPrimaryPollSrvMrid = _RlSntpNtpConfigPrimaryPollSrvMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 6),
    _RlSntpNtpConfigPrimaryPollSrvMrid_Type()
)
rlSntpNtpConfigPrimaryPollSrvMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPrimaryPollSrvMrid.setStatus("current")
_RlSntpNtpConfigPrimaryPollSrvIfIndex_Type = Integer32
_RlSntpNtpConfigPrimaryPollSrvIfIndex_Object = MibScalar
rlSntpNtpConfigPrimaryPollSrvIfIndex = _RlSntpNtpConfigPrimaryPollSrvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 7),
    _RlSntpNtpConfigPrimaryPollSrvIfIndex_Type()
)
rlSntpNtpConfigPrimaryPollSrvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPrimaryPollSrvIfIndex.setStatus("current")
_RlSntpNtpConfigPrimaryPollSrvStratum_Type = NTPStratum
_RlSntpNtpConfigPrimaryPollSrvStratum_Object = MibScalar
rlSntpNtpConfigPrimaryPollSrvStratum = _RlSntpNtpConfigPrimaryPollSrvStratum_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 8),
    _RlSntpNtpConfigPrimaryPollSrvStratum_Type()
)
rlSntpNtpConfigPrimaryPollSrvStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPrimaryPollSrvStratum.setStatus("current")
_RlSntpNtpConfigSyncSrvAddr_Type = IpAddress
_RlSntpNtpConfigSyncSrvAddr_Object = MibScalar
rlSntpNtpConfigSyncSrvAddr = _RlSntpNtpConfigSyncSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 9),
    _RlSntpNtpConfigSyncSrvAddr_Type()
)
rlSntpNtpConfigSyncSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvAddr.setStatus("current")
_RlSntpNtpConfigSyncSrvMrid_Type = Integer32
_RlSntpNtpConfigSyncSrvMrid_Object = MibScalar
rlSntpNtpConfigSyncSrvMrid = _RlSntpNtpConfigSyncSrvMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 10),
    _RlSntpNtpConfigSyncSrvMrid_Type()
)
rlSntpNtpConfigSyncSrvMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvMrid.setStatus("current")
_RlSntpNtpConfigSyncSrvIfIndex_Type = Integer32
_RlSntpNtpConfigSyncSrvIfIndex_Object = MibScalar
rlSntpNtpConfigSyncSrvIfIndex = _RlSntpNtpConfigSyncSrvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 11),
    _RlSntpNtpConfigSyncSrvIfIndex_Type()
)
rlSntpNtpConfigSyncSrvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvIfIndex.setStatus("current")


class _RlSntpNtpConfigSyncSrvType_Type(Integer32):
    """Custom type rlSntpNtpConfigSyncSrvType based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("unicast", 2),
          ("anycast", 3),
          ("broadcast", 4))
    )


_RlSntpNtpConfigSyncSrvType_Type.__name__ = "Integer32"
_RlSntpNtpConfigSyncSrvType_Object = MibScalar
rlSntpNtpConfigSyncSrvType = _RlSntpNtpConfigSyncSrvType_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 12),
    _RlSntpNtpConfigSyncSrvType_Type()
)
rlSntpNtpConfigSyncSrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvType.setStatus("current")
_RlSntpNtpConfigSyncSrvStratum_Type = NTPStratum
_RlSntpNtpConfigSyncSrvStratum_Object = MibScalar
rlSntpNtpConfigSyncSrvStratum = _RlSntpNtpConfigSyncSrvStratum_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 13),
    _RlSntpNtpConfigSyncSrvStratum_Type()
)
rlSntpNtpConfigSyncSrvStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvStratum.setStatus("current")
_RlSntpNtpConfigRetryTimeout_Type = Integer32
_RlSntpNtpConfigRetryTimeout_Object = MibScalar
rlSntpNtpConfigRetryTimeout = _RlSntpNtpConfigRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 14),
    _RlSntpNtpConfigRetryTimeout_Type()
)
rlSntpNtpConfigRetryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigRetryTimeout.setStatus("current")
_RlSntpNtpConfigRetryCnt_Type = Integer32
_RlSntpNtpConfigRetryCnt_Object = MibScalar
rlSntpNtpConfigRetryCnt = _RlSntpNtpConfigRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 1, 15),
    _RlSntpNtpConfigRetryCnt_Type()
)
rlSntpNtpConfigRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigRetryCnt.setStatus("current")
_RlSntpConfig_ObjectIdentity = ObjectIdentity
rlSntpConfig = _RlSntpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2)
)


class _RlSntpClientMode_Type(Integer32):
    """Custom type rlSntpClientMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("passive", 3))
    )


_RlSntpClientMode_Type.__name__ = "Integer32"
_RlSntpClientMode_Object = MibScalar
rlSntpClientMode = _RlSntpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 1),
    _RlSntpClientMode_Type()
)
rlSntpClientMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpClientMode.setStatus("current")


class _RlSntpUnicastAdminState_Type(Integer32):
    """Custom type rlSntpUnicastAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlSntpUnicastAdminState_Type.__name__ = "Integer32"
_RlSntpUnicastAdminState_Object = MibScalar
rlSntpUnicastAdminState = _RlSntpUnicastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 2),
    _RlSntpUnicastAdminState_Type()
)
rlSntpUnicastAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpUnicastAdminState.setStatus("current")


class _RlSntpBroadcastAdminState_Type(Integer32):
    """Custom type rlSntpBroadcastAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlSntpBroadcastAdminState_Type.__name__ = "Integer32"
_RlSntpBroadcastAdminState_Object = MibScalar
rlSntpBroadcastAdminState = _RlSntpBroadcastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 3),
    _RlSntpBroadcastAdminState_Type()
)
rlSntpBroadcastAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastAdminState.setStatus("current")


class _RlSntpAnycastAdminState_Type(Integer32):
    """Custom type rlSntpAnycastAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlSntpAnycastAdminState_Type.__name__ = "Integer32"
_RlSntpAnycastAdminState_Object = MibScalar
rlSntpAnycastAdminState = _RlSntpAnycastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 4),
    _RlSntpAnycastAdminState_Type()
)
rlSntpAnycastAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAnycastAdminState.setStatus("current")


class _RlSntpUnicastPollState_Type(TruthValue):
    """Custom type rlSntpUnicastPollState based on TruthValue"""
    defaultValue = 2


_RlSntpUnicastPollState_Type.__name__ = "TruthValue"
_RlSntpUnicastPollState_Object = MibScalar
rlSntpUnicastPollState = _RlSntpUnicastPollState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 5),
    _RlSntpUnicastPollState_Type()
)
rlSntpUnicastPollState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpUnicastPollState.setStatus("current")


class _RlSntpBroadcastPollState_Type(TruthValue):
    """Custom type rlSntpBroadcastPollState based on TruthValue"""
    defaultValue = 2


_RlSntpBroadcastPollState_Type.__name__ = "TruthValue"
_RlSntpBroadcastPollState_Object = MibScalar
rlSntpBroadcastPollState = _RlSntpBroadcastPollState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 6),
    _RlSntpBroadcastPollState_Type()
)
rlSntpBroadcastPollState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastPollState.setStatus("current")


class _RlSntpAnycastPollState_Type(TruthValue):
    """Custom type rlSntpAnycastPollState based on TruthValue"""
    defaultValue = 2


_RlSntpAnycastPollState_Type.__name__ = "TruthValue"
_RlSntpAnycastPollState_Object = MibScalar
rlSntpAnycastPollState = _RlSntpAnycastPollState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 7),
    _RlSntpAnycastPollState_Type()
)
rlSntpAnycastPollState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAnycastPollState.setStatus("current")


class _RlSntpAuthenticationState_Type(Integer32):
    """Custom type rlSntpAuthenticationState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlSntpAuthenticationState_Type.__name__ = "Integer32"
_RlSntpAuthenticationState_Object = MibScalar
rlSntpAuthenticationState = _RlSntpAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 8),
    _RlSntpAuthenticationState_Type()
)
rlSntpAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationState.setStatus("current")


class _RlTimeValidFlag_Type(TruthValue):
    """Custom type rlTimeValidFlag based on TruthValue"""
    defaultValue = 2


_RlTimeValidFlag_Type.__name__ = "TruthValue"
_RlTimeValidFlag_Object = MibScalar
rlTimeValidFlag = _RlTimeValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 9),
    _RlTimeValidFlag_Type()
)
rlTimeValidFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeValidFlag.setStatus("current")
_RlSntpConfigBroadcastTable_Object = MibTable
rlSntpConfigBroadcastTable = _RlSntpConfigBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10)
)
if mibBuilder.loadTexts:
    rlSntpConfigBroadcastTable.setStatus("current")
_RlSntpBroadcastEntry_Object = MibTableRow
rlSntpBroadcastEntry = _RlSntpBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1)
)
rlSntpBroadcastEntry.setIndexNames(
    (0, "RADLAN-TIMESYNCHRONIZATION-MIB", "rlSntpBroadcastIfIndex"),
)
if mibBuilder.loadTexts:
    rlSntpBroadcastEntry.setStatus("current")
_RlSntpBroadcastIfIndex_Type = Integer32
_RlSntpBroadcastIfIndex_Object = MibTableColumn
rlSntpBroadcastIfIndex = _RlSntpBroadcastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 1),
    _RlSntpBroadcastIfIndex_Type()
)
rlSntpBroadcastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpBroadcastIfIndex.setStatus("current")


class _RlSntpBroadcastIfAdminState_Type(Integer32):
    """Custom type rlSntpBroadcastIfAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlSntpBroadcastIfAdminState_Type.__name__ = "Integer32"
_RlSntpBroadcastIfAdminState_Object = MibTableColumn
rlSntpBroadcastIfAdminState = _RlSntpBroadcastIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 2),
    _RlSntpBroadcastIfAdminState_Type()
)
rlSntpBroadcastIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastIfAdminState.setStatus("current")


class _RlSntpBroadcastMode_Type(Integer32):
    """Custom type rlSntpBroadcastMode based on Integer32"""
    defaultValue = 4

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
        *(("none", 1),
          ("receive", 2),
          ("send", 3),
          ("receiveSend", 4))
    )


_RlSntpBroadcastMode_Type.__name__ = "Integer32"
_RlSntpBroadcastMode_Object = MibTableColumn
rlSntpBroadcastMode = _RlSntpBroadcastMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 3),
    _RlSntpBroadcastMode_Type()
)
rlSntpBroadcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastMode.setStatus("current")


class _RlSntpBroadcastPolled_Type(TruthValue):
    """Custom type rlSntpBroadcastPolled based on TruthValue"""
    defaultValue = 2


_RlSntpBroadcastPolled_Type.__name__ = "TruthValue"
_RlSntpBroadcastPolled_Object = MibTableColumn
rlSntpBroadcastPolled = _RlSntpBroadcastPolled_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 4),
    _RlSntpBroadcastPolled_Type()
)
rlSntpBroadcastPolled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastPolled.setStatus("current")
_RlSntpBroadcastAddress_Type = IpAddress
_RlSntpBroadcastAddress_Object = MibTableColumn
rlSntpBroadcastAddress = _RlSntpBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 5),
    _RlSntpBroadcastAddress_Type()
)
rlSntpBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastAddress.setStatus("current")
_RlSntpBroadcastStratum_Type = NTPStratum
_RlSntpBroadcastStratum_Object = MibTableColumn
rlSntpBroadcastStratum = _RlSntpBroadcastStratum_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 6),
    _RlSntpBroadcastStratum_Type()
)
rlSntpBroadcastStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastStratum.setStatus("current")
_RlSntpBroadcastLastResp_Type = NTPTimeStamp
_RlSntpBroadcastLastResp_Object = MibTableColumn
rlSntpBroadcastLastResp = _RlSntpBroadcastLastResp_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 7),
    _RlSntpBroadcastLastResp_Type()
)
rlSntpBroadcastLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastLastResp.setStatus("current")


class _RlSntpBroadcastStatus_Type(Integer32):
    """Custom type rlSntpBroadcastStatus based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("inProcess", 2),
          ("up", 3),
          ("down", 4))
    )


_RlSntpBroadcastStatus_Type.__name__ = "Integer32"
_RlSntpBroadcastStatus_Object = MibTableColumn
rlSntpBroadcastStatus = _RlSntpBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 8),
    _RlSntpBroadcastStatus_Type()
)
rlSntpBroadcastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastStatus.setStatus("current")
_RlSntpBroadcastOffset_Type = NTPTimeStamp
_RlSntpBroadcastOffset_Object = MibTableColumn
rlSntpBroadcastOffset = _RlSntpBroadcastOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 9),
    _RlSntpBroadcastOffset_Type()
)
rlSntpBroadcastOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpBroadcastOffset.setUnits("seconds")
_RlSntpBroadcastDelay_Type = NTPSignedTimeValue
_RlSntpBroadcastDelay_Object = MibTableColumn
rlSntpBroadcastDelay = _RlSntpBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 10),
    _RlSntpBroadcastDelay_Type()
)
rlSntpBroadcastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpBroadcastDelay.setUnits("seconds")
_RlSntpBroadcastRowStatus_Type = RowStatus
_RlSntpBroadcastRowStatus_Object = MibTableColumn
rlSntpBroadcastRowStatus = _RlSntpBroadcastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 10, 1, 11),
    _RlSntpBroadcastRowStatus_Type()
)
rlSntpBroadcastRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastRowStatus.setStatus("current")
_RlSntpConfigAnycastTable_Object = MibTable
rlSntpConfigAnycastTable = _RlSntpConfigAnycastTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11)
)
if mibBuilder.loadTexts:
    rlSntpConfigAnycastTable.setStatus("current")
_RlSntpAnycastEntry_Object = MibTableRow
rlSntpAnycastEntry = _RlSntpAnycastEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1)
)
rlSntpAnycastEntry.setIndexNames(
    (0, "RADLAN-TIMESYNCHRONIZATION-MIB", "rlSntpAnycastIfIndex"),
)
if mibBuilder.loadTexts:
    rlSntpAnycastEntry.setStatus("current")
_RlSntpAnycastIfIndex_Type = Integer32
_RlSntpAnycastIfIndex_Object = MibTableColumn
rlSntpAnycastIfIndex = _RlSntpAnycastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 1),
    _RlSntpAnycastIfIndex_Type()
)
rlSntpAnycastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpAnycastIfIndex.setStatus("current")
_RlSntpAnycastAddress_Type = IpAddress
_RlSntpAnycastAddress_Object = MibTableColumn
rlSntpAnycastAddress = _RlSntpAnycastAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 2),
    _RlSntpAnycastAddress_Type()
)
rlSntpAnycastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastAddress.setStatus("current")
_RlSntpAnycastStratum_Type = NTPStratum
_RlSntpAnycastStratum_Object = MibTableColumn
rlSntpAnycastStratum = _RlSntpAnycastStratum_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 3),
    _RlSntpAnycastStratum_Type()
)
rlSntpAnycastStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastStratum.setStatus("current")
_RlSntpAnycastLastResp_Type = NTPTimeStamp
_RlSntpAnycastLastResp_Object = MibTableColumn
rlSntpAnycastLastResp = _RlSntpAnycastLastResp_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 4),
    _RlSntpAnycastLastResp_Type()
)
rlSntpAnycastLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastLastResp.setStatus("current")


class _RlSntpAnycastStatus_Type(Integer32):
    """Custom type rlSntpAnycastStatus based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("inProcess", 2),
          ("up", 3),
          ("down", 4))
    )


_RlSntpAnycastStatus_Type.__name__ = "Integer32"
_RlSntpAnycastStatus_Object = MibTableColumn
rlSntpAnycastStatus = _RlSntpAnycastStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 5),
    _RlSntpAnycastStatus_Type()
)
rlSntpAnycastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastStatus.setStatus("current")
_RlSntpAnycastOffset_Type = NTPTimeStamp
_RlSntpAnycastOffset_Object = MibTableColumn
rlSntpAnycastOffset = _RlSntpAnycastOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 6),
    _RlSntpAnycastOffset_Type()
)
rlSntpAnycastOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpAnycastOffset.setUnits("seconds")
_RlSntpAnycastDelay_Type = NTPSignedTimeValue
_RlSntpAnycastDelay_Object = MibTableColumn
rlSntpAnycastDelay = _RlSntpAnycastDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 7),
    _RlSntpAnycastDelay_Type()
)
rlSntpAnycastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpAnycastDelay.setUnits("seconds")
_RlSntpAnycastRowStatus_Type = RowStatus
_RlSntpAnycastRowStatus_Object = MibTableColumn
rlSntpAnycastRowStatus = _RlSntpAnycastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 11, 1, 8),
    _RlSntpAnycastRowStatus_Type()
)
rlSntpAnycastRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAnycastRowStatus.setStatus("current")
_RlSntpConfigServerTable_Object = MibTable
rlSntpConfigServerTable = _RlSntpConfigServerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12)
)
if mibBuilder.loadTexts:
    rlSntpConfigServerTable.setStatus("current")
_RlSntpServerEntry_Object = MibTableRow
rlSntpServerEntry = _RlSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1)
)
rlSntpServerEntry.setIndexNames(
    (0, "RADLAN-TIMESYNCHRONIZATION-MIB", "rlSntpServerAddress"),
)
if mibBuilder.loadTexts:
    rlSntpServerEntry.setStatus("current")
_RlSntpServerAddress_Type = IpAddress
_RlSntpServerAddress_Object = MibTableColumn
rlSntpServerAddress = _RlSntpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 1),
    _RlSntpServerAddress_Type()
)
rlSntpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpServerAddress.setStatus("current")


class _RlSntpServerPolled_Type(TruthValue):
    """Custom type rlSntpServerPolled based on TruthValue"""
    defaultValue = 2


_RlSntpServerPolled_Type.__name__ = "TruthValue"
_RlSntpServerPolled_Object = MibTableColumn
rlSntpServerPolled = _RlSntpServerPolled_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 2),
    _RlSntpServerPolled_Type()
)
rlSntpServerPolled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServerPolled.setStatus("current")
_RlSntpServerStratum_Type = NTPStratum
_RlSntpServerStratum_Object = MibTableColumn
rlSntpServerStratum = _RlSntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 3),
    _RlSntpServerStratum_Type()
)
rlSntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerStratum.setStatus("current")
_RlSntpServerLastResp_Type = NTPTimeStamp
_RlSntpServerLastResp_Object = MibTableColumn
rlSntpServerLastResp = _RlSntpServerLastResp_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 4),
    _RlSntpServerLastResp_Type()
)
rlSntpServerLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerLastResp.setStatus("current")


class _RlSntpServerStatus_Type(Integer32):
    """Custom type rlSntpServerStatus based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("inProcess", 2),
          ("up", 3),
          ("down", 4))
    )


_RlSntpServerStatus_Type.__name__ = "Integer32"
_RlSntpServerStatus_Object = MibTableColumn
rlSntpServerStatus = _RlSntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 5),
    _RlSntpServerStatus_Type()
)
rlSntpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerStatus.setStatus("current")
_RlSntpServersOffset_Type = NTPTimeStamp
_RlSntpServersOffset_Object = MibTableColumn
rlSntpServersOffset = _RlSntpServersOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 6),
    _RlSntpServersOffset_Type()
)
rlSntpServersOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServersOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpServersOffset.setUnits("seconds")
_RlSntpServersDelay_Type = NTPSignedTimeValue
_RlSntpServersDelay_Object = MibTableColumn
rlSntpServersDelay = _RlSntpServersDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 7),
    _RlSntpServersDelay_Type()
)
rlSntpServersDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServersDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpServersDelay.setUnits("seconds")
_RlSntpServersKeyIdentifier_Type = Unsigned32
_RlSntpServersKeyIdentifier_Object = MibTableColumn
rlSntpServersKeyIdentifier = _RlSntpServersKeyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 8),
    _RlSntpServersKeyIdentifier_Type()
)
rlSntpServersKeyIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServersKeyIdentifier.setStatus("current")
_RlSntpServerRowStatus_Type = RowStatus
_RlSntpServerRowStatus_Object = MibTableColumn
rlSntpServerRowStatus = _RlSntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 12, 1, 9),
    _RlSntpServerRowStatus_Type()
)
rlSntpServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServerRowStatus.setStatus("current")
_RlSntpConfigAuthenticationTable_Object = MibTable
rlSntpConfigAuthenticationTable = _RlSntpConfigAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13)
)
if mibBuilder.loadTexts:
    rlSntpConfigAuthenticationTable.setStatus("current")
_RlSntpAuthenticationEntry_Object = MibTableRow
rlSntpAuthenticationEntry = _RlSntpAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1)
)
rlSntpAuthenticationEntry.setIndexNames(
    (0, "RADLAN-TIMESYNCHRONIZATION-MIB", "rlSntpAuthenticationKeyID"),
)
if mibBuilder.loadTexts:
    rlSntpAuthenticationEntry.setStatus("current")


class _RlSntpAuthenticationKeyID_Type(Unsigned32):
    """Custom type rlSntpAuthenticationKeyID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlSntpAuthenticationKeyID_Type.__name__ = "Unsigned32"
_RlSntpAuthenticationKeyID_Object = MibTableColumn
rlSntpAuthenticationKeyID = _RlSntpAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1, 1),
    _RlSntpAuthenticationKeyID_Type()
)
rlSntpAuthenticationKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationKeyID.setStatus("current")


class _RlSntpAuthenticationKeyValue_Type(DisplayString):
    """Custom type rlSntpAuthenticationKeyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RlSntpAuthenticationKeyValue_Type.__name__ = "DisplayString"
_RlSntpAuthenticationKeyValue_Object = MibTableColumn
rlSntpAuthenticationKeyValue = _RlSntpAuthenticationKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1, 2),
    _RlSntpAuthenticationKeyValue_Type()
)
rlSntpAuthenticationKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationKeyValue.setStatus("current")


class _RlSntpAuthenticationKeyState_Type(Integer32):
    """Custom type rlSntpAuthenticationKeyState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlSntpAuthenticationKeyState_Type.__name__ = "Integer32"
_RlSntpAuthenticationKeyState_Object = MibTableColumn
rlSntpAuthenticationKeyState = _RlSntpAuthenticationKeyState_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1, 3),
    _RlSntpAuthenticationKeyState_Type()
)
rlSntpAuthenticationKeyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationKeyState.setStatus("current")
_RlSntpAuthenticationRowStatus_Type = RowStatus
_RlSntpAuthenticationRowStatus_Object = MibTableColumn
rlSntpAuthenticationRowStatus = _RlSntpAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 2, 13, 1, 4),
    _RlSntpAuthenticationRowStatus_Type()
)
rlSntpAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationRowStatus.setStatus("current")
_RlNtpConfig_ObjectIdentity = ObjectIdentity
rlNtpConfig = _RlNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 92, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-TIMESYNCHRONIZATION-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPSignedTimeValue": NTPSignedTimeValue,
       "NTPStratum": NTPStratum,
       "rlTimeSynchronization": rlTimeSynchronization,
       "rlTimeSyncMethodMode": rlTimeSyncMethodMode,
       "rlTimeSyncMibVersion": rlTimeSyncMibVersion,
       "rndTimeSyncManagedTime": rndTimeSyncManagedTime,
       "rndTimeSyncManagedDate": rndTimeSyncManagedDate,
       "rndTimeSyncManagedDateTime": rndTimeSyncManagedDateTime,
       "rlTimeSyncMethod": rlTimeSyncMethod,
       "rlTimeZone": rlTimeZone,
       "rlTimeZoneCode": rlTimeZoneCode,
       "rlDaylightSavingTimeMode": rlDaylightSavingTimeMode,
       "rlDaylightSavingTimeStart": rlDaylightSavingTimeStart,
       "rlDaylightSavingTimeEnd": rlDaylightSavingTimeEnd,
       "rlDaylightSavingTimeOffset": rlDaylightSavingTimeOffset,
       "rlDaylightSavingTimeCode": rlDaylightSavingTimeCode,
       "rlTZDSTOffset": rlTZDSTOffset,
       "rlSntpNtpClient": rlSntpNtpClient,
       "rlSntpNtpConfig": rlSntpNtpConfig,
       "rlSntpNtpMibVersion": rlSntpNtpMibVersion,
       "rlSntpNtpConfigMode": rlSntpNtpConfigMode,
       "rlSntpNtpConfigSysStratum": rlSntpNtpConfigSysStratum,
       "rlSntpNtpConfigPollInterval": rlSntpNtpConfigPollInterval,
       "rlSntpNtpConfigPrimaryPollSrvAddr": rlSntpNtpConfigPrimaryPollSrvAddr,
       "rlSntpNtpConfigPrimaryPollSrvMrid": rlSntpNtpConfigPrimaryPollSrvMrid,
       "rlSntpNtpConfigPrimaryPollSrvIfIndex": rlSntpNtpConfigPrimaryPollSrvIfIndex,
       "rlSntpNtpConfigPrimaryPollSrvStratum": rlSntpNtpConfigPrimaryPollSrvStratum,
       "rlSntpNtpConfigSyncSrvAddr": rlSntpNtpConfigSyncSrvAddr,
       "rlSntpNtpConfigSyncSrvMrid": rlSntpNtpConfigSyncSrvMrid,
       "rlSntpNtpConfigSyncSrvIfIndex": rlSntpNtpConfigSyncSrvIfIndex,
       "rlSntpNtpConfigSyncSrvType": rlSntpNtpConfigSyncSrvType,
       "rlSntpNtpConfigSyncSrvStratum": rlSntpNtpConfigSyncSrvStratum,
       "rlSntpNtpConfigRetryTimeout": rlSntpNtpConfigRetryTimeout,
       "rlSntpNtpConfigRetryCnt": rlSntpNtpConfigRetryCnt,
       "rlSntpConfig": rlSntpConfig,
       "rlSntpClientMode": rlSntpClientMode,
       "rlSntpUnicastAdminState": rlSntpUnicastAdminState,
       "rlSntpBroadcastAdminState": rlSntpBroadcastAdminState,
       "rlSntpAnycastAdminState": rlSntpAnycastAdminState,
       "rlSntpUnicastPollState": rlSntpUnicastPollState,
       "rlSntpBroadcastPollState": rlSntpBroadcastPollState,
       "rlSntpAnycastPollState": rlSntpAnycastPollState,
       "rlSntpAuthenticationState": rlSntpAuthenticationState,
       "rlTimeValidFlag": rlTimeValidFlag,
       "rlSntpConfigBroadcastTable": rlSntpConfigBroadcastTable,
       "rlSntpBroadcastEntry": rlSntpBroadcastEntry,
       "rlSntpBroadcastIfIndex": rlSntpBroadcastIfIndex,
       "rlSntpBroadcastIfAdminState": rlSntpBroadcastIfAdminState,
       "rlSntpBroadcastMode": rlSntpBroadcastMode,
       "rlSntpBroadcastPolled": rlSntpBroadcastPolled,
       "rlSntpBroadcastAddress": rlSntpBroadcastAddress,
       "rlSntpBroadcastStratum": rlSntpBroadcastStratum,
       "rlSntpBroadcastLastResp": rlSntpBroadcastLastResp,
       "rlSntpBroadcastStatus": rlSntpBroadcastStatus,
       "rlSntpBroadcastOffset": rlSntpBroadcastOffset,
       "rlSntpBroadcastDelay": rlSntpBroadcastDelay,
       "rlSntpBroadcastRowStatus": rlSntpBroadcastRowStatus,
       "rlSntpConfigAnycastTable": rlSntpConfigAnycastTable,
       "rlSntpAnycastEntry": rlSntpAnycastEntry,
       "rlSntpAnycastIfIndex": rlSntpAnycastIfIndex,
       "rlSntpAnycastAddress": rlSntpAnycastAddress,
       "rlSntpAnycastStratum": rlSntpAnycastStratum,
       "rlSntpAnycastLastResp": rlSntpAnycastLastResp,
       "rlSntpAnycastStatus": rlSntpAnycastStatus,
       "rlSntpAnycastOffset": rlSntpAnycastOffset,
       "rlSntpAnycastDelay": rlSntpAnycastDelay,
       "rlSntpAnycastRowStatus": rlSntpAnycastRowStatus,
       "rlSntpConfigServerTable": rlSntpConfigServerTable,
       "rlSntpServerEntry": rlSntpServerEntry,
       "rlSntpServerAddress": rlSntpServerAddress,
       "rlSntpServerPolled": rlSntpServerPolled,
       "rlSntpServerStratum": rlSntpServerStratum,
       "rlSntpServerLastResp": rlSntpServerLastResp,
       "rlSntpServerStatus": rlSntpServerStatus,
       "rlSntpServersOffset": rlSntpServersOffset,
       "rlSntpServersDelay": rlSntpServersDelay,
       "rlSntpServersKeyIdentifier": rlSntpServersKeyIdentifier,
       "rlSntpServerRowStatus": rlSntpServerRowStatus,
       "rlSntpConfigAuthenticationTable": rlSntpConfigAuthenticationTable,
       "rlSntpAuthenticationEntry": rlSntpAuthenticationEntry,
       "rlSntpAuthenticationKeyID": rlSntpAuthenticationKeyID,
       "rlSntpAuthenticationKeyValue": rlSntpAuthenticationKeyValue,
       "rlSntpAuthenticationKeyState": rlSntpAuthenticationKeyState,
       "rlSntpAuthenticationRowStatus": rlSntpAuthenticationRowStatus,
       "rlNtpConfig": rlNtpConfig}
)
