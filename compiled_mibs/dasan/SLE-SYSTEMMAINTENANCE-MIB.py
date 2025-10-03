# SNMP MIB module (SLE-SYSTEMMAINTENANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-SYSTEMMAINTENANCE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:06 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleSystemMaintenance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1)
)


# Types definitions



class EnableFlag(Integer32):
    """Custom type EnableFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )





class SleDefAutoCliScheduleType(Integer32):
    """Custom type SleDefAutoCliScheduleType based on Integer32"""
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
        *(("periodic", 1),
          ("at", 2),
          ("daily", 3),
          ("immediate", 4))
    )





class SleDefAutoCliScheduleTransferType(Integer32):
    """Custom type SleDefAutoCliScheduleTransferType based on Integer32"""
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
        *(("ftp", 1),
          ("tftp", 2),
          ("memory", 3),
          ("none", 4))
    )





class SleDefAutoCliScheduleResult(Integer32):
    """Custom type SleDefAutoCliScheduleResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleSystemBase_ObjectIdentity = ObjectIdentity
sleSystemBase = _SleSystemBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1)
)
_SleSystemBaseInfo_ObjectIdentity = ObjectIdentity
sleSystemBaseInfo = _SleSystemBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1)
)
_SleSystemModelName_Type = OctetString
_SleSystemModelName_Object = MibScalar
sleSystemModelName = _SleSystemModelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 1),
    _SleSystemModelName_Type()
)
sleSystemModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemModelName.setStatus("current")
_SleSystemSerialNumber_Type = OctetString
_SleSystemSerialNumber_Object = MibScalar
sleSystemSerialNumber = _SleSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 2),
    _SleSystemSerialNumber_Type()
)
sleSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSerialNumber.setStatus("current")
_SleSystemHWVersion_Type = OctetString
_SleSystemHWVersion_Object = MibScalar
sleSystemHWVersion = _SleSystemHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 3),
    _SleSystemHWVersion_Type()
)
sleSystemHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemHWVersion.setStatus("current")
_SleSystemBLVersion_Type = OctetString
_SleSystemBLVersion_Object = MibScalar
sleSystemBLVersion = _SleSystemBLVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 4),
    _SleSystemBLVersion_Type()
)
sleSystemBLVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemBLVersion.setStatus("current")
_SleSystemSWCompatibility_Type = OctetString
_SleSystemSWCompatibility_Object = MibScalar
sleSystemSWCompatibility = _SleSystemSWCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 5),
    _SleSystemSWCompatibility_Type()
)
sleSystemSWCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSWCompatibility.setStatus("current")
_SleSystemOSVersion_Type = OctetString
_SleSystemOSVersion_Object = MibScalar
sleSystemOSVersion = _SleSystemOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 6),
    _SleSystemOSVersion_Type()
)
sleSystemOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemOSVersion.setStatus("current")
_SleSystemMacAddress_Type = MacAddress
_SleSystemMacAddress_Object = MibScalar
sleSystemMacAddress = _SleSystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 7),
    _SleSystemMacAddress_Type()
)
sleSystemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMacAddress.setStatus("current")
_SleSystemHostName_Type = OctetString
_SleSystemHostName_Object = MibScalar
sleSystemHostName = _SleSystemHostName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 8),
    _SleSystemHostName_Type()
)
sleSystemHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemHostName.setStatus("current")
_SleSystemCPULoadAll_Type = OctetString
_SleSystemCPULoadAll_Object = MibScalar
sleSystemCPULoadAll = _SleSystemCPULoadAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 9),
    _SleSystemCPULoadAll_Type()
)
sleSystemCPULoadAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemCPULoadAll.setStatus("current")
_SleSystemCPULoadInterrupt_Type = OctetString
_SleSystemCPULoadInterrupt_Object = MibScalar
sleSystemCPULoadInterrupt = _SleSystemCPULoadInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 10),
    _SleSystemCPULoadInterrupt_Type()
)
sleSystemCPULoadInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemCPULoadInterrupt.setStatus("current")


class _SleSystemCPUThreshold_Type(Integer32):
    """Custom type sleSystemCPUThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SleSystemCPUThreshold_Type.__name__ = "Integer32"
_SleSystemCPUThreshold_Object = MibScalar
sleSystemCPUThreshold = _SleSystemCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 11),
    _SleSystemCPUThreshold_Type()
)
sleSystemCPUThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemCPUThreshold.setStatus("current")


class _SleSystemCPUInterval_Type(Integer32):
    """Custom type sleSystemCPUInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(600, 600),
    )


_SleSystemCPUInterval_Type.__name__ = "Integer32"
_SleSystemCPUInterval_Object = MibScalar
sleSystemCPUInterval = _SleSystemCPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 12),
    _SleSystemCPUInterval_Type()
)
sleSystemCPUInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemCPUInterval.setStatus("current")
_SleSystemMemoryTotal_Type = Unsigned32
_SleSystemMemoryTotal_Object = MibScalar
sleSystemMemoryTotal = _SleSystemMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 13),
    _SleSystemMemoryTotal_Type()
)
sleSystemMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMemoryTotal.setStatus("current")
_SleSystemMemoryFree_Type = Unsigned32
_SleSystemMemoryFree_Object = MibScalar
sleSystemMemoryFree = _SleSystemMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 14),
    _SleSystemMemoryFree_Type()
)
sleSystemMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMemoryFree.setStatus("current")
_SleSystemMemoryShared_Type = Unsigned32
_SleSystemMemoryShared_Object = MibScalar
sleSystemMemoryShared = _SleSystemMemoryShared_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 15),
    _SleSystemMemoryShared_Type()
)
sleSystemMemoryShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMemoryShared.setStatus("current")
_SleSystemMemoryBuffers_Type = Unsigned32
_SleSystemMemoryBuffers_Object = MibScalar
sleSystemMemoryBuffers = _SleSystemMemoryBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 16),
    _SleSystemMemoryBuffers_Type()
)
sleSystemMemoryBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMemoryBuffers.setStatus("current")
_SleSystemMemoryCached_Type = Unsigned32
_SleSystemMemoryCached_Object = MibScalar
sleSystemMemoryCached = _SleSystemMemoryCached_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 17),
    _SleSystemMemoryCached_Type()
)
sleSystemMemoryCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMemoryCached.setStatus("current")
_SleSystemMemorySwapTotal_Type = Unsigned32
_SleSystemMemorySwapTotal_Object = MibScalar
sleSystemMemorySwapTotal = _SleSystemMemorySwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 18),
    _SleSystemMemorySwapTotal_Type()
)
sleSystemMemorySwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMemorySwapTotal.setStatus("current")
_SleSystemMemorySwapFree_Type = Unsigned32
_SleSystemMemorySwapFree_Object = MibScalar
sleSystemMemorySwapFree = _SleSystemMemorySwapFree_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 19),
    _SleSystemMemorySwapFree_Type()
)
sleSystemMemorySwapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMemorySwapFree.setStatus("current")


class _SleSystemDefaultOS_Type(Integer32):
    """Custom type sleSystemDefaultOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDualOS", 0),
          ("os1", 1),
          ("os2", 2))
    )


_SleSystemDefaultOS_Type.__name__ = "Integer32"
_SleSystemDefaultOS_Object = MibScalar
sleSystemDefaultOS = _SleSystemDefaultOS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 20),
    _SleSystemDefaultOS_Type()
)
sleSystemDefaultOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemDefaultOS.setStatus("current")
_SleSystemOS1Version_Type = OctetString
_SleSystemOS1Version_Object = MibScalar
sleSystemOS1Version = _SleSystemOS1Version_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 21),
    _SleSystemOS1Version_Type()
)
sleSystemOS1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemOS1Version.setStatus("current")
_SleSystemOS1Size_Type = Unsigned32
_SleSystemOS1Size_Object = MibScalar
sleSystemOS1Size = _SleSystemOS1Size_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 22),
    _SleSystemOS1Size_Type()
)
sleSystemOS1Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemOS1Size.setStatus("current")
_SleSystemOS1BuildNumber_Type = OctetString
_SleSystemOS1BuildNumber_Object = MibScalar
sleSystemOS1BuildNumber = _SleSystemOS1BuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 23),
    _SleSystemOS1BuildNumber_Type()
)
sleSystemOS1BuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemOS1BuildNumber.setStatus("current")
_SleSystemOS2Version_Type = OctetString
_SleSystemOS2Version_Object = MibScalar
sleSystemOS2Version = _SleSystemOS2Version_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 24),
    _SleSystemOS2Version_Type()
)
sleSystemOS2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemOS2Version.setStatus("current")
_SleSystemOS2Size_Type = Unsigned32
_SleSystemOS2Size_Object = MibScalar
sleSystemOS2Size = _SleSystemOS2Size_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 25),
    _SleSystemOS2Size_Type()
)
sleSystemOS2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemOS2Size.setStatus("current")
_SleSystemOS2BuildNumber_Type = OctetString
_SleSystemOS2BuildNumber_Object = MibScalar
sleSystemOS2BuildNumber = _SleSystemOS2BuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 26),
    _SleSystemOS2BuildNumber_Type()
)
sleSystemOS2BuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemOS2BuildNumber.setStatus("current")
_SleSystemFlashTotalSize_Type = Unsigned32
_SleSystemFlashTotalSize_Object = MibScalar
sleSystemFlashTotalSize = _SleSystemFlashTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 27),
    _SleSystemFlashTotalSize_Type()
)
sleSystemFlashTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemFlashTotalSize.setStatus("current")
_SleSystemFlashOSSize_Type = Unsigned32
_SleSystemFlashOSSize_Object = MibScalar
sleSystemFlashOSSize = _SleSystemFlashOSSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 28),
    _SleSystemFlashOSSize_Type()
)
sleSystemFlashOSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemFlashOSSize.setStatus("current")
_SleSystemFlashConfigSize_Type = Unsigned32
_SleSystemFlashConfigSize_Object = MibScalar
sleSystemFlashConfigSize = _SleSystemFlashConfigSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 29),
    _SleSystemFlashConfigSize_Type()
)
sleSystemFlashConfigSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemFlashConfigSize.setStatus("current")
_SleSystemFlashOSUsedSize_Type = Unsigned32
_SleSystemFlashOSUsedSize_Object = MibScalar
sleSystemFlashOSUsedSize = _SleSystemFlashOSUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 30),
    _SleSystemFlashOSUsedSize_Type()
)
sleSystemFlashOSUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemFlashOSUsedSize.setStatus("current")
_SleSystemFlashConfigUsedSize_Type = Unsigned32
_SleSystemFlashConfigUsedSize_Object = MibScalar
sleSystemFlashConfigUsedSize = _SleSystemFlashConfigUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 31),
    _SleSystemFlashConfigUsedSize_Type()
)
sleSystemFlashConfigUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemFlashConfigUsedSize.setStatus("current")
_SleSystemClock_Type = OctetString
_SleSystemClock_Object = MibScalar
sleSystemClock = _SleSystemClock_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 32),
    _SleSystemClock_Type()
)
sleSystemClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemClock.setStatus("current")
_SleSystemTimezone_Type = OctetString
_SleSystemTimezone_Object = MibScalar
sleSystemTimezone = _SleSystemTimezone_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 33),
    _SleSystemTimezone_Type()
)
sleSystemTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemTimezone.setStatus("current")
_SleSystemDNSDomainName_Type = OctetString
_SleSystemDNSDomainName_Object = MibScalar
sleSystemDNSDomainName = _SleSystemDNSDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 34),
    _SleSystemDNSDomainName_Type()
)
sleSystemDNSDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemDNSDomainName.setStatus("current")
_SleSystemInitBanner_Type = OctetString
_SleSystemInitBanner_Object = MibScalar
sleSystemInitBanner = _SleSystemInitBanner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 35),
    _SleSystemInitBanner_Type()
)
sleSystemInitBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemInitBanner.setStatus("current")
_SleSystemSuccessBanner_Type = OctetString
_SleSystemSuccessBanner_Object = MibScalar
sleSystemSuccessBanner = _SleSystemSuccessBanner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 36),
    _SleSystemSuccessBanner_Type()
)
sleSystemSuccessBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSuccessBanner.setStatus("current")
_SleSystemFailBanner_Type = OctetString
_SleSystemFailBanner_Object = MibScalar
sleSystemFailBanner = _SleSystemFailBanner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 37),
    _SleSystemFailBanner_Type()
)
sleSystemFailBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemFailBanner.setStatus("current")


class _SleSystemSyslogState_Type(Integer32):
    """Custom type sleSystemSyslogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", -2),
          ("stop", 0),
          ("start", 1))
    )


_SleSystemSyslogState_Type.__name__ = "Integer32"
_SleSystemSyslogState_Object = MibScalar
sleSystemSyslogState = _SleSystemSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 38),
    _SleSystemSyslogState_Type()
)
sleSystemSyslogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSyslogState.setStatus("current")
_SleSystemSyslogVolatileNumber_Type = Integer32
_SleSystemSyslogVolatileNumber_Object = MibScalar
sleSystemSyslogVolatileNumber = _SleSystemSyslogVolatileNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 39),
    _SleSystemSyslogVolatileNumber_Type()
)
sleSystemSyslogVolatileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSyslogVolatileNumber.setStatus("current")
_SleSystemSyslogNonVolatileNumber_Type = Integer32
_SleSystemSyslogNonVolatileNumber_Object = MibScalar
sleSystemSyslogNonVolatileNumber = _SleSystemSyslogNonVolatileNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 40),
    _SleSystemSyslogNonVolatileNumber_Type()
)
sleSystemSyslogNonVolatileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSyslogNonVolatileNumber.setStatus("current")
_SleSystemSyslogBindAddress_Type = IpAddress
_SleSystemSyslogBindAddress_Object = MibScalar
sleSystemSyslogBindAddress = _SleSystemSyslogBindAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 41),
    _SleSystemSyslogBindAddress_Type()
)
sleSystemSyslogBindAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSyslogBindAddress.setStatus("current")


class _SleSystemSyslogLocalCode_Type(Integer32):
    """Custom type sleSystemSyslogLocalCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SleSystemSyslogLocalCode_Type.__name__ = "Integer32"
_SleSystemSyslogLocalCode_Object = MibScalar
sleSystemSyslogLocalCode = _SleSystemSyslogLocalCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 42),
    _SleSystemSyslogLocalCode_Type()
)
sleSystemSyslogLocalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSyslogLocalCode.setStatus("current")


class _SleSystemSSHState_Type(Integer32):
    """Custom type sleSystemSSHState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSystemSSHState_Type.__name__ = "Integer32"
_SleSystemSSHState_Object = MibScalar
sleSystemSSHState = _SleSystemSSHState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 43),
    _SleSystemSSHState_Type()
)
sleSystemSSHState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSSHState.setStatus("current")


class _SleSystemNTPState_Type(Integer32):
    """Custom type sleSystemNTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("ntp", 1),
          ("sntp", 2))
    )


_SleSystemNTPState_Type.__name__ = "Integer32"
_SleSystemNTPState_Object = MibScalar
sleSystemNTPState = _SleSystemNTPState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 44),
    _SleSystemNTPState_Type()
)
sleSystemNTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemNTPState.setStatus("current")
_SleSystemBackupInterval_Type = Integer32
_SleSystemBackupInterval_Object = MibScalar
sleSystemBackupInterval = _SleSystemBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 45),
    _SleSystemBackupInterval_Type()
)
sleSystemBackupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemBackupInterval.setStatus("current")


class _SleSystemDhcpActivity_Type(Integer32):
    """Custom type sleSystemDhcpActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSystemDhcpActivity_Type.__name__ = "Integer32"
_SleSystemDhcpActivity_Object = MibScalar
sleSystemDhcpActivity = _SleSystemDhcpActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 46),
    _SleSystemDhcpActivity_Type()
)
sleSystemDhcpActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemDhcpActivity.setStatus("current")


class _SleSystemDefaultTTL_Type(Integer32):
    """Custom type sleSystemDefaultTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 255),
    )


_SleSystemDefaultTTL_Type.__name__ = "Integer32"
_SleSystemDefaultTTL_Object = MibScalar
sleSystemDefaultTTL = _SleSystemDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 47),
    _SleSystemDefaultTTL_Type()
)
sleSystemDefaultTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemDefaultTTL.setStatus("current")
_SleSystemSyslogVolatileSize_Type = Integer32
_SleSystemSyslogVolatileSize_Object = MibScalar
sleSystemSyslogVolatileSize = _SleSystemSyslogVolatileSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 48),
    _SleSystemSyslogVolatileSize_Type()
)
sleSystemSyslogVolatileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSyslogVolatileSize.setStatus("current")
_SleSystemSyslogBindInterfaceName_Type = OctetString
_SleSystemSyslogBindInterfaceName_Object = MibScalar
sleSystemSyslogBindInterfaceName = _SleSystemSyslogBindInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 49),
    _SleSystemSyslogBindInterfaceName_Type()
)
sleSystemSyslogBindInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSyslogBindInterfaceName.setStatus("current")


class _SleSystemSessionTime_Type(Integer32):
    """Custom type sleSystemSessionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_SleSystemSessionTime_Type.__name__ = "Integer32"
_SleSystemSessionTime_Object = MibScalar
sleSystemSessionTime = _SleSystemSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 50),
    _SleSystemSessionTime_Type()
)
sleSystemSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSessionTime.setStatus("current")


class _SleSystemExecTimeout_Type(Integer32):
    """Custom type sleSystemExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147519),
    )


_SleSystemExecTimeout_Type.__name__ = "Integer32"
_SleSystemExecTimeout_Object = MibScalar
sleSystemExecTimeout = _SleSystemExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 51),
    _SleSystemExecTimeout_Type()
)
sleSystemExecTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemExecTimeout.setStatus("current")


class _SleSystemWatchdogStatus_Type(Integer32):
    """Custom type sleSystemWatchdogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSystemWatchdogStatus_Type.__name__ = "Integer32"
_SleSystemWatchdogStatus_Object = MibScalar
sleSystemWatchdogStatus = _SleSystemWatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 52),
    _SleSystemWatchdogStatus_Type()
)
sleSystemWatchdogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemWatchdogStatus.setStatus("current")
_SleSystemNtpBindInterface_Type = OctetString
_SleSystemNtpBindInterface_Object = MibScalar
sleSystemNtpBindInterface = _SleSystemNtpBindInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 53),
    _SleSystemNtpBindInterface_Type()
)
sleSystemNtpBindInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemNtpBindInterface.setStatus("current")
_SleSystemFtpBindInterface_Type = OctetString
_SleSystemFtpBindInterface_Object = MibScalar
sleSystemFtpBindInterface = _SleSystemFtpBindInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 54),
    _SleSystemFtpBindInterface_Type()
)
sleSystemFtpBindInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemFtpBindInterface.setStatus("current")


class _SleSystemRedundancyPort_Type(Integer32):
    """Custom type sleSystemRedundancyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SleSystemRedundancyPort_Type.__name__ = "Integer32"
_SleSystemRedundancyPort_Object = MibScalar
sleSystemRedundancyPort = _SleSystemRedundancyPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 55),
    _SleSystemRedundancyPort_Type()
)
sleSystemRedundancyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemRedundancyPort.setStatus("current")


class _SleSystemSyslogVolatileMaxLine_Type(Integer32):
    """Custom type sleSystemSyslogVolatileMaxLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 16384),
    )


_SleSystemSyslogVolatileMaxLine_Type.__name__ = "Integer32"
_SleSystemSyslogVolatileMaxLine_Object = MibScalar
sleSystemSyslogVolatileMaxLine = _SleSystemSyslogVolatileMaxLine_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 56),
    _SleSystemSyslogVolatileMaxLine_Type()
)
sleSystemSyslogVolatileMaxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSyslogVolatileMaxLine.setStatus("current")
_SleSystemBootInfo_Type = OctetString
_SleSystemBootInfo_Object = MibScalar
sleSystemBootInfo = _SleSystemBootInfo_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 57),
    _SleSystemBootInfo_Type()
)
sleSystemBootInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemBootInfo.setStatus("current")
_SleSystemTempHighThreshold_Type = Integer32
_SleSystemTempHighThreshold_Object = MibScalar
sleSystemTempHighThreshold = _SleSystemTempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 58),
    _SleSystemTempHighThreshold_Type()
)
sleSystemTempHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemTempHighThreshold.setStatus("current")
_SleSystemTempLowThreshold_Type = Integer32
_SleSystemTempLowThreshold_Object = MibScalar
sleSystemTempLowThreshold = _SleSystemTempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 59),
    _SleSystemTempLowThreshold_Type()
)
sleSystemTempLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemTempLowThreshold.setStatus("current")


class _SleSystemMemThreshold_Type(Integer32):
    """Custom type sleSystemMemThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SleSystemMemThreshold_Type.__name__ = "Integer32"
_SleSystemMemThreshold_Object = MibScalar
sleSystemMemThreshold = _SleSystemMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 60),
    _SleSystemMemThreshold_Type()
)
sleSystemMemThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemMemThreshold.setStatus("current")


class _SleSystemLowCPUThreshold_Type(Integer32):
    """Custom type sleSystemLowCPUThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SleSystemLowCPUThreshold_Type.__name__ = "Integer32"
_SleSystemLowCPUThreshold_Object = MibScalar
sleSystemLowCPUThreshold = _SleSystemLowCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 61),
    _SleSystemLowCPUThreshold_Type()
)
sleSystemLowCPUThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemLowCPUThreshold.setStatus("current")


class _SleSystemLowCPUInterval_Type(Integer32):
    """Custom type sleSystemLowCPUInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(600, 600),
    )


_SleSystemLowCPUInterval_Type.__name__ = "Integer32"
_SleSystemLowCPUInterval_Object = MibScalar
sleSystemLowCPUInterval = _SleSystemLowCPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 62),
    _SleSystemLowCPUInterval_Type()
)
sleSystemLowCPUInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemLowCPUInterval.setStatus("current")


class _SleSystemRunningOS_Type(Integer32):
    """Custom type sleSystemRunningOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDualOS", 0),
          ("os1", 1),
          ("os2", 2))
    )


_SleSystemRunningOS_Type.__name__ = "Integer32"
_SleSystemRunningOS_Object = MibScalar
sleSystemRunningOS = _SleSystemRunningOS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 63),
    _SleSystemRunningOS_Type()
)
sleSystemRunningOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemRunningOS.setStatus("current")
_SleSystemNtpBindAddress_Type = IpAddress
_SleSystemNtpBindAddress_Object = MibScalar
sleSystemNtpBindAddress = _SleSystemNtpBindAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 64),
    _SleSystemNtpBindAddress_Type()
)
sleSystemNtpBindAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemNtpBindAddress.setStatus("current")


class _SleSystemEnablePasswdType_Type(Integer32):
    """Custom type sleSystemEnablePasswdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plain", 1),
          ("encrypt", 2))
    )


_SleSystemEnablePasswdType_Type.__name__ = "Integer32"
_SleSystemEnablePasswdType_Object = MibScalar
sleSystemEnablePasswdType = _SleSystemEnablePasswdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 65),
    _SleSystemEnablePasswdType_Type()
)
sleSystemEnablePasswdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemEnablePasswdType.setStatus("current")


class _SleSystemEnablePasswd_Type(OctetString):
    """Custom type sleSystemEnablePasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SleSystemEnablePasswd_Type.__name__ = "OctetString"
_SleSystemEnablePasswd_Object = MibScalar
sleSystemEnablePasswd = _SleSystemEnablePasswd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 66),
    _SleSystemEnablePasswd_Type()
)
sleSystemEnablePasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemEnablePasswd.setStatus("current")


class _SleSystemServicePasswdEncryption_Type(Integer32):
    """Custom type sleSystemServicePasswdEncryption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSystemServicePasswdEncryption_Type.__name__ = "Integer32"
_SleSystemServicePasswdEncryption_Object = MibScalar
sleSystemServicePasswdEncryption = _SleSystemServicePasswdEncryption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 67),
    _SleSystemServicePasswdEncryption_Type()
)
sleSystemServicePasswdEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemServicePasswdEncryption.setStatus("current")
_SleSystemUptime64_Type = Counter64
_SleSystemUptime64_Object = MibScalar
sleSystemUptime64 = _SleSystemUptime64_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 68),
    _SleSystemUptime64_Type()
)
sleSystemUptime64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUptime64.setStatus("current")


class _SleSystemNtpPollnterval_Type(Integer32):
    """Custom type sleSystemNtpPollnterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 20),
    )


_SleSystemNtpPollnterval_Type.__name__ = "Integer32"
_SleSystemNtpPollnterval_Object = MibScalar
sleSystemNtpPollnterval = _SleSystemNtpPollnterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 69),
    _SleSystemNtpPollnterval_Type()
)
sleSystemNtpPollnterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemNtpPollnterval.setStatus("current")


class _SleSystemCPUDuration_Type(Integer32):
    """Custom type sleSystemCPUDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_SleSystemCPUDuration_Type.__name__ = "Integer32"
_SleSystemCPUDuration_Object = MibScalar
sleSystemCPUDuration = _SleSystemCPUDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 70),
    _SleSystemCPUDuration_Type()
)
sleSystemCPUDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemCPUDuration.setStatus("current")


class _SleSystemLowCPUDuration_Type(Integer32):
    """Custom type sleSystemLowCPUDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_SleSystemLowCPUDuration_Type.__name__ = "Integer32"
_SleSystemLowCPUDuration_Object = MibScalar
sleSystemLowCPUDuration = _SleSystemLowCPUDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 71),
    _SleSystemLowCPUDuration_Type()
)
sleSystemLowCPUDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemLowCPUDuration.setStatus("current")
_SleSystemBarcode_Type = OctetString
_SleSystemBarcode_Object = MibScalar
sleSystemBarcode = _SleSystemBarcode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 72),
    _SleSystemBarcode_Type()
)
sleSystemBarcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemBarcode.setStatus("current")


class _SleSystemEnhancedFeature_Type(Integer32):
    """Custom type sleSystemEnhancedFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSystemEnhancedFeature_Type.__name__ = "Integer32"
_SleSystemEnhancedFeature_Object = MibScalar
sleSystemEnhancedFeature = _SleSystemEnhancedFeature_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 73),
    _SleSystemEnhancedFeature_Type()
)
sleSystemEnhancedFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemEnhancedFeature.setStatus("current")


class _SleSystemGetBranchModel_Type(Integer32):
    """Custom type sleSystemGetBranchModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("nsn", 1))
    )


_SleSystemGetBranchModel_Type.__name__ = "Integer32"
_SleSystemGetBranchModel_Object = MibScalar
sleSystemGetBranchModel = _SleSystemGetBranchModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 74),
    _SleSystemGetBranchModel_Type()
)
sleSystemGetBranchModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemGetBranchModel.setStatus("current")
_SleSystemTargetId_Type = OctetString
_SleSystemTargetId_Object = MibScalar
sleSystemTargetId = _SleSystemTargetId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 75),
    _SleSystemTargetId_Type()
)
sleSystemTargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemTargetId.setStatus("current")
_SleSystemNodeName_Type = OctetString
_SleSystemNodeName_Object = MibScalar
sleSystemNodeName = _SleSystemNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 76),
    _SleSystemNodeName_Type()
)
sleSystemNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemNodeName.setStatus("current")
_SleSystemNetworkName_Type = OctetString
_SleSystemNetworkName_Object = MibScalar
sleSystemNetworkName = _SleSystemNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 77),
    _SleSystemNetworkName_Type()
)
sleSystemNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemNetworkName.setStatus("current")
_SleSystemShelfId_Type = OctetString
_SleSystemShelfId_Object = MibScalar
sleSystemShelfId = _SleSystemShelfId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 78),
    _SleSystemShelfId_Type()
)
sleSystemShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemShelfId.setStatus("current")
_SleSystemSlotId_Type = OctetString
_SleSystemSlotId_Object = MibScalar
sleSystemSlotId = _SleSystemSlotId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 79),
    _SleSystemSlotId_Type()
)
sleSystemSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotId.setStatus("current")


class _SleSystemWebMgmt_Type(Integer32):
    """Custom type sleSystemWebMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSystemWebMgmt_Type.__name__ = "Integer32"
_SleSystemWebMgmt_Object = MibScalar
sleSystemWebMgmt = _SleSystemWebMgmt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 80),
    _SleSystemWebMgmt_Type()
)
sleSystemWebMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemWebMgmt.setStatus("current")
_SleSystemManufacturer_Type = OctetString
_SleSystemManufacturer_Object = MibScalar
sleSystemManufacturer = _SleSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 81),
    _SleSystemManufacturer_Type()
)
sleSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemManufacturer.setStatus("current")
_SleSystemManufactureDate_Type = OctetString
_SleSystemManufactureDate_Object = MibScalar
sleSystemManufactureDate = _SleSystemManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 82),
    _SleSystemManufactureDate_Type()
)
sleSystemManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemManufactureDate.setStatus("current")


class _SleSystemNosUpgradeStatus_Type(Integer32):
    """Custom type sleSystemNosUpgradeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ok", 1),
          ("fail", 2),
          ("inprogress", 3),
          ("unknown", 255))
    )


_SleSystemNosUpgradeStatus_Type.__name__ = "Integer32"
_SleSystemNosUpgradeStatus_Object = MibScalar
sleSystemNosUpgradeStatus = _SleSystemNosUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 83),
    _SleSystemNosUpgradeStatus_Type()
)
sleSystemNosUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemNosUpgradeStatus.setStatus("current")


class _SleSystemAutoReloadInHour_Type(Integer32):
    """Custom type sleSystemAutoReloadInHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SleSystemAutoReloadInHour_Type.__name__ = "Integer32"
_SleSystemAutoReloadInHour_Object = MibScalar
sleSystemAutoReloadInHour = _SleSystemAutoReloadInHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 84),
    _SleSystemAutoReloadInHour_Type()
)
sleSystemAutoReloadInHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutoReloadInHour.setStatus("current")


class _SleSystemAutoReloadInMinutes_Type(Integer32):
    """Custom type sleSystemAutoReloadInMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SleSystemAutoReloadInMinutes_Type.__name__ = "Integer32"
_SleSystemAutoReloadInMinutes_Object = MibScalar
sleSystemAutoReloadInMinutes = _SleSystemAutoReloadInMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 85),
    _SleSystemAutoReloadInMinutes_Type()
)
sleSystemAutoReloadInMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutoReloadInMinutes.setStatus("current")


class _SleSystemAutoReloadDailyHour_Type(Integer32):
    """Custom type sleSystemAutoReloadDailyHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SleSystemAutoReloadDailyHour_Type.__name__ = "Integer32"
_SleSystemAutoReloadDailyHour_Object = MibScalar
sleSystemAutoReloadDailyHour = _SleSystemAutoReloadDailyHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 86),
    _SleSystemAutoReloadDailyHour_Type()
)
sleSystemAutoReloadDailyHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutoReloadDailyHour.setStatus("current")


class _SleSystemAutoReloadDailyMinutes_Type(Integer32):
    """Custom type sleSystemAutoReloadDailyMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SleSystemAutoReloadDailyMinutes_Type.__name__ = "Integer32"
_SleSystemAutoReloadDailyMinutes_Object = MibScalar
sleSystemAutoReloadDailyMinutes = _SleSystemAutoReloadDailyMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 87),
    _SleSystemAutoReloadDailyMinutes_Type()
)
sleSystemAutoReloadDailyMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutoReloadDailyMinutes.setStatus("current")


class _SleSystemAutoReloadAtYear_Type(Integer32):
    """Custom type sleSystemAutoReloadAtYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2008, 2035),
    )


_SleSystemAutoReloadAtYear_Type.__name__ = "Integer32"
_SleSystemAutoReloadAtYear_Object = MibScalar
sleSystemAutoReloadAtYear = _SleSystemAutoReloadAtYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 88),
    _SleSystemAutoReloadAtYear_Type()
)
sleSystemAutoReloadAtYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutoReloadAtYear.setStatus("current")


class _SleSystemAutoReloadAtMonth_Type(Integer32):
    """Custom type sleSystemAutoReloadAtMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_SleSystemAutoReloadAtMonth_Type.__name__ = "Integer32"
_SleSystemAutoReloadAtMonth_Object = MibScalar
sleSystemAutoReloadAtMonth = _SleSystemAutoReloadAtMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 89),
    _SleSystemAutoReloadAtMonth_Type()
)
sleSystemAutoReloadAtMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutoReloadAtMonth.setStatus("current")


class _SleSystemAutoReloadAtDay_Type(Integer32):
    """Custom type sleSystemAutoReloadAtDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SleSystemAutoReloadAtDay_Type.__name__ = "Integer32"
_SleSystemAutoReloadAtDay_Object = MibScalar
sleSystemAutoReloadAtDay = _SleSystemAutoReloadAtDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 90),
    _SleSystemAutoReloadAtDay_Type()
)
sleSystemAutoReloadAtDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutoReloadAtDay.setStatus("current")


class _SleSystemAutpReloadAtHour_Type(Integer32):
    """Custom type sleSystemAutpReloadAtHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SleSystemAutpReloadAtHour_Type.__name__ = "Integer32"
_SleSystemAutpReloadAtHour_Object = MibScalar
sleSystemAutpReloadAtHour = _SleSystemAutpReloadAtHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 91),
    _SleSystemAutpReloadAtHour_Type()
)
sleSystemAutpReloadAtHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutpReloadAtHour.setStatus("current")


class _SleSystemAutpReloadAtMinutes_Type(Integer32):
    """Custom type sleSystemAutpReloadAtMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SleSystemAutpReloadAtMinutes_Type.__name__ = "Integer32"
_SleSystemAutpReloadAtMinutes_Object = MibScalar
sleSystemAutpReloadAtMinutes = _SleSystemAutpReloadAtMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 92),
    _SleSystemAutpReloadAtMinutes_Type()
)
sleSystemAutpReloadAtMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAutpReloadAtMinutes.setStatus("current")
_SleSystemAdministeredMac_Type = OctetString
_SleSystemAdministeredMac_Object = MibScalar
sleSystemAdministeredMac = _SleSystemAdministeredMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 93),
    _SleSystemAdministeredMac_Type()
)
sleSystemAdministeredMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemAdministeredMac.setStatus("current")
_SleSystemBaseMac_Type = OctetString
_SleSystemBaseMac_Object = MibScalar
sleSystemBaseMac = _SleSystemBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 94),
    _SleSystemBaseMac_Type()
)
sleSystemBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemBaseMac.setStatus("current")
_SleSystemSyslogBindAddrType_Type = InetAddressType
_SleSystemSyslogBindAddrType_Object = MibScalar
sleSystemSyslogBindAddrType = _SleSystemSyslogBindAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 95),
    _SleSystemSyslogBindAddrType_Type()
)
sleSystemSyslogBindAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemSyslogBindAddrType.setStatus("current")
_SleSystemSyslogBindIPAddress_Type = InetAddress
_SleSystemSyslogBindIPAddress_Object = MibScalar
sleSystemSyslogBindIPAddress = _SleSystemSyslogBindIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 96),
    _SleSystemSyslogBindIPAddress_Type()
)
sleSystemSyslogBindIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemSyslogBindIPAddress.setStatus("current")
_SleSystemNtpBindAddrType_Type = InetAddressType
_SleSystemNtpBindAddrType_Object = MibScalar
sleSystemNtpBindAddrType = _SleSystemNtpBindAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 97),
    _SleSystemNtpBindAddrType_Type()
)
sleSystemNtpBindAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemNtpBindAddrType.setStatus("current")
_SleSystemNtpBindIPAddress_Type = InetAddress
_SleSystemNtpBindIPAddress_Object = MibScalar
sleSystemNtpBindIPAddress = _SleSystemNtpBindIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 98),
    _SleSystemNtpBindIPAddress_Type()
)
sleSystemNtpBindIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemNtpBindIPAddress.setStatus("current")
_SleSystemPLDversion_Type = OctetString
_SleSystemPLDversion_Object = MibScalar
sleSystemPLDversion = _SleSystemPLDversion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 99),
    _SleSystemPLDversion_Type()
)
sleSystemPLDversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemPLDversion.setStatus("current")
_SleSysetmGlobalTimeoutMin_Type = Integer32
_SleSysetmGlobalTimeoutMin_Object = MibScalar
sleSysetmGlobalTimeoutMin = _SleSysetmGlobalTimeoutMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 100),
    _SleSysetmGlobalTimeoutMin_Type()
)
sleSysetmGlobalTimeoutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSysetmGlobalTimeoutMin.setStatus("current")
_SleSysetmGlobalTimeoutSec_Type = Integer32
_SleSysetmGlobalTimeoutSec_Object = MibScalar
sleSysetmGlobalTimeoutSec = _SleSysetmGlobalTimeoutSec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 101),
    _SleSysetmGlobalTimeoutSec_Type()
)
sleSysetmGlobalTimeoutSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSysetmGlobalTimeoutSec.setStatus("current")


class _SleSystemCPULoad5s_Type(Integer32):
    """Custom type sleSystemCPULoad5s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleSystemCPULoad5s_Type.__name__ = "Integer32"
_SleSystemCPULoad5s_Object = MibScalar
sleSystemCPULoad5s = _SleSystemCPULoad5s_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 102),
    _SleSystemCPULoad5s_Type()
)
sleSystemCPULoad5s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemCPULoad5s.setStatus("current")


class _SleSystemCPULoad1m_Type(Integer32):
    """Custom type sleSystemCPULoad1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleSystemCPULoad1m_Type.__name__ = "Integer32"
_SleSystemCPULoad1m_Object = MibScalar
sleSystemCPULoad1m = _SleSystemCPULoad1m_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 103),
    _SleSystemCPULoad1m_Type()
)
sleSystemCPULoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemCPULoad1m.setStatus("current")


class _SleSystemCPULoad10m_Type(Integer32):
    """Custom type sleSystemCPULoad10m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleSystemCPULoad10m_Type.__name__ = "Integer32"
_SleSystemCPULoad10m_Object = MibScalar
sleSystemCPULoad10m = _SleSystemCPULoad10m_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 1, 104),
    _SleSystemCPULoad10m_Type()
)
sleSystemCPULoad10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemCPULoad10m.setStatus("current")
_SleSystemBaseControl_ObjectIdentity = ObjectIdentity
sleSystemBaseControl = _SleSystemBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2)
)


class _SleSystemControlRequest_Type(Integer32):
    """Custom type sleSystemControlRequest based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("setSystemBaseSystemInfoProfile", 1),
          ("setSystemBaseCPUThresholdProfile", 2),
          ("sleSystemBaseDefaultOS", 3),
          ("setSystemBaseRTCProfile", 4),
          ("setSystemBaseDNSDomainName", 5),
          ("setSystemBaseBannerProfile", 6),
          ("setSystemBaseSyslogProfile", 7),
          ("setSystemBaseSSHState", 8),
          ("setSystemBaseNTPState", 9),
          ("setSystemBaseOSUpgradeProfile", 10),
          ("setSystemBaseBackup", 11),
          ("setSystemBaseBackupInterval", 12),
          ("setSystemBaseReload", 13),
          ("setSystemDhcpActivity", 14),
          ("setSystemBasePonFwDownloadProfile", 15),
          ("setSystemDefaultTTL", 16),
          ("setSystemBaseSyslogBindIfName", 17),
          ("clearSystemBaseSyslogBindIfName", 18),
          ("setSystemConfigPortMove", 19),
          ("setSystemConfigPortCopy", 20),
          ("setSystemConfigPortClear", 21),
          ("setSystemControlSessionTime", 22),
          ("setSystemControlExecTimeout", 23),
          ("setSystemWatchdogStatus", 24),
          ("clearSystemOs", 25),
          ("setNtpBindInterface", 26),
          ("setFtpBindInterface", 27),
          ("setSystemBaseRedundancyPort", 28),
          ("clearRedundancy", 29),
          ("setSystemBaseTempThreshold", 30),
          ("setSystemBaseMemThreshold", 31),
          ("setSystemBaseReloadBoth", 32),
          ("setSystemBaseBootloaderUpgradeProfile", 33),
          ("setNtpBindAddress", 34),
          ("setEnablePasswd", 35),
          ("setEnableSerivceEncryption", 36),
          ("restoreSystemPasswd", 37),
          ("setNtpPollInterval", 38),
          ("setRestoreFactory", 39),
          ("setWebMgmtStatus", 40),
          ("setSystemBaseAutoReloadInTime", 41),
          ("setSystemBaseAutoReloadDailyTime", 42),
          ("setSystemBaseAutoReloadAtTime", 43),
          ("setSystemAdministeredMac", 44),
          ("setSystemSyslogProfileEx", 45),
          ("setNtpBindAddressEx", 46),
          ("setRetryWriteMemory", 47),
          ("setGlobalTimeout", 48))
    )


_SleSystemControlRequest_Type.__name__ = "Integer32"
_SleSystemControlRequest_Object = MibScalar
sleSystemControlRequest = _SleSystemControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 1),
    _SleSystemControlRequest_Type()
)
sleSystemControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlRequest.setStatus("current")
_SleSystemControlStatus_Type = SleControlStatusType
_SleSystemControlStatus_Object = MibScalar
sleSystemControlStatus = _SleSystemControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 2),
    _SleSystemControlStatus_Type()
)
sleSystemControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemControlStatus.setStatus("current")
_SleSystemControlTimer_Type = Gauge32
_SleSystemControlTimer_Object = MibScalar
sleSystemControlTimer = _SleSystemControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 3),
    _SleSystemControlTimer_Type()
)
sleSystemControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlTimer.setStatus("current")
_SleSystemControlTimeStamp_Type = TimeTicks
_SleSystemControlTimeStamp_Object = MibScalar
sleSystemControlTimeStamp = _SleSystemControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 4),
    _SleSystemControlTimeStamp_Type()
)
sleSystemControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemControlTimeStamp.setStatus("current")
_SleSystemControlReqResult_Type = SleControlRequestResultType
_SleSystemControlReqResult_Object = MibScalar
sleSystemControlReqResult = _SleSystemControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 5),
    _SleSystemControlReqResult_Type()
)
sleSystemControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemControlReqResult.setStatus("current")
_SleSystemControlHostName_Type = OctetString
_SleSystemControlHostName_Object = MibScalar
sleSystemControlHostName = _SleSystemControlHostName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 6),
    _SleSystemControlHostName_Type()
)
sleSystemControlHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlHostName.setStatus("current")


class _SleSystemControlCPUThreshold_Type(Integer32):
    """Custom type sleSystemControlCPUThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SleSystemControlCPUThreshold_Type.__name__ = "Integer32"
_SleSystemControlCPUThreshold_Object = MibScalar
sleSystemControlCPUThreshold = _SleSystemControlCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 7),
    _SleSystemControlCPUThreshold_Type()
)
sleSystemControlCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlCPUThreshold.setStatus("current")


class _SleSystemControlCPUInterval_Type(Integer32):
    """Custom type sleSystemControlCPUInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(600, 600),
    )


_SleSystemControlCPUInterval_Type.__name__ = "Integer32"
_SleSystemControlCPUInterval_Object = MibScalar
sleSystemControlCPUInterval = _SleSystemControlCPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 8),
    _SleSystemControlCPUInterval_Type()
)
sleSystemControlCPUInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlCPUInterval.setStatus("current")


class _SleSystemControlDefaultOS_Type(Integer32):
    """Custom type sleSystemControlDefaultOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("os1", 1),
          ("os2", 2))
    )


_SleSystemControlDefaultOS_Type.__name__ = "Integer32"
_SleSystemControlDefaultOS_Object = MibScalar
sleSystemControlDefaultOS = _SleSystemControlDefaultOS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 9),
    _SleSystemControlDefaultOS_Type()
)
sleSystemControlDefaultOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlDefaultOS.setStatus("current")
_SleSystemControlClock_Type = OctetString
_SleSystemControlClock_Object = MibScalar
sleSystemControlClock = _SleSystemControlClock_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 10),
    _SleSystemControlClock_Type()
)
sleSystemControlClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlClock.setStatus("current")
_SleSystemControlTimezone_Type = OctetString
_SleSystemControlTimezone_Object = MibScalar
sleSystemControlTimezone = _SleSystemControlTimezone_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 11),
    _SleSystemControlTimezone_Type()
)
sleSystemControlTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlTimezone.setStatus("current")
_SleSystemControlDNSDomainName_Type = OctetString
_SleSystemControlDNSDomainName_Object = MibScalar
sleSystemControlDNSDomainName = _SleSystemControlDNSDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 12),
    _SleSystemControlDNSDomainName_Type()
)
sleSystemControlDNSDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlDNSDomainName.setStatus("current")
_SleSystemControlInitBanner_Type = OctetString
_SleSystemControlInitBanner_Object = MibScalar
sleSystemControlInitBanner = _SleSystemControlInitBanner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 13),
    _SleSystemControlInitBanner_Type()
)
sleSystemControlInitBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlInitBanner.setStatus("current")
_SleSystemControlSuccessBanner_Type = OctetString
_SleSystemControlSuccessBanner_Object = MibScalar
sleSystemControlSuccessBanner = _SleSystemControlSuccessBanner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 14),
    _SleSystemControlSuccessBanner_Type()
)
sleSystemControlSuccessBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSuccessBanner.setStatus("current")
_SleSystemControlFailBanner_Type = OctetString
_SleSystemControlFailBanner_Object = MibScalar
sleSystemControlFailBanner = _SleSystemControlFailBanner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 15),
    _SleSystemControlFailBanner_Type()
)
sleSystemControlFailBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlFailBanner.setStatus("current")


class _SleSystemControlSyslogState_Type(Integer32):
    """Custom type sleSystemControlSyslogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", -2),
          ("stop", 0),
          ("start", 1))
    )


_SleSystemControlSyslogState_Type.__name__ = "Integer32"
_SleSystemControlSyslogState_Object = MibScalar
sleSystemControlSyslogState = _SleSystemControlSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 16),
    _SleSystemControlSyslogState_Type()
)
sleSystemControlSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogState.setStatus("current")


class _SleSystemControlSyslogVolatileNumber_Type(Integer32):
    """Custom type sleSystemControlSyslogVolatileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", -2),
          ("clearLocalVolatileHistory", 0))
    )


_SleSystemControlSyslogVolatileNumber_Type.__name__ = "Integer32"
_SleSystemControlSyslogVolatileNumber_Object = MibScalar
sleSystemControlSyslogVolatileNumber = _SleSystemControlSyslogVolatileNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 17),
    _SleSystemControlSyslogVolatileNumber_Type()
)
sleSystemControlSyslogVolatileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogVolatileNumber.setStatus("current")


class _SleSystemControlSyslogNonVolatileNumber_Type(Integer32):
    """Custom type sleSystemControlSyslogNonVolatileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", -2),
          ("clearLocalNonVolatileHistory", 0))
    )


_SleSystemControlSyslogNonVolatileNumber_Type.__name__ = "Integer32"
_SleSystemControlSyslogNonVolatileNumber_Object = MibScalar
sleSystemControlSyslogNonVolatileNumber = _SleSystemControlSyslogNonVolatileNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 18),
    _SleSystemControlSyslogNonVolatileNumber_Type()
)
sleSystemControlSyslogNonVolatileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogNonVolatileNumber.setStatus("current")
_SleSystemControlSyslogBindAddress_Type = IpAddress
_SleSystemControlSyslogBindAddress_Object = MibScalar
sleSystemControlSyslogBindAddress = _SleSystemControlSyslogBindAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 19),
    _SleSystemControlSyslogBindAddress_Type()
)
sleSystemControlSyslogBindAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogBindAddress.setStatus("current")


class _SleSystemControlSyslogLocalCode_Type(Integer32):
    """Custom type sleSystemControlSyslogLocalCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SleSystemControlSyslogLocalCode_Type.__name__ = "Integer32"
_SleSystemControlSyslogLocalCode_Object = MibScalar
sleSystemControlSyslogLocalCode = _SleSystemControlSyslogLocalCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 20),
    _SleSystemControlSyslogLocalCode_Type()
)
sleSystemControlSyslogLocalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogLocalCode.setStatus("current")


class _SleSystemControlSSHState_Type(Integer32):
    """Custom type sleSystemControlSSHState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSystemControlSSHState_Type.__name__ = "Integer32"
_SleSystemControlSSHState_Object = MibScalar
sleSystemControlSSHState = _SleSystemControlSSHState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 21),
    _SleSystemControlSSHState_Type()
)
sleSystemControlSSHState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSSHState.setStatus("current")


class _SleSystemControlNTPState_Type(Integer32):
    """Custom type sleSystemControlNTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("ntp", 1),
          ("sntp", 2))
    )


_SleSystemControlNTPState_Type.__name__ = "Integer32"
_SleSystemControlNTPState_Object = MibScalar
sleSystemControlNTPState = _SleSystemControlNTPState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 22),
    _SleSystemControlNTPState_Type()
)
sleSystemControlNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlNTPState.setStatus("current")


class _SleSystemControlOSUpgradeNumber_Type(Integer32):
    """Custom type sleSystemControlOSUpgradeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("os1", 1),
          ("os2", 2))
    )


_SleSystemControlOSUpgradeNumber_Type.__name__ = "Integer32"
_SleSystemControlOSUpgradeNumber_Object = MibScalar
sleSystemControlOSUpgradeNumber = _SleSystemControlOSUpgradeNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 23),
    _SleSystemControlOSUpgradeNumber_Type()
)
sleSystemControlOSUpgradeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlOSUpgradeNumber.setStatus("current")
_SleSystemControlServerAddress_Type = IpAddress
_SleSystemControlServerAddress_Object = MibScalar
sleSystemControlServerAddress = _SleSystemControlServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 24),
    _SleSystemControlServerAddress_Type()
)
sleSystemControlServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlServerAddress.setStatus("current")


class _SleSystemControlUpDownFlag_Type(Integer32):
    """Custom type sleSystemControlUpDownFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("upload", 0),
          ("download", 1))
    )


_SleSystemControlUpDownFlag_Type.__name__ = "Integer32"
_SleSystemControlUpDownFlag_Object = MibScalar
sleSystemControlUpDownFlag = _SleSystemControlUpDownFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 25),
    _SleSystemControlUpDownFlag_Type()
)
sleSystemControlUpDownFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlUpDownFlag.setStatus("current")
_SleSystemControlUserID_Type = OctetString
_SleSystemControlUserID_Object = MibScalar
sleSystemControlUserID = _SleSystemControlUserID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 26),
    _SleSystemControlUserID_Type()
)
sleSystemControlUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlUserID.setStatus("current")
_SleSystemControlPassword_Type = OctetString
_SleSystemControlPassword_Object = MibScalar
sleSystemControlPassword = _SleSystemControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 27),
    _SleSystemControlPassword_Type()
)
sleSystemControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlPassword.setStatus("current")
_SleSystemControlFileName_Type = OctetString
_SleSystemControlFileName_Object = MibScalar
sleSystemControlFileName = _SleSystemControlFileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 28),
    _SleSystemControlFileName_Type()
)
sleSystemControlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlFileName.setStatus("current")


class _SleSystemControlBackupFlag_Type(Integer32):
    """Custom type sleSystemControlBackupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("writeMemory", 1),
          ("restoreFactoryDefault", 2),
          ("restoreL2Default", 3))
    )


_SleSystemControlBackupFlag_Type.__name__ = "Integer32"
_SleSystemControlBackupFlag_Object = MibScalar
sleSystemControlBackupFlag = _SleSystemControlBackupFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 29),
    _SleSystemControlBackupFlag_Type()
)
sleSystemControlBackupFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlBackupFlag.setStatus("current")


class _SleSystemControlReloadOS_Type(Integer32):
    """Custom type sleSystemControlReloadOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("os1", 1),
          ("os2", 2))
    )


_SleSystemControlReloadOS_Type.__name__ = "Integer32"
_SleSystemControlReloadOS_Object = MibScalar
sleSystemControlReloadOS = _SleSystemControlReloadOS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 30),
    _SleSystemControlReloadOS_Type()
)
sleSystemControlReloadOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlReloadOS.setStatus("current")
_SleSystemControlBackupInterval_Type = Integer32
_SleSystemControlBackupInterval_Object = MibScalar
sleSystemControlBackupInterval = _SleSystemControlBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 31),
    _SleSystemControlBackupInterval_Type()
)
sleSystemControlBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlBackupInterval.setStatus("current")


class _SleSystemControlDhcpActivity_Type(Integer32):
    """Custom type sleSystemControlDhcpActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSystemControlDhcpActivity_Type.__name__ = "Integer32"
_SleSystemControlDhcpActivity_Object = MibScalar
sleSystemControlDhcpActivity = _SleSystemControlDhcpActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 32),
    _SleSystemControlDhcpActivity_Type()
)
sleSystemControlDhcpActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlDhcpActivity.setStatus("current")


class _SleSystemControlDefaultTTL_Type(Integer32):
    """Custom type sleSystemControlDefaultTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 255),
    )


_SleSystemControlDefaultTTL_Type.__name__ = "Integer32"
_SleSystemControlDefaultTTL_Object = MibScalar
sleSystemControlDefaultTTL = _SleSystemControlDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 33),
    _SleSystemControlDefaultTTL_Type()
)
sleSystemControlDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlDefaultTTL.setStatus("current")


class _SleSystemControlSyslogVolatileSize_Type(Integer32):
    """Custom type sleSystemControlSyslogVolatileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SleSystemControlSyslogVolatileSize_Type.__name__ = "Integer32"
_SleSystemControlSyslogVolatileSize_Object = MibScalar
sleSystemControlSyslogVolatileSize = _SleSystemControlSyslogVolatileSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 34),
    _SleSystemControlSyslogVolatileSize_Type()
)
sleSystemControlSyslogVolatileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogVolatileSize.setStatus("current")
_SleSystemControlSyslogBindInterfaceName_Type = OctetString
_SleSystemControlSyslogBindInterfaceName_Object = MibScalar
sleSystemControlSyslogBindInterfaceName = _SleSystemControlSyslogBindInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 35),
    _SleSystemControlSyslogBindInterfaceName_Type()
)
sleSystemControlSyslogBindInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogBindInterfaceName.setStatus("current")


class _SleSystemControlSrcPort_Type(Integer32):
    """Custom type sleSystemControlSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleSystemControlSrcPort_Type.__name__ = "Integer32"
_SleSystemControlSrcPort_Object = MibScalar
sleSystemControlSrcPort = _SleSystemControlSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 36),
    _SleSystemControlSrcPort_Type()
)
sleSystemControlSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSrcPort.setStatus("current")


class _SleSystemControlDstPort_Type(Integer32):
    """Custom type sleSystemControlDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleSystemControlDstPort_Type.__name__ = "Integer32"
_SleSystemControlDstPort_Object = MibScalar
sleSystemControlDstPort = _SleSystemControlDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 37),
    _SleSystemControlDstPort_Type()
)
sleSystemControlDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlDstPort.setStatus("current")


class _SleSystemControlSessionTime_Type(Integer32):
    """Custom type sleSystemControlSessionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_SleSystemControlSessionTime_Type.__name__ = "Integer32"
_SleSystemControlSessionTime_Object = MibScalar
sleSystemControlSessionTime = _SleSystemControlSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 38),
    _SleSystemControlSessionTime_Type()
)
sleSystemControlSessionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSessionTime.setStatus("current")


class _SleSystemControlExecTimeout_Type(Integer32):
    """Custom type sleSystemControlExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147519),
    )


_SleSystemControlExecTimeout_Type.__name__ = "Integer32"
_SleSystemControlExecTimeout_Object = MibScalar
sleSystemControlExecTimeout = _SleSystemControlExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 39),
    _SleSystemControlExecTimeout_Type()
)
sleSystemControlExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlExecTimeout.setStatus("current")


class _SleSystemControlWatchdogStatus_Type(Integer32):
    """Custom type sleSystemControlWatchdogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSystemControlWatchdogStatus_Type.__name__ = "Integer32"
_SleSystemControlWatchdogStatus_Object = MibScalar
sleSystemControlWatchdogStatus = _SleSystemControlWatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 40),
    _SleSystemControlWatchdogStatus_Type()
)
sleSystemControlWatchdogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlWatchdogStatus.setStatus("current")
_SleSystemControlClearOs_Type = Integer32
_SleSystemControlClearOs_Object = MibScalar
sleSystemControlClearOs = _SleSystemControlClearOs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 41),
    _SleSystemControlClearOs_Type()
)
sleSystemControlClearOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlClearOs.setStatus("current")
_SleSystemControlNtpBindInterface_Type = OctetString
_SleSystemControlNtpBindInterface_Object = MibScalar
sleSystemControlNtpBindInterface = _SleSystemControlNtpBindInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 42),
    _SleSystemControlNtpBindInterface_Type()
)
sleSystemControlNtpBindInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlNtpBindInterface.setStatus("current")
_SleSystemControlFtpBindInterface_Type = OctetString
_SleSystemControlFtpBindInterface_Object = MibScalar
sleSystemControlFtpBindInterface = _SleSystemControlFtpBindInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 43),
    _SleSystemControlFtpBindInterface_Type()
)
sleSystemControlFtpBindInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlFtpBindInterface.setStatus("current")


class _SleSystemControlSyslogVolMaxLine_Type(Integer32):
    """Custom type sleSystemControlSyslogVolMaxLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 16384),
    )


_SleSystemControlSyslogVolMaxLine_Type.__name__ = "Integer32"
_SleSystemControlSyslogVolMaxLine_Object = MibScalar
sleSystemControlSyslogVolMaxLine = _SleSystemControlSyslogVolMaxLine_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 44),
    _SleSystemControlSyslogVolMaxLine_Type()
)
sleSystemControlSyslogVolMaxLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogVolMaxLine.setStatus("current")
_SleSystemControlTempHighThreshold_Type = Integer32
_SleSystemControlTempHighThreshold_Object = MibScalar
sleSystemControlTempHighThreshold = _SleSystemControlTempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 45),
    _SleSystemControlTempHighThreshold_Type()
)
sleSystemControlTempHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlTempHighThreshold.setStatus("current")
_SleSystemControlTempLowThreshold_Type = Integer32
_SleSystemControlTempLowThreshold_Object = MibScalar
sleSystemControlTempLowThreshold = _SleSystemControlTempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 46),
    _SleSystemControlTempLowThreshold_Type()
)
sleSystemControlTempLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlTempLowThreshold.setStatus("current")


class _SleSystemControlMemThreshold_Type(Integer32):
    """Custom type sleSystemControlMemThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SleSystemControlMemThreshold_Type.__name__ = "Integer32"
_SleSystemControlMemThreshold_Object = MibScalar
sleSystemControlMemThreshold = _SleSystemControlMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 47),
    _SleSystemControlMemThreshold_Type()
)
sleSystemControlMemThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlMemThreshold.setStatus("current")


class _SleSystemControlLowCPUThreshold_Type(Integer32):
    """Custom type sleSystemControlLowCPUThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SleSystemControlLowCPUThreshold_Type.__name__ = "Integer32"
_SleSystemControlLowCPUThreshold_Object = MibScalar
sleSystemControlLowCPUThreshold = _SleSystemControlLowCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 48),
    _SleSystemControlLowCPUThreshold_Type()
)
sleSystemControlLowCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlLowCPUThreshold.setStatus("current")


class _SleSystemControlLowCPUInterval_Type(Integer32):
    """Custom type sleSystemControlLowCPUInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(600, 600),
    )


_SleSystemControlLowCPUInterval_Type.__name__ = "Integer32"
_SleSystemControlLowCPUInterval_Object = MibScalar
sleSystemControlLowCPUInterval = _SleSystemControlLowCPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 49),
    _SleSystemControlLowCPUInterval_Type()
)
sleSystemControlLowCPUInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlLowCPUInterval.setStatus("current")
_SleSystemControlNtpBindAddress_Type = IpAddress
_SleSystemControlNtpBindAddress_Object = MibScalar
sleSystemControlNtpBindAddress = _SleSystemControlNtpBindAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 50),
    _SleSystemControlNtpBindAddress_Type()
)
sleSystemControlNtpBindAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlNtpBindAddress.setStatus("current")


class _SleSystemControlEnablePasswdType_Type(Integer32):
    """Custom type sleSystemControlEnablePasswdType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plain", 1),
          ("encrypt", 2))
    )


_SleSystemControlEnablePasswdType_Type.__name__ = "Integer32"
_SleSystemControlEnablePasswdType_Object = MibScalar
sleSystemControlEnablePasswdType = _SleSystemControlEnablePasswdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 51),
    _SleSystemControlEnablePasswdType_Type()
)
sleSystemControlEnablePasswdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlEnablePasswdType.setStatus("current")


class _SleSystemControlEnablePasswd_Type(OctetString):
    """Custom type sleSystemControlEnablePasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SleSystemControlEnablePasswd_Type.__name__ = "OctetString"
_SleSystemControlEnablePasswd_Object = MibScalar
sleSystemControlEnablePasswd = _SleSystemControlEnablePasswd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 52),
    _SleSystemControlEnablePasswd_Type()
)
sleSystemControlEnablePasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlEnablePasswd.setStatus("current")


class _SleSystemControlServicePasswdEncryption_Type(Integer32):
    """Custom type sleSystemControlServicePasswdEncryption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSystemControlServicePasswdEncryption_Type.__name__ = "Integer32"
_SleSystemControlServicePasswdEncryption_Object = MibScalar
sleSystemControlServicePasswdEncryption = _SleSystemControlServicePasswdEncryption_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 53),
    _SleSystemControlServicePasswdEncryption_Type()
)
sleSystemControlServicePasswdEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlServicePasswdEncryption.setStatus("current")


class _SleSystemControlNtpPollInterval_Type(Integer32):
    """Custom type sleSystemControlNtpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 20),
    )


_SleSystemControlNtpPollInterval_Type.__name__ = "Integer32"
_SleSystemControlNtpPollInterval_Object = MibScalar
sleSystemControlNtpPollInterval = _SleSystemControlNtpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 54),
    _SleSystemControlNtpPollInterval_Type()
)
sleSystemControlNtpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlNtpPollInterval.setStatus("current")


class _SleSystemControlCPUDuration_Type(Integer32):
    """Custom type sleSystemControlCPUDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_SleSystemControlCPUDuration_Type.__name__ = "Integer32"
_SleSystemControlCPUDuration_Object = MibScalar
sleSystemControlCPUDuration = _SleSystemControlCPUDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 55),
    _SleSystemControlCPUDuration_Type()
)
sleSystemControlCPUDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlCPUDuration.setStatus("current")


class _SleSystemControlLowCPUDuration_Type(Integer32):
    """Custom type sleSystemControlLowCPUDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_SleSystemControlLowCPUDuration_Type.__name__ = "Integer32"
_SleSystemControlLowCPUDuration_Object = MibScalar
sleSystemControlLowCPUDuration = _SleSystemControlLowCPUDuration_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 56),
    _SleSystemControlLowCPUDuration_Type()
)
sleSystemControlLowCPUDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlLowCPUDuration.setStatus("current")


class _SleSystemControlWebMgmt_Type(Integer32):
    """Custom type sleSystemControlWebMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleSystemControlWebMgmt_Type.__name__ = "Integer32"
_SleSystemControlWebMgmt_Object = MibScalar
sleSystemControlWebMgmt = _SleSystemControlWebMgmt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 57),
    _SleSystemControlWebMgmt_Type()
)
sleSystemControlWebMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemControlWebMgmt.setStatus("current")


class _SleSystemControlAutoReloadYear_Type(Integer32):
    """Custom type sleSystemControlAutoReloadYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2008, 2035),
    )


_SleSystemControlAutoReloadYear_Type.__name__ = "Integer32"
_SleSystemControlAutoReloadYear_Object = MibScalar
sleSystemControlAutoReloadYear = _SleSystemControlAutoReloadYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 58),
    _SleSystemControlAutoReloadYear_Type()
)
sleSystemControlAutoReloadYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlAutoReloadYear.setStatus("current")


class _SleSystemControlAutoReloadMonth_Type(Integer32):
    """Custom type sleSystemControlAutoReloadMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_SleSystemControlAutoReloadMonth_Type.__name__ = "Integer32"
_SleSystemControlAutoReloadMonth_Object = MibScalar
sleSystemControlAutoReloadMonth = _SleSystemControlAutoReloadMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 59),
    _SleSystemControlAutoReloadMonth_Type()
)
sleSystemControlAutoReloadMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlAutoReloadMonth.setStatus("current")


class _SleSystemControlAutoReloadDay_Type(Integer32):
    """Custom type sleSystemControlAutoReloadDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SleSystemControlAutoReloadDay_Type.__name__ = "Integer32"
_SleSystemControlAutoReloadDay_Object = MibScalar
sleSystemControlAutoReloadDay = _SleSystemControlAutoReloadDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 60),
    _SleSystemControlAutoReloadDay_Type()
)
sleSystemControlAutoReloadDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlAutoReloadDay.setStatus("current")


class _SleSystemControlAutoReloadHour_Type(Integer32):
    """Custom type sleSystemControlAutoReloadHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SleSystemControlAutoReloadHour_Type.__name__ = "Integer32"
_SleSystemControlAutoReloadHour_Object = MibScalar
sleSystemControlAutoReloadHour = _SleSystemControlAutoReloadHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 61),
    _SleSystemControlAutoReloadHour_Type()
)
sleSystemControlAutoReloadHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlAutoReloadHour.setStatus("current")


class _SleSystemControlAutoReloadMinutes_Type(Integer32):
    """Custom type sleSystemControlAutoReloadMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SleSystemControlAutoReloadMinutes_Type.__name__ = "Integer32"
_SleSystemControlAutoReloadMinutes_Object = MibScalar
sleSystemControlAutoReloadMinutes = _SleSystemControlAutoReloadMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 62),
    _SleSystemControlAutoReloadMinutes_Type()
)
sleSystemControlAutoReloadMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlAutoReloadMinutes.setStatus("current")
_SleSystemControlAdministeredMac_Type = OctetString
_SleSystemControlAdministeredMac_Object = MibScalar
sleSystemControlAdministeredMac = _SleSystemControlAdministeredMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 63),
    _SleSystemControlAdministeredMac_Type()
)
sleSystemControlAdministeredMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlAdministeredMac.setStatus("current")
_SleSystemControlSyslogBindAddrType_Type = InetAddressType
_SleSystemControlSyslogBindAddrType_Object = MibScalar
sleSystemControlSyslogBindAddrType = _SleSystemControlSyslogBindAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 64),
    _SleSystemControlSyslogBindAddrType_Type()
)
sleSystemControlSyslogBindAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogBindAddrType.setStatus("current")
_SleSystemControlSyslogBindIPAddress_Type = InetAddress
_SleSystemControlSyslogBindIPAddress_Object = MibScalar
sleSystemControlSyslogBindIPAddress = _SleSystemControlSyslogBindIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 65),
    _SleSystemControlSyslogBindIPAddress_Type()
)
sleSystemControlSyslogBindIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlSyslogBindIPAddress.setStatus("current")
_SleSystemControlNtpBindAddrType_Type = InetAddressType
_SleSystemControlNtpBindAddrType_Object = MibScalar
sleSystemControlNtpBindAddrType = _SleSystemControlNtpBindAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 66),
    _SleSystemControlNtpBindAddrType_Type()
)
sleSystemControlNtpBindAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlNtpBindAddrType.setStatus("current")
_SleSystemControlNtpBindIPAddress_Type = InetAddress
_SleSystemControlNtpBindIPAddress_Object = MibScalar
sleSystemControlNtpBindIPAddress = _SleSystemControlNtpBindIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 67),
    _SleSystemControlNtpBindIPAddress_Type()
)
sleSystemControlNtpBindIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlNtpBindIPAddress.setStatus("current")


class _SleSystemControlWriteMemRetryCount_Type(Integer32):
    """Custom type sleSystemControlWriteMemRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 10),
    )


_SleSystemControlWriteMemRetryCount_Type.__name__ = "Integer32"
_SleSystemControlWriteMemRetryCount_Object = MibScalar
sleSystemControlWriteMemRetryCount = _SleSystemControlWriteMemRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 68),
    _SleSystemControlWriteMemRetryCount_Type()
)
sleSystemControlWriteMemRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlWriteMemRetryCount.setStatus("current")


class _SleSystemControlWriteMemRetryInterval_Type(Integer32):
    """Custom type sleSystemControlWriteMemRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 180),
    )


_SleSystemControlWriteMemRetryInterval_Type.__name__ = "Integer32"
_SleSystemControlWriteMemRetryInterval_Object = MibScalar
sleSystemControlWriteMemRetryInterval = _SleSystemControlWriteMemRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 69),
    _SleSystemControlWriteMemRetryInterval_Type()
)
sleSystemControlWriteMemRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlWriteMemRetryInterval.setStatus("current")


class _SleSystemControlGlobalTimeoutMin_Type(Integer32):
    """Custom type sleSystemControlGlobalTimeoutMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 180),
    )


_SleSystemControlGlobalTimeoutMin_Type.__name__ = "Integer32"
_SleSystemControlGlobalTimeoutMin_Object = MibScalar
sleSystemControlGlobalTimeoutMin = _SleSystemControlGlobalTimeoutMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 70),
    _SleSystemControlGlobalTimeoutMin_Type()
)
sleSystemControlGlobalTimeoutMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlGlobalTimeoutMin.setStatus("current")


class _SleSystemControlGlobalTimeoutSec_Type(Integer32):
    """Custom type sleSystemControlGlobalTimeoutSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 180),
    )


_SleSystemControlGlobalTimeoutSec_Type.__name__ = "Integer32"
_SleSystemControlGlobalTimeoutSec_Object = MibScalar
sleSystemControlGlobalTimeoutSec = _SleSystemControlGlobalTimeoutSec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 2, 71),
    _SleSystemControlGlobalTimeoutSec_Type()
)
sleSystemControlGlobalTimeoutSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemControlGlobalTimeoutSec.setStatus("current")
_SleSystemBaseNotification_ObjectIdentity = ObjectIdentity
sleSystemBaseNotification = _SleSystemBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3)
)
_SleSystemBaseSlotInfo_ObjectIdentity = ObjectIdentity
sleSystemBaseSlotInfo = _SleSystemBaseSlotInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4)
)
_SleSystemBaseSlotInfoTable_Object = MibTable
sleSystemBaseSlotInfoTable = _SleSystemBaseSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sleSystemBaseSlotInfoTable.setStatus("current")
_SleSystemBaseSlotInfoEntry_Object = MibTableRow
sleSystemBaseSlotInfoEntry = _SleSystemBaseSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1)
)
sleSystemBaseSlotInfoEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotIndex"),
)
if mibBuilder.loadTexts:
    sleSystemBaseSlotInfoEntry.setStatus("current")


class _SleSystemSlotIndex_Type(Integer32):
    """Custom type sleSystemSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SleSystemSlotIndex_Type.__name__ = "Integer32"
_SleSystemSlotIndex_Object = MibTableColumn
sleSystemSlotIndex = _SleSystemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 1),
    _SleSystemSlotIndex_Type()
)
sleSystemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotIndex.setStatus("current")
_SleSystemSlotUptime_Type = TimeTicks
_SleSystemSlotUptime_Object = MibTableColumn
sleSystemSlotUptime = _SleSystemSlotUptime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 2),
    _SleSystemSlotUptime_Type()
)
sleSystemSlotUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotUptime.setStatus("current")
_SleSystemSlotModelName_Type = OctetString
_SleSystemSlotModelName_Object = MibTableColumn
sleSystemSlotModelName = _SleSystemSlotModelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 3),
    _SleSystemSlotModelName_Type()
)
sleSystemSlotModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotModelName.setStatus("current")
_SleSystemSlotSerialNumber_Type = OctetString
_SleSystemSlotSerialNumber_Object = MibTableColumn
sleSystemSlotSerialNumber = _SleSystemSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 4),
    _SleSystemSlotSerialNumber_Type()
)
sleSystemSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotSerialNumber.setStatus("current")
_SleSystemSlotHWVersion_Type = OctetString
_SleSystemSlotHWVersion_Object = MibTableColumn
sleSystemSlotHWVersion = _SleSystemSlotHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 5),
    _SleSystemSlotHWVersion_Type()
)
sleSystemSlotHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotHWVersion.setStatus("current")
_SleSystemSlotBLVersion_Type = OctetString
_SleSystemSlotBLVersion_Object = MibTableColumn
sleSystemSlotBLVersion = _SleSystemSlotBLVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 6),
    _SleSystemSlotBLVersion_Type()
)
sleSystemSlotBLVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotBLVersion.setStatus("current")
_SleSystemSlotSWCompatibility_Type = OctetString
_SleSystemSlotSWCompatibility_Object = MibTableColumn
sleSystemSlotSWCompatibility = _SleSystemSlotSWCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 7),
    _SleSystemSlotSWCompatibility_Type()
)
sleSystemSlotSWCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotSWCompatibility.setStatus("current")
_SleSystemSlotOSVersion_Type = OctetString
_SleSystemSlotOSVersion_Object = MibTableColumn
sleSystemSlotOSVersion = _SleSystemSlotOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 8),
    _SleSystemSlotOSVersion_Type()
)
sleSystemSlotOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotOSVersion.setStatus("current")
_SleSystemSlotMacAddress_Type = OctetString
_SleSystemSlotMacAddress_Object = MibTableColumn
sleSystemSlotMacAddress = _SleSystemSlotMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 9),
    _SleSystemSlotMacAddress_Type()
)
sleSystemSlotMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotMacAddress.setStatus("current")
_SleSystemSlotCPULoadAll_Type = OctetString
_SleSystemSlotCPULoadAll_Object = MibTableColumn
sleSystemSlotCPULoadAll = _SleSystemSlotCPULoadAll_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 10),
    _SleSystemSlotCPULoadAll_Type()
)
sleSystemSlotCPULoadAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotCPULoadAll.setStatus("current")
_SleSystemSlotCPULoadInterrupt_Type = OctetString
_SleSystemSlotCPULoadInterrupt_Object = MibTableColumn
sleSystemSlotCPULoadInterrupt = _SleSystemSlotCPULoadInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 11),
    _SleSystemSlotCPULoadInterrupt_Type()
)
sleSystemSlotCPULoadInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotCPULoadInterrupt.setStatus("current")
_SleSystemSlotMemoryTotal_Type = Unsigned32
_SleSystemSlotMemoryTotal_Object = MibTableColumn
sleSystemSlotMemoryTotal = _SleSystemSlotMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 12),
    _SleSystemSlotMemoryTotal_Type()
)
sleSystemSlotMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotMemoryTotal.setStatus("current")
_SleSystemSlotMemoryFree_Type = Unsigned32
_SleSystemSlotMemoryFree_Object = MibTableColumn
sleSystemSlotMemoryFree = _SleSystemSlotMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 13),
    _SleSystemSlotMemoryFree_Type()
)
sleSystemSlotMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotMemoryFree.setStatus("current")
_SleSystemSlotMemoryShared_Type = Unsigned32
_SleSystemSlotMemoryShared_Object = MibTableColumn
sleSystemSlotMemoryShared = _SleSystemSlotMemoryShared_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 14),
    _SleSystemSlotMemoryShared_Type()
)
sleSystemSlotMemoryShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotMemoryShared.setStatus("current")
_SleSystemSlotMemoryBuffers_Type = Unsigned32
_SleSystemSlotMemoryBuffers_Object = MibTableColumn
sleSystemSlotMemoryBuffers = _SleSystemSlotMemoryBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 15),
    _SleSystemSlotMemoryBuffers_Type()
)
sleSystemSlotMemoryBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotMemoryBuffers.setStatus("current")
_SleSystemSlotMemoryCached_Type = Unsigned32
_SleSystemSlotMemoryCached_Object = MibTableColumn
sleSystemSlotMemoryCached = _SleSystemSlotMemoryCached_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 16),
    _SleSystemSlotMemoryCached_Type()
)
sleSystemSlotMemoryCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotMemoryCached.setStatus("current")
_SleSystemSlotMemorySwapTotal_Type = Unsigned32
_SleSystemSlotMemorySwapTotal_Object = MibTableColumn
sleSystemSlotMemorySwapTotal = _SleSystemSlotMemorySwapTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 17),
    _SleSystemSlotMemorySwapTotal_Type()
)
sleSystemSlotMemorySwapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotMemorySwapTotal.setStatus("current")
_SleSystemSlotMemorySwapFree_Type = Unsigned32
_SleSystemSlotMemorySwapFree_Object = MibTableColumn
sleSystemSlotMemorySwapFree = _SleSystemSlotMemorySwapFree_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 18),
    _SleSystemSlotMemorySwapFree_Type()
)
sleSystemSlotMemorySwapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotMemorySwapFree.setStatus("current")


class _SleSystemSlotBootReason_Type(Integer32):
    """Custom type sleSystemSlotBootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              9,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("powerboot", 1),
          ("panic", 2),
          ("swreboot", 3),
          ("lowmemory", 4),
          ("watchdog", 5),
          ("swWatchdog", 9),
          ("swrebootBySfu", 11),
          ("autoreset", 12))
    )


_SleSystemSlotBootReason_Type.__name__ = "Integer32"
_SleSystemSlotBootReason_Object = MibTableColumn
sleSystemSlotBootReason = _SleSystemSlotBootReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 19),
    _SleSystemSlotBootReason_Type()
)
sleSystemSlotBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotBootReason.setStatus("current")
_SleSystemSlotBootTime_Type = Unsigned32
_SleSystemSlotBootTime_Object = MibTableColumn
sleSystemSlotBootTime = _SleSystemSlotBootTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 20),
    _SleSystemSlotBootTime_Type()
)
sleSystemSlotBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotBootTime.setStatus("current")
if mibBuilder.loadTexts:
    sleSystemSlotBootTime.setUnits("1 second")
_SleSystemSlotVoltage_Type = Unsigned32
_SleSystemSlotVoltage_Object = MibTableColumn
sleSystemSlotVoltage = _SleSystemSlotVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 4, 1, 1, 21),
    _SleSystemSlotVoltage_Type()
)
sleSystemSlotVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemSlotVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sleSystemSlotVoltage.setUnits("0.1 v")
_SleDNSServer_ObjectIdentity = ObjectIdentity
sleDNSServer = _SleDNSServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2)
)
_SleDNSServerTable_Object = MibTable
sleDNSServerTable = _SleDNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sleDNSServerTable.setStatus("current")
_SleDNSServerEntry_Object = MibTableRow
sleDNSServerEntry = _SleDNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 1, 1)
)
sleDNSServerEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerIndex"),
)
if mibBuilder.loadTexts:
    sleDNSServerEntry.setStatus("current")


class _SleDNSServerIndex_Type(Integer32):
    """Custom type sleDNSServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleDNSServerIndex_Type.__name__ = "Integer32"
_SleDNSServerIndex_Object = MibTableColumn
sleDNSServerIndex = _SleDNSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 1, 1, 1),
    _SleDNSServerIndex_Type()
)
sleDNSServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDNSServerIndex.setStatus("current")
_SleDNSServerName_Type = IpAddress
_SleDNSServerName_Object = MibTableColumn
sleDNSServerName = _SleDNSServerName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 1, 1, 2),
    _SleDNSServerName_Type()
)
sleDNSServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDNSServerName.setStatus("current")
_SleDnsServerAddrType_Type = InetAddressType
_SleDnsServerAddrType_Object = MibTableColumn
sleDnsServerAddrType = _SleDnsServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 1, 1, 3),
    _SleDnsServerAddrType_Type()
)
sleDnsServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsServerAddrType.setStatus("current")
_SleDnsServerAddress_Type = InetAddress
_SleDnsServerAddress_Object = MibTableColumn
sleDnsServerAddress = _SleDnsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 1, 1, 4),
    _SleDnsServerAddress_Type()
)
sleDnsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsServerAddress.setStatus("current")
_SleDNSServerControl_ObjectIdentity = ObjectIdentity
sleDNSServerControl = _SleDNSServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2)
)


class _SleDNSServerControlRequest_Type(Integer32):
    """Custom type sleDNSServerControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createDNSServer", 1),
          ("destroyDNSServer", 2),
          ("createDnsServerEx", 3))
    )


_SleDNSServerControlRequest_Type.__name__ = "Integer32"
_SleDNSServerControlRequest_Object = MibScalar
sleDNSServerControlRequest = _SleDNSServerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 1),
    _SleDNSServerControlRequest_Type()
)
sleDNSServerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDNSServerControlRequest.setStatus("current")
_SleDNSServerControlStatus_Type = SleControlStatusType
_SleDNSServerControlStatus_Object = MibScalar
sleDNSServerControlStatus = _SleDNSServerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 2),
    _SleDNSServerControlStatus_Type()
)
sleDNSServerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDNSServerControlStatus.setStatus("current")
_SleDNSServerControlTimer_Type = Gauge32
_SleDNSServerControlTimer_Object = MibScalar
sleDNSServerControlTimer = _SleDNSServerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 3),
    _SleDNSServerControlTimer_Type()
)
sleDNSServerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDNSServerControlTimer.setStatus("current")
_SleDNSServerControlTImeStamp_Type = TimeTicks
_SleDNSServerControlTImeStamp_Object = MibScalar
sleDNSServerControlTImeStamp = _SleDNSServerControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 4),
    _SleDNSServerControlTImeStamp_Type()
)
sleDNSServerControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDNSServerControlTImeStamp.setStatus("current")
_SleDNSServerControlReqResult_Type = SleControlRequestResultType
_SleDNSServerControlReqResult_Object = MibScalar
sleDNSServerControlReqResult = _SleDNSServerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 5),
    _SleDNSServerControlReqResult_Type()
)
sleDNSServerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDNSServerControlReqResult.setStatus("current")
_SleDNSServerControlIndex_Type = Integer32
_SleDNSServerControlIndex_Object = MibScalar
sleDNSServerControlIndex = _SleDNSServerControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 6),
    _SleDNSServerControlIndex_Type()
)
sleDNSServerControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDNSServerControlIndex.setStatus("current")
_SleDNSServerControlName_Type = IpAddress
_SleDNSServerControlName_Object = MibScalar
sleDNSServerControlName = _SleDNSServerControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 7),
    _SleDNSServerControlName_Type()
)
sleDNSServerControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDNSServerControlName.setStatus("current")
_SleDnsServerControlAddrType_Type = InetAddressType
_SleDnsServerControlAddrType_Object = MibScalar
sleDnsServerControlAddrType = _SleDnsServerControlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 8),
    _SleDnsServerControlAddrType_Type()
)
sleDnsServerControlAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsServerControlAddrType.setStatus("current")
_SleDnsServerControlAddress_Type = InetAddress
_SleDnsServerControlAddress_Object = MibScalar
sleDnsServerControlAddress = _SleDnsServerControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 2, 9),
    _SleDnsServerControlAddress_Type()
)
sleDnsServerControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsServerControlAddress.setStatus("current")
_SleDNSServerNotification_ObjectIdentity = ObjectIdentity
sleDNSServerNotification = _SleDNSServerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 3)
)
_SleLogin_ObjectIdentity = ObjectIdentity
sleLogin = _SleLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 3)
)
_SleLoginTable_Object = MibTable
sleLoginTable = _SleLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sleLoginTable.setStatus("current")
_SleLoginEntry_Object = MibTableRow
sleLoginEntry = _SleLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 3, 1, 1)
)
sleLoginEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleLoginIndex"),
)
if mibBuilder.loadTexts:
    sleLoginEntry.setStatus("current")


class _SleLoginIndex_Type(Integer32):
    """Custom type sleLoginIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_SleLoginIndex_Type.__name__ = "Integer32"
_SleLoginIndex_Object = MibTableColumn
sleLoginIndex = _SleLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 3, 1, 1, 1),
    _SleLoginIndex_Type()
)
sleLoginIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLoginIndex.setStatus("current")
_SleLoginUser_Type = OctetString
_SleLoginUser_Object = MibTableColumn
sleLoginUser = _SleLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 3, 1, 1, 2),
    _SleLoginUser_Type()
)
sleLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLoginUser.setStatus("current")
_SleLoginTTY_Type = OctetString
_SleLoginTTY_Object = MibTableColumn
sleLoginTTY = _SleLoginTTY_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 3, 1, 1, 3),
    _SleLoginTTY_Type()
)
sleLoginTTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLoginTTY.setStatus("current")
_SleLoginRemote_Type = OctetString
_SleLoginRemote_Object = MibTableColumn
sleLoginRemote = _SleLoginRemote_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 3, 1, 1, 4),
    _SleLoginRemote_Type()
)
sleLoginRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLoginRemote.setStatus("current")
_SleLoginTime_Type = OctetString
_SleLoginTime_Object = MibTableColumn
sleLoginTime = _SleLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 3, 1, 1, 5),
    _SleLoginTime_Type()
)
sleLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLoginTime.setStatus("current")
_SleBackup_ObjectIdentity = ObjectIdentity
sleBackup = _SleBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4)
)
_SleBackupTable_Object = MibTable
sleBackupTable = _SleBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sleBackupTable.setStatus("current")
_SleBackupEntry_Object = MibTableRow
sleBackupEntry = _SleBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 1, 1)
)
sleBackupEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleBackupConfigFile"),
)
if mibBuilder.loadTexts:
    sleBackupEntry.setStatus("current")
_SleBackupConfigFile_Type = OctetString
_SleBackupConfigFile_Object = MibTableColumn
sleBackupConfigFile = _SleBackupConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 1, 1, 1),
    _SleBackupConfigFile_Type()
)
sleBackupConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBackupConfigFile.setStatus("current")
_SleBackupControl_ObjectIdentity = ObjectIdentity
sleBackupControl = _SleBackupControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2)
)


class _SleBackupControlRequest_Type(Integer32):
    """Custom type sleBackupControlRequest based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("createBackup", 1),
          ("destroyBackup", 2),
          ("setBackupToRemote", 3),
          ("setBackupConfigBySftp", 4),
          ("setBackupConfigByScp", 5),
          ("setBackupKeyBySftp", 6),
          ("setBackupKeyByScp", 7),
          ("createBackupEx", 8),
          ("setBackupToRemoteEx", 9),
          ("setBackupConfigBySftpEx", 10),
          ("setBackupConfigByScpEx", 11),
          ("setBackupKeyBySftpEx", 12),
          ("setBackupKeyByScpEx", 13))
    )


_SleBackupControlRequest_Type.__name__ = "Integer32"
_SleBackupControlRequest_Object = MibScalar
sleBackupControlRequest = _SleBackupControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 1),
    _SleBackupControlRequest_Type()
)
sleBackupControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlRequest.setStatus("current")
_SleBackupControlStatus_Type = SleControlStatusType
_SleBackupControlStatus_Object = MibScalar
sleBackupControlStatus = _SleBackupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 2),
    _SleBackupControlStatus_Type()
)
sleBackupControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBackupControlStatus.setStatus("current")
_SleBackupControlTimer_Type = Gauge32
_SleBackupControlTimer_Object = MibScalar
sleBackupControlTimer = _SleBackupControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 3),
    _SleBackupControlTimer_Type()
)
sleBackupControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlTimer.setStatus("current")
_SleBackupControlTimeStamp_Type = TimeTicks
_SleBackupControlTimeStamp_Object = MibScalar
sleBackupControlTimeStamp = _SleBackupControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 4),
    _SleBackupControlTimeStamp_Type()
)
sleBackupControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBackupControlTimeStamp.setStatus("current")
_SleBackupControlReqResult_Type = SleControlRequestResultType
_SleBackupControlReqResult_Object = MibScalar
sleBackupControlReqResult = _SleBackupControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 5),
    _SleBackupControlReqResult_Type()
)
sleBackupControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBackupControlReqResult.setStatus("current")


class _SleBackupControlCreateMode_Type(Integer32):
    """Custom type sleBackupControlCreateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupFromRunning", 1),
          ("backupFromLocal", 2),
          ("backupFromRemote", 3))
    )


_SleBackupControlCreateMode_Type.__name__ = "Integer32"
_SleBackupControlCreateMode_Object = MibScalar
sleBackupControlCreateMode = _SleBackupControlCreateMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 6),
    _SleBackupControlCreateMode_Type()
)
sleBackupControlCreateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlCreateMode.setStatus("current")
_SleBackupControlServerIP_Type = IpAddress
_SleBackupControlServerIP_Object = MibScalar
sleBackupControlServerIP = _SleBackupControlServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 7),
    _SleBackupControlServerIP_Type()
)
sleBackupControlServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlServerIP.setStatus("current")
_SleBackupControlUserID_Type = OctetString
_SleBackupControlUserID_Object = MibScalar
sleBackupControlUserID = _SleBackupControlUserID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 8),
    _SleBackupControlUserID_Type()
)
sleBackupControlUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlUserID.setStatus("current")
_SleBackupControlPassword_Type = OctetString
_SleBackupControlPassword_Object = MibScalar
sleBackupControlPassword = _SleBackupControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 9),
    _SleBackupControlPassword_Type()
)
sleBackupControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlPassword.setStatus("current")
_SleBackupControlSrcConfigFile_Type = OctetString
_SleBackupControlSrcConfigFile_Object = MibScalar
sleBackupControlSrcConfigFile = _SleBackupControlSrcConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 10),
    _SleBackupControlSrcConfigFile_Type()
)
sleBackupControlSrcConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlSrcConfigFile.setStatus("current")
_SleBackupControlDstConfigFile_Type = OctetString
_SleBackupControlDstConfigFile_Object = MibScalar
sleBackupControlDstConfigFile = _SleBackupControlDstConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 11),
    _SleBackupControlDstConfigFile_Type()
)
sleBackupControlDstConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlDstConfigFile.setStatus("current")
_SleBackupControlServerAddrType_Type = InetAddressType
_SleBackupControlServerAddrType_Object = MibScalar
sleBackupControlServerAddrType = _SleBackupControlServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 12),
    _SleBackupControlServerAddrType_Type()
)
sleBackupControlServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlServerAddrType.setStatus("current")
_SleBackupControlServerAddress_Type = InetAddress
_SleBackupControlServerAddress_Object = MibScalar
sleBackupControlServerAddress = _SleBackupControlServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 2, 13),
    _SleBackupControlServerAddress_Type()
)
sleBackupControlServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleBackupControlServerAddress.setStatus("current")
_SleBackupNotification_ObjectIdentity = ObjectIdentity
sleBackupNotification = _SleBackupNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 3)
)
_SleProcess_ObjectIdentity = ObjectIdentity
sleProcess = _SleProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5)
)
_SleProcessTable_Object = MibTable
sleProcessTable = _SleProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sleProcessTable.setStatus("current")
_SleProcessEntry_Object = MibTableRow
sleProcessEntry = _SleProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1)
)
sleProcessEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleProcessID"),
)
if mibBuilder.loadTexts:
    sleProcessEntry.setStatus("current")


class _SleProcessID_Type(Integer32):
    """Custom type sleProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleProcessID_Type.__name__ = "Integer32"
_SleProcessID_Object = MibTableColumn
sleProcessID = _SleProcessID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 1),
    _SleProcessID_Type()
)
sleProcessID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleProcessID.setStatus("current")
_SleProcessUser_Type = OctetString
_SleProcessUser_Object = MibTableColumn
sleProcessUser = _SleProcessUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 2),
    _SleProcessUser_Type()
)
sleProcessUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessUser.setStatus("current")
_SleProcessCPU_Type = Integer32
_SleProcessCPU_Object = MibTableColumn
sleProcessCPU = _SleProcessCPU_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 3),
    _SleProcessCPU_Type()
)
sleProcessCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessCPU.setStatus("current")
_SleProcessMemory_Type = Integer32
_SleProcessMemory_Object = MibTableColumn
sleProcessMemory = _SleProcessMemory_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 4),
    _SleProcessMemory_Type()
)
sleProcessMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessMemory.setStatus("current")
_SleProcessVSZ_Type = Integer32
_SleProcessVSZ_Object = MibTableColumn
sleProcessVSZ = _SleProcessVSZ_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 5),
    _SleProcessVSZ_Type()
)
sleProcessVSZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessVSZ.setStatus("current")
_SleProcessRSS_Type = Integer32
_SleProcessRSS_Object = MibTableColumn
sleProcessRSS = _SleProcessRSS_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 6),
    _SleProcessRSS_Type()
)
sleProcessRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessRSS.setStatus("current")
_SleProcessTerminal_Type = OctetString
_SleProcessTerminal_Object = MibTableColumn
sleProcessTerminal = _SleProcessTerminal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 7),
    _SleProcessTerminal_Type()
)
sleProcessTerminal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessTerminal.setStatus("current")
_SleProcessStatus_Type = OctetString
_SleProcessStatus_Object = MibTableColumn
sleProcessStatus = _SleProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 8),
    _SleProcessStatus_Type()
)
sleProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessStatus.setStatus("current")
_SleProcessStartTime_Type = OctetString
_SleProcessStartTime_Object = MibTableColumn
sleProcessStartTime = _SleProcessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 9),
    _SleProcessStartTime_Type()
)
sleProcessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessStartTime.setStatus("current")
_SleProcessUsedTime_Type = OctetString
_SleProcessUsedTime_Object = MibTableColumn
sleProcessUsedTime = _SleProcessUsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 10),
    _SleProcessUsedTime_Type()
)
sleProcessUsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessUsedTime.setStatus("current")
_SleProcessCommand_Type = OctetString
_SleProcessCommand_Object = MibTableColumn
sleProcessCommand = _SleProcessCommand_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 5, 1, 1, 11),
    _SleProcessCommand_Type()
)
sleProcessCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleProcessCommand.setStatus("current")
_SleNTP_ObjectIdentity = ObjectIdentity
sleNTP = _SleNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6)
)
_SleNTPServerTable_Object = MibTable
sleNTPServerTable = _SleNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sleNTPServerTable.setStatus("current")
_SleNTPServerEntry_Object = MibTableRow
sleNTPServerEntry = _SleNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 1, 1)
)
sleNTPServerEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerName"),
)
if mibBuilder.loadTexts:
    sleNTPServerEntry.setStatus("current")


class _SleNTPServerName_Type(OctetString):
    """Custom type sleNTPServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SleNTPServerName_Type.__name__ = "OctetString"
_SleNTPServerName_Object = MibTableColumn
sleNTPServerName = _SleNTPServerName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 1, 1, 1),
    _SleNTPServerName_Type()
)
sleNTPServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNTPServerName.setStatus("current")
_SleNtpServerAuthenticationKey_Type = Integer32
_SleNtpServerAuthenticationKey_Object = MibTableColumn
sleNtpServerAuthenticationKey = _SleNtpServerAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 1, 1, 2),
    _SleNtpServerAuthenticationKey_Type()
)
sleNtpServerAuthenticationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNtpServerAuthenticationKey.setStatus("current")
_SleNtpServerVRFIndex_Type = Integer32
_SleNtpServerVRFIndex_Object = MibTableColumn
sleNtpServerVRFIndex = _SleNtpServerVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 1, 1, 3),
    _SleNtpServerVRFIndex_Type()
)
sleNtpServerVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNtpServerVRFIndex.setStatus("current")


class _SleNtpServerPrefer_Type(Integer32):
    """Custom type sleNtpServerPrefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SleNtpServerPrefer_Type.__name__ = "Integer32"
_SleNtpServerPrefer_Object = MibTableColumn
sleNtpServerPrefer = _SleNtpServerPrefer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 1, 1, 4),
    _SleNtpServerPrefer_Type()
)
sleNtpServerPrefer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNtpServerPrefer.setStatus("current")


class _SleNtpServerVersion_Type(Integer32):
    """Custom type sleNtpServerVersion based on Integer32"""
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
        *(("none", 0),
          ("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("version4", 4))
    )


_SleNtpServerVersion_Type.__name__ = "Integer32"
_SleNtpServerVersion_Object = MibTableColumn
sleNtpServerVersion = _SleNtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 1, 1, 5),
    _SleNtpServerVersion_Type()
)
sleNtpServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNtpServerVersion.setStatus("current")
_SleNTPServerControl_ObjectIdentity = ObjectIdentity
sleNTPServerControl = _SleNTPServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2)
)


class _SleNTPServerControlRequest_Type(Integer32):
    """Custom type sleNTPServerControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createNTPServer", 1),
          ("destoryNTPServer", 2))
    )


_SleNTPServerControlRequest_Type.__name__ = "Integer32"
_SleNTPServerControlRequest_Object = MibScalar
sleNTPServerControlRequest = _SleNTPServerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 1),
    _SleNTPServerControlRequest_Type()
)
sleNTPServerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNTPServerControlRequest.setStatus("current")
_SleNTPServerControlStatus_Type = SleControlStatusType
_SleNTPServerControlStatus_Object = MibScalar
sleNTPServerControlStatus = _SleNTPServerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 2),
    _SleNTPServerControlStatus_Type()
)
sleNTPServerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNTPServerControlStatus.setStatus("current")
_SleNTPServerControlTimer_Type = Gauge32
_SleNTPServerControlTimer_Object = MibScalar
sleNTPServerControlTimer = _SleNTPServerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 3),
    _SleNTPServerControlTimer_Type()
)
sleNTPServerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNTPServerControlTimer.setStatus("current")
_SleNTPServerControlTImeStamp_Type = TimeTicks
_SleNTPServerControlTImeStamp_Object = MibScalar
sleNTPServerControlTImeStamp = _SleNTPServerControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 4),
    _SleNTPServerControlTImeStamp_Type()
)
sleNTPServerControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNTPServerControlTImeStamp.setStatus("current")
_SleNTPServerControlReqResult_Type = SleControlRequestResultType
_SleNTPServerControlReqResult_Object = MibScalar
sleNTPServerControlReqResult = _SleNTPServerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 5),
    _SleNTPServerControlReqResult_Type()
)
sleNTPServerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNTPServerControlReqResult.setStatus("current")


class _SleNTPServerControlName_Type(OctetString):
    """Custom type sleNTPServerControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SleNTPServerControlName_Type.__name__ = "OctetString"
_SleNTPServerControlName_Object = MibScalar
sleNTPServerControlName = _SleNTPServerControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 6),
    _SleNTPServerControlName_Type()
)
sleNTPServerControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNTPServerControlName.setStatus("current")
_SleNtpServerControlAuthenticationKey_Type = Integer32
_SleNtpServerControlAuthenticationKey_Object = MibScalar
sleNtpServerControlAuthenticationKey = _SleNtpServerControlAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 7),
    _SleNtpServerControlAuthenticationKey_Type()
)
sleNtpServerControlAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNtpServerControlAuthenticationKey.setStatus("current")
_SleNtpServerControlVRFIndex_Type = Integer32
_SleNtpServerControlVRFIndex_Object = MibScalar
sleNtpServerControlVRFIndex = _SleNtpServerControlVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 8),
    _SleNtpServerControlVRFIndex_Type()
)
sleNtpServerControlVRFIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNtpServerControlVRFIndex.setStatus("current")


class _SleNtpServerControlType_Type(Integer32):
    """Custom type sleNtpServerControlType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ntp", 0),
          ("sntp", 1))
    )


_SleNtpServerControlType_Type.__name__ = "Integer32"
_SleNtpServerControlType_Object = MibScalar
sleNtpServerControlType = _SleNtpServerControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 9),
    _SleNtpServerControlType_Type()
)
sleNtpServerControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNtpServerControlType.setStatus("current")


class _SleNtpServerControlPrefer_Type(Integer32):
    """Custom type sleNtpServerControlPrefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SleNtpServerControlPrefer_Type.__name__ = "Integer32"
_SleNtpServerControlPrefer_Object = MibScalar
sleNtpServerControlPrefer = _SleNtpServerControlPrefer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 10),
    _SleNtpServerControlPrefer_Type()
)
sleNtpServerControlPrefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNtpServerControlPrefer.setStatus("current")


class _SleNtpServerControlVersion_Type(Integer32):
    """Custom type sleNtpServerControlVersion based on Integer32"""
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
        *(("none", 0),
          ("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("version4", 4))
    )


_SleNtpServerControlVersion_Type.__name__ = "Integer32"
_SleNtpServerControlVersion_Object = MibScalar
sleNtpServerControlVersion = _SleNtpServerControlVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 2, 11),
    _SleNtpServerControlVersion_Type()
)
sleNtpServerControlVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNtpServerControlVersion.setStatus("current")
_SleNTPServerNotification_ObjectIdentity = ObjectIdentity
sleNTPServerNotification = _SleNTPServerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 3)
)
_SleSyslogConf_ObjectIdentity = ObjectIdentity
sleSyslogConf = _SleSyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7)
)
_SleSyslogConfTable_Object = MibTable
sleSyslogConfTable = _SleSyslogConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1)
)
if mibBuilder.loadTexts:
    sleSyslogConfTable.setStatus("current")
_SleSyslogConfEntry_Object = MibTableRow
sleSyslogConfEntry = _SleSyslogConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1)
)
sleSyslogConfEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfIndex"),
)
if mibBuilder.loadTexts:
    sleSyslogConfEntry.setStatus("current")


class _SleSyslogConfIndex_Type(Integer32):
    """Custom type sleSyslogConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleSyslogConfIndex_Type.__name__ = "Integer32"
_SleSyslogConfIndex_Object = MibTableColumn
sleSyslogConfIndex = _SleSyslogConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 1),
    _SleSyslogConfIndex_Type()
)
sleSyslogConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfIndex.setStatus("current")


class _SleSyslogConfMode_Type(Integer32):
    """Custom type sleSyslogConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("priority", 1))
    )


_SleSyslogConfMode_Type.__name__ = "Integer32"
_SleSyslogConfMode_Object = MibTableColumn
sleSyslogConfMode = _SleSyslogConfMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 2),
    _SleSyslogConfMode_Type()
)
sleSyslogConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfMode.setStatus("current")


class _SleSyslogConfFacility_Type(Integer32):
    """Custom type sleSyslogConfFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auth", 0),
          ("authpriv", 1),
          ("kern", 2),
          ("local0", 3),
          ("local1", 4),
          ("local2", 5),
          ("local3", 6),
          ("local4", 7),
          ("local5", 8),
          ("local6", 9),
          ("local7", 10),
          ("syslog", 11),
          ("user", 12),
          ("nomap", 99))
    )


_SleSyslogConfFacility_Type.__name__ = "Integer32"
_SleSyslogConfFacility_Object = MibTableColumn
sleSyslogConfFacility = _SleSyslogConfFacility_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 3),
    _SleSyslogConfFacility_Type()
)
sleSyslogConfFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfFacility.setStatus("current")


class _SleSyslogConfSeverity_Type(Integer32):
    """Custom type sleSyslogConfSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7),
          ("other", 99))
    )


_SleSyslogConfSeverity_Type.__name__ = "Integer32"
_SleSyslogConfSeverity_Object = MibTableColumn
sleSyslogConfSeverity = _SleSyslogConfSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 4),
    _SleSyslogConfSeverity_Type()
)
sleSyslogConfSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfSeverity.setStatus("current")


class _SleSyslogConfTarget_Type(Integer32):
    """Custom type sleSyslogConfTarget based on Integer32"""
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
        *(("local", 1),
          ("consol", 2),
          ("remote", 3),
          ("external", 4))
    )


_SleSyslogConfTarget_Type.__name__ = "Integer32"
_SleSyslogConfTarget_Object = MibTableColumn
sleSyslogConfTarget = _SleSyslogConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 5),
    _SleSyslogConfTarget_Type()
)
sleSyslogConfTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfTarget.setStatus("current")


class _SleSyslogConfStorage_Type(Integer32):
    """Custom type sleSyslogConfStorage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", -1),
          ("volatile", 0),
          ("nonvolatile", 1),
          ("sdcardsfu", 2),
          ("sdcard", 3))
    )


_SleSyslogConfStorage_Type.__name__ = "Integer32"
_SleSyslogConfStorage_Object = MibTableColumn
sleSyslogConfStorage = _SleSyslogConfStorage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 6),
    _SleSyslogConfStorage_Type()
)
sleSyslogConfStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfStorage.setStatus("current")
_SleSyslogConfTargetAddress_Type = IpAddress
_SleSyslogConfTargetAddress_Object = MibTableColumn
sleSyslogConfTargetAddress = _SleSyslogConfTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 7),
    _SleSyslogConfTargetAddress_Type()
)
sleSyslogConfTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfTargetAddress.setStatus("current")
_SleSyslogConfRemoteAddrType_Type = InetAddressType
_SleSyslogConfRemoteAddrType_Object = MibTableColumn
sleSyslogConfRemoteAddrType = _SleSyslogConfRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 8),
    _SleSyslogConfRemoteAddrType_Type()
)
sleSyslogConfRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfRemoteAddrType.setStatus("current")
_SleSyslogConfRemoteAddress_Type = InetAddress
_SleSyslogConfRemoteAddress_Object = MibTableColumn
sleSyslogConfRemoteAddress = _SleSyslogConfRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 9),
    _SleSyslogConfRemoteAddress_Type()
)
sleSyslogConfRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfRemoteAddress.setStatus("current")
_SleSyslogConfVRFIndex_Type = Integer32
_SleSyslogConfVRFIndex_Object = MibTableColumn
sleSyslogConfVRFIndex = _SleSyslogConfVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 10),
    _SleSyslogConfVRFIndex_Type()
)
sleSyslogConfVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfVRFIndex.setStatus("current")
_SleSyslogConfSlotIndex_Type = Integer32
_SleSyslogConfSlotIndex_Object = MibTableColumn
sleSyslogConfSlotIndex = _SleSyslogConfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 1, 1, 11),
    _SleSyslogConfSlotIndex_Type()
)
sleSyslogConfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfSlotIndex.setStatus("current")
_SleSyslogConfControl_ObjectIdentity = ObjectIdentity
sleSyslogConfControl = _SleSyslogConfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2)
)


class _SleSyslogConfControlRequest_Type(Integer32):
    """Custom type sleSyslogConfControlRequest based on Integer32"""
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
        *(("createSyslogConf", 1),
          ("destroySyslogConf", 2),
          ("createSyslogConfEx", 3),
          ("destroySyslgConfEx", 4))
    )


_SleSyslogConfControlRequest_Type.__name__ = "Integer32"
_SleSyslogConfControlRequest_Object = MibScalar
sleSyslogConfControlRequest = _SleSyslogConfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 1),
    _SleSyslogConfControlRequest_Type()
)
sleSyslogConfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlRequest.setStatus("current")
_SleSyslogConfControlStatus_Type = Integer32
_SleSyslogConfControlStatus_Object = MibScalar
sleSyslogConfControlStatus = _SleSyslogConfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 2),
    _SleSyslogConfControlStatus_Type()
)
sleSyslogConfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfControlStatus.setStatus("current")
_SleSyslogConfControlTimer_Type = Gauge32
_SleSyslogConfControlTimer_Object = MibScalar
sleSyslogConfControlTimer = _SleSyslogConfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 3),
    _SleSyslogConfControlTimer_Type()
)
sleSyslogConfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlTimer.setStatus("current")
_SleSyslogConfControlTimeStamp_Type = TimeTicks
_SleSyslogConfControlTimeStamp_Object = MibScalar
sleSyslogConfControlTimeStamp = _SleSyslogConfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 4),
    _SleSyslogConfControlTimeStamp_Type()
)
sleSyslogConfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfControlTimeStamp.setStatus("current")
_SleSyslogConfControlReqResult_Type = Integer32
_SleSyslogConfControlReqResult_Object = MibScalar
sleSyslogConfControlReqResult = _SleSyslogConfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 5),
    _SleSyslogConfControlReqResult_Type()
)
sleSyslogConfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogConfControlReqResult.setStatus("current")
_SleSyslogConfControlIndex_Type = Integer32
_SleSyslogConfControlIndex_Object = MibScalar
sleSyslogConfControlIndex = _SleSyslogConfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 6),
    _SleSyslogConfControlIndex_Type()
)
sleSyslogConfControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlIndex.setStatus("current")


class _SleSyslogConfControlMode_Type(Integer32):
    """Custom type sleSyslogConfControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("priority", 1))
    )


_SleSyslogConfControlMode_Type.__name__ = "Integer32"
_SleSyslogConfControlMode_Object = MibScalar
sleSyslogConfControlMode = _SleSyslogConfControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 7),
    _SleSyslogConfControlMode_Type()
)
sleSyslogConfControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlMode.setStatus("current")


class _SleSyslogConfControlSeverity_Type(Integer32):
    """Custom type sleSyslogConfControlSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7),
          ("other", 99))
    )


_SleSyslogConfControlSeverity_Type.__name__ = "Integer32"
_SleSyslogConfControlSeverity_Object = MibScalar
sleSyslogConfControlSeverity = _SleSyslogConfControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 8),
    _SleSyslogConfControlSeverity_Type()
)
sleSyslogConfControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlSeverity.setStatus("current")


class _SleSyslogConfControlFacility_Type(Integer32):
    """Custom type sleSyslogConfControlFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auth", 0),
          ("authpriv", 1),
          ("kern", 2),
          ("local0", 3),
          ("local1", 4),
          ("local2", 5),
          ("local3", 6),
          ("local4", 7),
          ("local5", 8),
          ("local6", 9),
          ("local7", 10),
          ("syslog", 11),
          ("user", 12),
          ("nomap", 99))
    )


_SleSyslogConfControlFacility_Type.__name__ = "Integer32"
_SleSyslogConfControlFacility_Object = MibScalar
sleSyslogConfControlFacility = _SleSyslogConfControlFacility_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 9),
    _SleSyslogConfControlFacility_Type()
)
sleSyslogConfControlFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlFacility.setStatus("current")


class _SleSyslogConfControlTarget_Type(Integer32):
    """Custom type sleSyslogConfControlTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("consol", 2),
          ("remote", 3))
    )


_SleSyslogConfControlTarget_Type.__name__ = "Integer32"
_SleSyslogConfControlTarget_Object = MibScalar
sleSyslogConfControlTarget = _SleSyslogConfControlTarget_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 10),
    _SleSyslogConfControlTarget_Type()
)
sleSyslogConfControlTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlTarget.setStatus("current")


class _SleSyslogConfControlStorage_Type(Integer32):
    """Custom type sleSyslogConfControlStorage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", -1),
          ("volatile", 0),
          ("nonvolatile", 1))
    )


_SleSyslogConfControlStorage_Type.__name__ = "Integer32"
_SleSyslogConfControlStorage_Object = MibScalar
sleSyslogConfControlStorage = _SleSyslogConfControlStorage_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 11),
    _SleSyslogConfControlStorage_Type()
)
sleSyslogConfControlStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlStorage.setStatus("current")
_SleSyslogConfControlTargetAddress_Type = IpAddress
_SleSyslogConfControlTargetAddress_Object = MibScalar
sleSyslogConfControlTargetAddress = _SleSyslogConfControlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 12),
    _SleSyslogConfControlTargetAddress_Type()
)
sleSyslogConfControlTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlTargetAddress.setStatus("current")
_SleSyslogConfControlRemoteAddrType_Type = InetAddressType
_SleSyslogConfControlRemoteAddrType_Object = MibScalar
sleSyslogConfControlRemoteAddrType = _SleSyslogConfControlRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 13),
    _SleSyslogConfControlRemoteAddrType_Type()
)
sleSyslogConfControlRemoteAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlRemoteAddrType.setStatus("current")
_SleSyslogConfControlRemoteAddress_Type = InetAddress
_SleSyslogConfControlRemoteAddress_Object = MibScalar
sleSyslogConfControlRemoteAddress = _SleSyslogConfControlRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 14),
    _SleSyslogConfControlRemoteAddress_Type()
)
sleSyslogConfControlRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlRemoteAddress.setStatus("current")
_SleSyslogConfControlVRFIndex_Type = Integer32
_SleSyslogConfControlVRFIndex_Object = MibScalar
sleSyslogConfControlVRFIndex = _SleSyslogConfControlVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 15),
    _SleSyslogConfControlVRFIndex_Type()
)
sleSyslogConfControlVRFIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlVRFIndex.setStatus("current")
_SleSyslogConfControlSlotIndex_Type = Integer32
_SleSyslogConfControlSlotIndex_Object = MibScalar
sleSyslogConfControlSlotIndex = _SleSyslogConfControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 2, 16),
    _SleSyslogConfControlSlotIndex_Type()
)
sleSyslogConfControlSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSyslogConfControlSlotIndex.setStatus("current")
_SleSyslogConfNotification_ObjectIdentity = ObjectIdentity
sleSyslogConfNotification = _SleSyslogConfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 3)
)
_SleSyslogHistVol_ObjectIdentity = ObjectIdentity
sleSyslogHistVol = _SleSyslogHistVol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 8)
)
_SleSyslogHistVolTable_Object = MibTable
sleSyslogHistVolTable = _SleSyslogHistVolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 8, 1)
)
if mibBuilder.loadTexts:
    sleSyslogHistVolTable.setStatus("current")
_SleSyslogHistVolEntry_Object = MibTableRow
sleSyslogHistVolEntry = _SleSyslogHistVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 8, 1, 1)
)
sleSyslogHistVolEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogHistVolIndex"),
)
if mibBuilder.loadTexts:
    sleSyslogHistVolEntry.setStatus("current")


class _SleSyslogHistVolIndex_Type(Integer32):
    """Custom type sleSyslogHistVolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSyslogHistVolIndex_Type.__name__ = "Integer32"
_SleSyslogHistVolIndex_Object = MibTableColumn
sleSyslogHistVolIndex = _SleSyslogHistVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 8, 1, 1, 1),
    _SleSyslogHistVolIndex_Type()
)
sleSyslogHistVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogHistVolIndex.setStatus("current")
_SleSyslogHistVolMsgText_Type = OctetString
_SleSyslogHistVolMsgText_Object = MibTableColumn
sleSyslogHistVolMsgText = _SleSyslogHistVolMsgText_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 8, 1, 1, 2),
    _SleSyslogHistVolMsgText_Type()
)
sleSyslogHistVolMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogHistVolMsgText.setStatus("current")
_SleSyslogHistVolTime_Type = TimeTicks
_SleSyslogHistVolTime_Object = MibTableColumn
sleSyslogHistVolTime = _SleSyslogHistVolTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 8, 1, 1, 3),
    _SleSyslogHistVolTime_Type()
)
sleSyslogHistVolTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogHistVolTime.setStatus("current")
_SleSyslogHistNVol_ObjectIdentity = ObjectIdentity
sleSyslogHistNVol = _SleSyslogHistNVol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 9)
)
_SleSyslogHistNVolTable_Object = MibTable
sleSyslogHistNVolTable = _SleSyslogHistNVolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 9, 1)
)
if mibBuilder.loadTexts:
    sleSyslogHistNVolTable.setStatus("current")
_SleSyslogHistNVolEntry_Object = MibTableRow
sleSyslogHistNVolEntry = _SleSyslogHistNVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 9, 1, 1)
)
sleSyslogHistNVolEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogHistNVolIndex"),
)
if mibBuilder.loadTexts:
    sleSyslogHistNVolEntry.setStatus("current")


class _SleSyslogHistNVolIndex_Type(Integer32):
    """Custom type sleSyslogHistNVolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSyslogHistNVolIndex_Type.__name__ = "Integer32"
_SleSyslogHistNVolIndex_Object = MibTableColumn
sleSyslogHistNVolIndex = _SleSyslogHistNVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 9, 1, 1, 1),
    _SleSyslogHistNVolIndex_Type()
)
sleSyslogHistNVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogHistNVolIndex.setStatus("current")
_SleSyslogHistNVolMsgText_Type = OctetString
_SleSyslogHistNVolMsgText_Object = MibTableColumn
sleSyslogHistNVolMsgText = _SleSyslogHistNVolMsgText_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 9, 1, 1, 2),
    _SleSyslogHistNVolMsgText_Type()
)
sleSyslogHistNVolMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogHistNVolMsgText.setStatus("current")
_SleSyslogHistNVolTime_Type = TimeTicks
_SleSyslogHistNVolTime_Object = MibTableColumn
sleSyslogHistNVolTime = _SleSyslogHistNVolTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 9, 1, 1, 3),
    _SleSyslogHistNVolTime_Type()
)
sleSyslogHistNVolTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSyslogHistNVolTime.setStatus("current")
_SleSSHRemote_ObjectIdentity = ObjectIdentity
sleSSHRemote = _SleSSHRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10)
)
_SleSSHRemoteTable_Object = MibTable
sleSSHRemoteTable = _SleSSHRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 1)
)
if mibBuilder.loadTexts:
    sleSSHRemoteTable.setStatus("current")
_SleSSHRemoteEntry_Object = MibTableRow
sleSSHRemoteEntry = _SleSSHRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 1, 1)
)
sleSSHRemoteEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteIndex"),
)
if mibBuilder.loadTexts:
    sleSSHRemoteEntry.setStatus("current")


class _SleSSHRemoteIndex_Type(Integer32):
    """Custom type sleSSHRemoteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSSHRemoteIndex_Type.__name__ = "Integer32"
_SleSSHRemoteIndex_Object = MibTableColumn
sleSSHRemoteIndex = _SleSSHRemoteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 1, 1, 1),
    _SleSSHRemoteIndex_Type()
)
sleSSHRemoteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSSHRemoteIndex.setStatus("current")


class _SleSSHRemoteUser_Type(OctetString):
    """Custom type sleSSHRemoteUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SleSSHRemoteUser_Type.__name__ = "OctetString"
_SleSSHRemoteUser_Object = MibTableColumn
sleSSHRemoteUser = _SleSSHRemoteUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 1, 1, 2),
    _SleSSHRemoteUser_Type()
)
sleSSHRemoteUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSSHRemoteUser.setStatus("current")
_SleSSHRemoteHost_Type = IpAddress
_SleSSHRemoteHost_Object = MibTableColumn
sleSSHRemoteHost = _SleSSHRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 1, 1, 3),
    _SleSSHRemoteHost_Type()
)
sleSSHRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSSHRemoteHost.setStatus("current")


class _SleSSHRemoteTime_Type(OctetString):
    """Custom type sleSSHRemoteTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleSSHRemoteTime_Type.__name__ = "OctetString"
_SleSSHRemoteTime_Object = MibTableColumn
sleSSHRemoteTime = _SleSSHRemoteTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 1, 1, 4),
    _SleSSHRemoteTime_Type()
)
sleSSHRemoteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSSHRemoteTime.setStatus("current")
_SleSSHRemoteFromHost_Type = OctetString
_SleSSHRemoteFromHost_Object = MibTableColumn
sleSSHRemoteFromHost = _SleSSHRemoteFromHost_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 1, 1, 5),
    _SleSSHRemoteFromHost_Type()
)
sleSSHRemoteFromHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSSHRemoteFromHost.setStatus("current")
_SleSSHRemoteControl_ObjectIdentity = ObjectIdentity
sleSSHRemoteControl = _SleSSHRemoteControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 2)
)


class _SleSSHRemoteControlRequest_Type(Integer32):
    """Custom type sleSSHRemoteControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("destorySshRemoteConnection", 1)
    )


_SleSSHRemoteControlRequest_Type.__name__ = "Integer32"
_SleSSHRemoteControlRequest_Object = MibScalar
sleSSHRemoteControlRequest = _SleSSHRemoteControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 2, 1),
    _SleSSHRemoteControlRequest_Type()
)
sleSSHRemoteControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSSHRemoteControlRequest.setStatus("current")
_SleSSHRemoteControlStatus_Type = SleControlStatusType
_SleSSHRemoteControlStatus_Object = MibScalar
sleSSHRemoteControlStatus = _SleSSHRemoteControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 2, 2),
    _SleSSHRemoteControlStatus_Type()
)
sleSSHRemoteControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSSHRemoteControlStatus.setStatus("current")
_SleSSHRemoteControlTimer_Type = Gauge32
_SleSSHRemoteControlTimer_Object = MibScalar
sleSSHRemoteControlTimer = _SleSSHRemoteControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 2, 3),
    _SleSSHRemoteControlTimer_Type()
)
sleSSHRemoteControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSSHRemoteControlTimer.setStatus("current")
_SleSSHRemoteControlTImeStamp_Type = TimeTicks
_SleSSHRemoteControlTImeStamp_Object = MibScalar
sleSSHRemoteControlTImeStamp = _SleSSHRemoteControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 2, 4),
    _SleSSHRemoteControlTImeStamp_Type()
)
sleSSHRemoteControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSSHRemoteControlTImeStamp.setStatus("current")
_SleSSHRemoteControlReqResult_Type = SleControlRequestResultType
_SleSSHRemoteControlReqResult_Object = MibScalar
sleSSHRemoteControlReqResult = _SleSSHRemoteControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 2, 5),
    _SleSSHRemoteControlReqResult_Type()
)
sleSSHRemoteControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSSHRemoteControlReqResult.setStatus("current")


class _SleSSHRemoteControlIndex_Type(Integer32):
    """Custom type sleSSHRemoteControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSSHRemoteControlIndex_Type.__name__ = "Integer32"
_SleSSHRemoteControlIndex_Object = MibScalar
sleSSHRemoteControlIndex = _SleSSHRemoteControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 2, 6),
    _SleSSHRemoteControlIndex_Type()
)
sleSSHRemoteControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSSHRemoteControlIndex.setStatus("current")
_SleSSHRemoteNotification_ObjectIdentity = ObjectIdentity
sleSSHRemoteNotification = _SleSSHRemoteNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 3)
)
_SleAutoCli_ObjectIdentity = ObjectIdentity
sleAutoCli = _SleAutoCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11)
)
_SleAutoCliInfo_ObjectIdentity = ObjectIdentity
sleAutoCliInfo = _SleAutoCliInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1)
)
_SleAutoCliBase_ObjectIdentity = ObjectIdentity
sleAutoCliBase = _SleAutoCliBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 1)
)
_SleAutoCliConfStatus_Type = EnableFlag
_SleAutoCliConfStatus_Object = MibScalar
sleAutoCliConfStatus = _SleAutoCliConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 1, 1),
    _SleAutoCliConfStatus_Type()
)
sleAutoCliConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliConfStatus.setStatus("current")
_SleAutoCliMemoryMaxSize_Type = Integer32
_SleAutoCliMemoryMaxSize_Object = MibScalar
sleAutoCliMemoryMaxSize = _SleAutoCliMemoryMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 1, 2),
    _SleAutoCliMemoryMaxSize_Type()
)
sleAutoCliMemoryMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliMemoryMaxSize.setStatus("current")
_SleAutoCliMemoryUsedsize_Type = Integer32
_SleAutoCliMemoryUsedsize_Object = MibScalar
sleAutoCliMemoryUsedsize = _SleAutoCliMemoryUsedsize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 1, 3),
    _SleAutoCliMemoryUsedsize_Type()
)
sleAutoCliMemoryUsedsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliMemoryUsedsize.setStatus("current")
_SleAutoCliMemoryFreesize_Type = Integer32
_SleAutoCliMemoryFreesize_Object = MibScalar
sleAutoCliMemoryFreesize = _SleAutoCliMemoryFreesize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 1, 4),
    _SleAutoCliMemoryFreesize_Type()
)
sleAutoCliMemoryFreesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliMemoryFreesize.setStatus("current")
_SleAutoCliTransferInterval_Type = Integer32
_SleAutoCliTransferInterval_Object = MibScalar
sleAutoCliTransferInterval = _SleAutoCliTransferInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 1, 5),
    _SleAutoCliTransferInterval_Type()
)
sleAutoCliTransferInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliTransferInterval.setStatus("current")
if mibBuilder.loadTexts:
    sleAutoCliTransferInterval.setUnits("minute")
_SleAutoCliBaseControl_ObjectIdentity = ObjectIdentity
sleAutoCliBaseControl = _SleAutoCliBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2)
)


class _SleAutoCliControlRequest_Type(Integer32):
    """Custom type sleAutoCliControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setAutoCliStatus", 1),
          ("setMemoryMaxsize", 2),
          ("setTransferInterval", 3))
    )


_SleAutoCliControlRequest_Type.__name__ = "Integer32"
_SleAutoCliControlRequest_Object = MibScalar
sleAutoCliControlRequest = _SleAutoCliControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2, 1),
    _SleAutoCliControlRequest_Type()
)
sleAutoCliControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliControlRequest.setStatus("current")
_SleAutoCliControlStatus_Type = SleControlStatusType
_SleAutoCliControlStatus_Object = MibScalar
sleAutoCliControlStatus = _SleAutoCliControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2, 2),
    _SleAutoCliControlStatus_Type()
)
sleAutoCliControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliControlStatus.setStatus("current")
_SleAutoCliControlTimer_Type = Gauge32
_SleAutoCliControlTimer_Object = MibScalar
sleAutoCliControlTimer = _SleAutoCliControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2, 3),
    _SleAutoCliControlTimer_Type()
)
sleAutoCliControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliControlTimer.setStatus("current")
_SleAutoCliControlTimeStamp_Type = TimeTicks
_SleAutoCliControlTimeStamp_Object = MibScalar
sleAutoCliControlTimeStamp = _SleAutoCliControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2, 4),
    _SleAutoCliControlTimeStamp_Type()
)
sleAutoCliControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliControlTimeStamp.setStatus("current")
_SleAutoCliControlReqResult_Type = SleControlRequestResultType
_SleAutoCliControlReqResult_Object = MibScalar
sleAutoCliControlReqResult = _SleAutoCliControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2, 5),
    _SleAutoCliControlReqResult_Type()
)
sleAutoCliControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliControlReqResult.setStatus("current")
_SleAutoCliControlConfStatus_Type = EnableFlag
_SleAutoCliControlConfStatus_Object = MibScalar
sleAutoCliControlConfStatus = _SleAutoCliControlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2, 6),
    _SleAutoCliControlConfStatus_Type()
)
sleAutoCliControlConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliControlConfStatus.setStatus("current")
_SleAutoCliControlMemoryMaxsize_Type = Integer32
_SleAutoCliControlMemoryMaxsize_Object = MibScalar
sleAutoCliControlMemoryMaxsize = _SleAutoCliControlMemoryMaxsize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2, 7),
    _SleAutoCliControlMemoryMaxsize_Type()
)
sleAutoCliControlMemoryMaxsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliControlMemoryMaxsize.setStatus("current")
_SleAutoCliControlTransferInterval_Type = Integer32
_SleAutoCliControlTransferInterval_Object = MibScalar
sleAutoCliControlTransferInterval = _SleAutoCliControlTransferInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 2, 8),
    _SleAutoCliControlTransferInterval_Type()
)
sleAutoCliControlTransferInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliControlTransferInterval.setStatus("current")
if mibBuilder.loadTexts:
    sleAutoCliControlTransferInterval.setUnits("minute")
_SleAutoCliBaseNotification_ObjectIdentity = ObjectIdentity
sleAutoCliBaseNotification = _SleAutoCliBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 3)
)
_SleAutoCliScriptFile_ObjectIdentity = ObjectIdentity
sleAutoCliScriptFile = _SleAutoCliScriptFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2)
)
_SleAutoCliScriptFileTable_Object = MibTable
sleAutoCliScriptFileTable = _SleAutoCliScriptFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    sleAutoCliScriptFileTable.setStatus("current")
_SleAutoCliScriptFileEntry_Object = MibTableRow
sleAutoCliScriptFileEntry = _SleAutoCliScriptFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 1, 1)
)
sleAutoCliScriptFileEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptId"),
)
if mibBuilder.loadTexts:
    sleAutoCliScriptFileEntry.setStatus("current")


class _SleAutoCliScriptId_Type(Integer32):
    """Custom type sleAutoCliScriptId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleAutoCliScriptId_Type.__name__ = "Integer32"
_SleAutoCliScriptId_Object = MibTableColumn
sleAutoCliScriptId = _SleAutoCliScriptId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 1, 1, 1),
    _SleAutoCliScriptId_Type()
)
sleAutoCliScriptId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScriptId.setStatus("current")
_SleAutoCliScriptFileName_Type = OctetString
_SleAutoCliScriptFileName_Object = MibTableColumn
sleAutoCliScriptFileName = _SleAutoCliScriptFileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 1, 1, 2),
    _SleAutoCliScriptFileName_Type()
)
sleAutoCliScriptFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileName.setStatus("current")
_SleAutoCliScriptFileUser_Type = OctetString
_SleAutoCliScriptFileUser_Object = MibTableColumn
sleAutoCliScriptFileUser = _SleAutoCliScriptFileUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 1, 1, 3),
    _SleAutoCliScriptFileUser_Type()
)
sleAutoCliScriptFileUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileUser.setStatus("current")
_SleAutoCliScriptFileSize_Type = Integer32
_SleAutoCliScriptFileSize_Object = MibTableColumn
sleAutoCliScriptFileSize = _SleAutoCliScriptFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 1, 1, 4),
    _SleAutoCliScriptFileSize_Type()
)
sleAutoCliScriptFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileSize.setStatus("current")
_SleAutoCliScriptFileUpdateTime_Type = OctetString
_SleAutoCliScriptFileUpdateTime_Object = MibTableColumn
sleAutoCliScriptFileUpdateTime = _SleAutoCliScriptFileUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 1, 1, 5),
    _SleAutoCliScriptFileUpdateTime_Type()
)
sleAutoCliScriptFileUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileUpdateTime.setStatus("current")
_SleAutoCliScriptFileControl_ObjectIdentity = ObjectIdentity
sleAutoCliScriptFileControl = _SleAutoCliScriptFileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2)
)


class _SleAutoCliScriptFileControlRequest_Type(Integer32):
    """Custom type sleAutoCliScriptFileControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftpgetAutoCliScript", 1),
          ("tftpgetAutoCliScript", 2),
          ("destroyedAutoCliScript", 3))
    )


_SleAutoCliScriptFileControlRequest_Type.__name__ = "Integer32"
_SleAutoCliScriptFileControlRequest_Object = MibScalar
sleAutoCliScriptFileControlRequest = _SleAutoCliScriptFileControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 1),
    _SleAutoCliScriptFileControlRequest_Type()
)
sleAutoCliScriptFileControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlRequest.setStatus("current")
_SleAutoCliScriptFileControlStatus_Type = SleControlStatusType
_SleAutoCliScriptFileControlStatus_Object = MibScalar
sleAutoCliScriptFileControlStatus = _SleAutoCliScriptFileControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 2),
    _SleAutoCliScriptFileControlStatus_Type()
)
sleAutoCliScriptFileControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlStatus.setStatus("current")
_SleAutoCliScriptFileControlTimer_Type = Gauge32
_SleAutoCliScriptFileControlTimer_Object = MibScalar
sleAutoCliScriptFileControlTimer = _SleAutoCliScriptFileControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 3),
    _SleAutoCliScriptFileControlTimer_Type()
)
sleAutoCliScriptFileControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlTimer.setStatus("current")
_SleAutoCliScriptFileControlTimeStamp_Type = TimeTicks
_SleAutoCliScriptFileControlTimeStamp_Object = MibScalar
sleAutoCliScriptFileControlTimeStamp = _SleAutoCliScriptFileControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 4),
    _SleAutoCliScriptFileControlTimeStamp_Type()
)
sleAutoCliScriptFileControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlTimeStamp.setStatus("current")
_SleAutoCliScriptFileControlReqResult_Type = SleControlRequestResultType
_SleAutoCliScriptFileControlReqResult_Object = MibScalar
sleAutoCliScriptFileControlReqResult = _SleAutoCliScriptFileControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 5),
    _SleAutoCliScriptFileControlReqResult_Type()
)
sleAutoCliScriptFileControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlReqResult.setStatus("current")
_SleAutoCliScriptFileControlIpAddress_Type = IpAddress
_SleAutoCliScriptFileControlIpAddress_Object = MibScalar
sleAutoCliScriptFileControlIpAddress = _SleAutoCliScriptFileControlIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 6),
    _SleAutoCliScriptFileControlIpAddress_Type()
)
sleAutoCliScriptFileControlIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlIpAddress.setStatus("current")
_SleAutoCliScriptFileControlUserName_Type = OctetString
_SleAutoCliScriptFileControlUserName_Object = MibScalar
sleAutoCliScriptFileControlUserName = _SleAutoCliScriptFileControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 7),
    _SleAutoCliScriptFileControlUserName_Type()
)
sleAutoCliScriptFileControlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlUserName.setStatus("current")
_SleAutoCliScriptFileControlPassword_Type = OctetString
_SleAutoCliScriptFileControlPassword_Object = MibScalar
sleAutoCliScriptFileControlPassword = _SleAutoCliScriptFileControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 8),
    _SleAutoCliScriptFileControlPassword_Type()
)
sleAutoCliScriptFileControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlPassword.setStatus("current")
_SleAutoCliScriptFileControlFilePath_Type = OctetString
_SleAutoCliScriptFileControlFilePath_Object = MibScalar
sleAutoCliScriptFileControlFilePath = _SleAutoCliScriptFileControlFilePath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 9),
    _SleAutoCliScriptFileControlFilePath_Type()
)
sleAutoCliScriptFileControlFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlFilePath.setStatus("current")
_SleAutoCliScriptFileControlScriptName_Type = OctetString
_SleAutoCliScriptFileControlScriptName_Object = MibScalar
sleAutoCliScriptFileControlScriptName = _SleAutoCliScriptFileControlScriptName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 2, 10),
    _SleAutoCliScriptFileControlScriptName_Type()
)
sleAutoCliScriptFileControlScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScriptFileControlScriptName.setStatus("current")
_SleAutoCliScriptFileNotifications_ObjectIdentity = ObjectIdentity
sleAutoCliScriptFileNotifications = _SleAutoCliScriptFileNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 3)
)
_SleAutoCliSchedule_ObjectIdentity = ObjectIdentity
sleAutoCliSchedule = _SleAutoCliSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3)
)
_SleAutoCliScheduleTable_Object = MibTable
sleAutoCliScheduleTable = _SleAutoCliScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    sleAutoCliScheduleTable.setStatus("current")
_SleAutoCliScheduleEntry_Object = MibTableRow
sleAutoCliScheduleEntry = _SleAutoCliScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1)
)
sleAutoCliScheduleEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleName"),
)
if mibBuilder.loadTexts:
    sleAutoCliScheduleEntry.setStatus("current")
_SleAutoCliScheduleName_Type = OctetString
_SleAutoCliScheduleName_Object = MibTableColumn
sleAutoCliScheduleName = _SleAutoCliScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 1),
    _SleAutoCliScheduleName_Type()
)
sleAutoCliScheduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleName.setStatus("current")
_SleAutoCliScheduleType_Type = SleDefAutoCliScheduleType
_SleAutoCliScheduleType_Object = MibTableColumn
sleAutoCliScheduleType = _SleAutoCliScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 2),
    _SleAutoCliScheduleType_Type()
)
sleAutoCliScheduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleType.setStatus("current")
_SleAutoCliScheduleInterval_Type = Integer32
_SleAutoCliScheduleInterval_Object = MibTableColumn
sleAutoCliScheduleInterval = _SleAutoCliScheduleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 3),
    _SleAutoCliScheduleInterval_Type()
)
sleAutoCliScheduleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleInterval.setStatus("current")
_SleAutoCliScheduleYear_Type = Integer32
_SleAutoCliScheduleYear_Object = MibTableColumn
sleAutoCliScheduleYear = _SleAutoCliScheduleYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 4),
    _SleAutoCliScheduleYear_Type()
)
sleAutoCliScheduleYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleYear.setStatus("current")
_SleAutoCliScheduleMonth_Type = Integer32
_SleAutoCliScheduleMonth_Object = MibTableColumn
sleAutoCliScheduleMonth = _SleAutoCliScheduleMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 5),
    _SleAutoCliScheduleMonth_Type()
)
sleAutoCliScheduleMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleMonth.setStatus("current")
_SleAutoCliScheduleDay_Type = Integer32
_SleAutoCliScheduleDay_Object = MibTableColumn
sleAutoCliScheduleDay = _SleAutoCliScheduleDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 6),
    _SleAutoCliScheduleDay_Type()
)
sleAutoCliScheduleDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleDay.setStatus("current")
_SleAutoCliScheduleHour_Type = Integer32
_SleAutoCliScheduleHour_Object = MibTableColumn
sleAutoCliScheduleHour = _SleAutoCliScheduleHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 7),
    _SleAutoCliScheduleHour_Type()
)
sleAutoCliScheduleHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleHour.setStatus("current")
_SleAutoCliScheduleMinute_Type = Integer32
_SleAutoCliScheduleMinute_Object = MibTableColumn
sleAutoCliScheduleMinute = _SleAutoCliScheduleMinute_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 8),
    _SleAutoCliScheduleMinute_Type()
)
sleAutoCliScheduleMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleMinute.setStatus("current")
_SleAutoCliScheduleScriptName_Type = OctetString
_SleAutoCliScheduleScriptName_Object = MibTableColumn
sleAutoCliScheduleScriptName = _SleAutoCliScheduleScriptName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 9),
    _SleAutoCliScheduleScriptName_Type()
)
sleAutoCliScheduleScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleScriptName.setStatus("current")
_SleAutoCliScheduleTransferType_Type = SleDefAutoCliScheduleTransferType
_SleAutoCliScheduleTransferType_Object = MibTableColumn
sleAutoCliScheduleTransferType = _SleAutoCliScheduleTransferType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 10),
    _SleAutoCliScheduleTransferType_Type()
)
sleAutoCliScheduleTransferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleTransferType.setStatus("current")
_SleAutoCliScheduleLastExecutedTime_Type = OctetString
_SleAutoCliScheduleLastExecutedTime_Object = MibTableColumn
sleAutoCliScheduleLastExecutedTime = _SleAutoCliScheduleLastExecutedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 11),
    _SleAutoCliScheduleLastExecutedTime_Type()
)
sleAutoCliScheduleLastExecutedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleLastExecutedTime.setStatus("current")
_SleAutoCliScheduleOutputRule_Type = OctetString
_SleAutoCliScheduleOutputRule_Object = MibTableColumn
sleAutoCliScheduleOutputRule = _SleAutoCliScheduleOutputRule_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 12),
    _SleAutoCliScheduleOutputRule_Type()
)
sleAutoCliScheduleOutputRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleOutputRule.setStatus("current")
_SleAutoCliScheduleLastResult_Type = SleDefAutoCliScheduleResult
_SleAutoCliScheduleLastResult_Object = MibTableColumn
sleAutoCliScheduleLastResult = _SleAutoCliScheduleLastResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 13),
    _SleAutoCliScheduleLastResult_Type()
)
sleAutoCliScheduleLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleLastResult.setStatus("current")


class _SleAutoCliScheduleProfileName_Type(OctetString):
    """Custom type sleAutoCliScheduleProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleAutoCliScheduleProfileName_Type.__name__ = "OctetString"
_SleAutoCliScheduleProfileName_Object = MibTableColumn
sleAutoCliScheduleProfileName = _SleAutoCliScheduleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 1, 1, 14),
    _SleAutoCliScheduleProfileName_Type()
)
sleAutoCliScheduleProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleProfileName.setStatus("current")
_SleAutoCliScheduleControl_ObjectIdentity = ObjectIdentity
sleAutoCliScheduleControl = _SleAutoCliScheduleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2)
)


class _SleAutoCliScheduleControlRequest_Type(Integer32):
    """Custom type sleAutoCliScheduleControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createAutoCliSchedule", 1),
          ("destroyAutoCliSchedule", 2))
    )


_SleAutoCliScheduleControlRequest_Type.__name__ = "Integer32"
_SleAutoCliScheduleControlRequest_Object = MibScalar
sleAutoCliScheduleControlRequest = _SleAutoCliScheduleControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 1),
    _SleAutoCliScheduleControlRequest_Type()
)
sleAutoCliScheduleControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlRequest.setStatus("current")
_SleAutoCliScheduleControlStatus_Type = SleControlStatusType
_SleAutoCliScheduleControlStatus_Object = MibScalar
sleAutoCliScheduleControlStatus = _SleAutoCliScheduleControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 2),
    _SleAutoCliScheduleControlStatus_Type()
)
sleAutoCliScheduleControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlStatus.setStatus("current")
_SleAutoCliScheduleControlTimer_Type = Gauge32
_SleAutoCliScheduleControlTimer_Object = MibScalar
sleAutoCliScheduleControlTimer = _SleAutoCliScheduleControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 3),
    _SleAutoCliScheduleControlTimer_Type()
)
sleAutoCliScheduleControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlTimer.setStatus("current")
_SleAutoCliScheduleControlTimeStamp_Type = TimeTicks
_SleAutoCliScheduleControlTimeStamp_Object = MibScalar
sleAutoCliScheduleControlTimeStamp = _SleAutoCliScheduleControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 4),
    _SleAutoCliScheduleControlTimeStamp_Type()
)
sleAutoCliScheduleControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlTimeStamp.setStatus("current")
_SleAutoCliScheduleControlReqResult_Type = SleControlRequestResultType
_SleAutoCliScheduleControlReqResult_Object = MibScalar
sleAutoCliScheduleControlReqResult = _SleAutoCliScheduleControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 5),
    _SleAutoCliScheduleControlReqResult_Type()
)
sleAutoCliScheduleControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlReqResult.setStatus("current")
_SleAutoCliScheduleControlName_Type = OctetString
_SleAutoCliScheduleControlName_Object = MibScalar
sleAutoCliScheduleControlName = _SleAutoCliScheduleControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 6),
    _SleAutoCliScheduleControlName_Type()
)
sleAutoCliScheduleControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlName.setStatus("current")
_SleAutoCliScheduleControlType_Type = SleDefAutoCliScheduleType
_SleAutoCliScheduleControlType_Object = MibScalar
sleAutoCliScheduleControlType = _SleAutoCliScheduleControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 7),
    _SleAutoCliScheduleControlType_Type()
)
sleAutoCliScheduleControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlType.setStatus("current")
_SleAutoCliScheduleControlInterval_Type = Integer32
_SleAutoCliScheduleControlInterval_Object = MibScalar
sleAutoCliScheduleControlInterval = _SleAutoCliScheduleControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 8),
    _SleAutoCliScheduleControlInterval_Type()
)
sleAutoCliScheduleControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlInterval.setStatus("current")
_SleAutoCliScheduleControlYear_Type = Integer32
_SleAutoCliScheduleControlYear_Object = MibScalar
sleAutoCliScheduleControlYear = _SleAutoCliScheduleControlYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 9),
    _SleAutoCliScheduleControlYear_Type()
)
sleAutoCliScheduleControlYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlYear.setStatus("current")
_SleAutoCliScheduleControlMonth_Type = Integer32
_SleAutoCliScheduleControlMonth_Object = MibScalar
sleAutoCliScheduleControlMonth = _SleAutoCliScheduleControlMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 10),
    _SleAutoCliScheduleControlMonth_Type()
)
sleAutoCliScheduleControlMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlMonth.setStatus("current")
_SleAutoCliScheduleControlDay_Type = Integer32
_SleAutoCliScheduleControlDay_Object = MibScalar
sleAutoCliScheduleControlDay = _SleAutoCliScheduleControlDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 11),
    _SleAutoCliScheduleControlDay_Type()
)
sleAutoCliScheduleControlDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlDay.setStatus("current")
_SleAutoCliScheduleControlHour_Type = Integer32
_SleAutoCliScheduleControlHour_Object = MibScalar
sleAutoCliScheduleControlHour = _SleAutoCliScheduleControlHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 12),
    _SleAutoCliScheduleControlHour_Type()
)
sleAutoCliScheduleControlHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlHour.setStatus("current")
_SleAutoCliScheduleControlMinute_Type = Integer32
_SleAutoCliScheduleControlMinute_Object = MibScalar
sleAutoCliScheduleControlMinute = _SleAutoCliScheduleControlMinute_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 13),
    _SleAutoCliScheduleControlMinute_Type()
)
sleAutoCliScheduleControlMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlMinute.setStatus("current")
_SleAutoCliScheduleControlScriptName_Type = OctetString
_SleAutoCliScheduleControlScriptName_Object = MibScalar
sleAutoCliScheduleControlScriptName = _SleAutoCliScheduleControlScriptName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 14),
    _SleAutoCliScheduleControlScriptName_Type()
)
sleAutoCliScheduleControlScriptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlScriptName.setStatus("current")
_SleAutoCliScheduleControlTransferType_Type = SleDefAutoCliScheduleTransferType
_SleAutoCliScheduleControlTransferType_Object = MibScalar
sleAutoCliScheduleControlTransferType = _SleAutoCliScheduleControlTransferType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 15),
    _SleAutoCliScheduleControlTransferType_Type()
)
sleAutoCliScheduleControlTransferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlTransferType.setStatus("current")
_SleAutoCliScheduleControlOutputRule_Type = OctetString
_SleAutoCliScheduleControlOutputRule_Object = MibScalar
sleAutoCliScheduleControlOutputRule = _SleAutoCliScheduleControlOutputRule_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 16),
    _SleAutoCliScheduleControlOutputRule_Type()
)
sleAutoCliScheduleControlOutputRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlOutputRule.setStatus("current")


class _SleAutoCliScheduleControlProfileName_Type(OctetString):
    """Custom type sleAutoCliScheduleControlProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleAutoCliScheduleControlProfileName_Type.__name__ = "OctetString"
_SleAutoCliScheduleControlProfileName_Object = MibScalar
sleAutoCliScheduleControlProfileName = _SleAutoCliScheduleControlProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 2, 17),
    _SleAutoCliScheduleControlProfileName_Type()
)
sleAutoCliScheduleControlProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliScheduleControlProfileName.setStatus("current")
_SleAutoCliScheduleNotifications_ObjectIdentity = ObjectIdentity
sleAutoCliScheduleNotifications = _SleAutoCliScheduleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 3)
)
_SleAutoCliProfile_ObjectIdentity = ObjectIdentity
sleAutoCliProfile = _SleAutoCliProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4)
)
_SleAutoCliProfileTable_Object = MibTable
sleAutoCliProfileTable = _SleAutoCliProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    sleAutoCliProfileTable.setStatus("current")
_SleAutoCliProfileEntry_Object = MibTableRow
sleAutoCliProfileEntry = _SleAutoCliProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 1, 1)
)
sleAutoCliProfileEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileName"),
)
if mibBuilder.loadTexts:
    sleAutoCliProfileEntry.setStatus("current")


class _SleAutoCliProfileName_Type(OctetString):
    """Custom type sleAutoCliProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleAutoCliProfileName_Type.__name__ = "OctetString"
_SleAutoCliProfileName_Object = MibTableColumn
sleAutoCliProfileName = _SleAutoCliProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 1, 1, 1),
    _SleAutoCliProfileName_Type()
)
sleAutoCliProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileName.setStatus("current")


class _SleAutoCliProfileType_Type(Integer32):
    """Custom type sleAutoCliProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2))
    )


_SleAutoCliProfileType_Type.__name__ = "Integer32"
_SleAutoCliProfileType_Object = MibTableColumn
sleAutoCliProfileType = _SleAutoCliProfileType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 1, 1, 2),
    _SleAutoCliProfileType_Type()
)
sleAutoCliProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileType.setStatus("current")
_SleAutoCliProfileControl_ObjectIdentity = ObjectIdentity
sleAutoCliProfileControl = _SleAutoCliProfileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 2)
)


class _SleAutoCliProfileControlRequest_Type(Integer32):
    """Custom type sleAutoCliProfileControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createAutoCliProfile", 1),
          ("destroyAutoCliProfile", 2))
    )


_SleAutoCliProfileControlRequest_Type.__name__ = "Integer32"
_SleAutoCliProfileControlRequest_Object = MibScalar
sleAutoCliProfileControlRequest = _SleAutoCliProfileControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 2, 1),
    _SleAutoCliProfileControlRequest_Type()
)
sleAutoCliProfileControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileControlRequest.setStatus("current")
_SleAutoCliProfileControlStatus_Type = SleControlStatusType
_SleAutoCliProfileControlStatus_Object = MibScalar
sleAutoCliProfileControlStatus = _SleAutoCliProfileControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 2, 2),
    _SleAutoCliProfileControlStatus_Type()
)
sleAutoCliProfileControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliProfileControlStatus.setStatus("current")
_SleAutoCliProfileControlTimer_Type = Gauge32
_SleAutoCliProfileControlTimer_Object = MibScalar
sleAutoCliProfileControlTimer = _SleAutoCliProfileControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 2, 3),
    _SleAutoCliProfileControlTimer_Type()
)
sleAutoCliProfileControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileControlTimer.setStatus("current")
_SleAutoCliProfileControlTimeStamp_Type = TimeTicks
_SleAutoCliProfileControlTimeStamp_Object = MibScalar
sleAutoCliProfileControlTimeStamp = _SleAutoCliProfileControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 2, 4),
    _SleAutoCliProfileControlTimeStamp_Type()
)
sleAutoCliProfileControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliProfileControlTimeStamp.setStatus("current")
_SleAutoCliProfileControlReqResult_Type = SleControlRequestResultType
_SleAutoCliProfileControlReqResult_Object = MibScalar
sleAutoCliProfileControlReqResult = _SleAutoCliProfileControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 2, 5),
    _SleAutoCliProfileControlReqResult_Type()
)
sleAutoCliProfileControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliProfileControlReqResult.setStatus("current")


class _SleAutoCliProfileControlName_Type(OctetString):
    """Custom type sleAutoCliProfileControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleAutoCliProfileControlName_Type.__name__ = "OctetString"
_SleAutoCliProfileControlName_Object = MibScalar
sleAutoCliProfileControlName = _SleAutoCliProfileControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 2, 6),
    _SleAutoCliProfileControlName_Type()
)
sleAutoCliProfileControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileControlName.setStatus("current")


class _SleAutoCliProfileControlType_Type(Integer32):
    """Custom type sleAutoCliProfileControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2))
    )


_SleAutoCliProfileControlType_Type.__name__ = "Integer32"
_SleAutoCliProfileControlType_Object = MibScalar
sleAutoCliProfileControlType = _SleAutoCliProfileControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 2, 7),
    _SleAutoCliProfileControlType_Type()
)
sleAutoCliProfileControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileControlType.setStatus("current")
_SleAutoCliProfileNotifications_ObjectIdentity = ObjectIdentity
sleAutoCliProfileNotifications = _SleAutoCliProfileNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 3)
)
_SleAutoCliProfileServer_ObjectIdentity = ObjectIdentity
sleAutoCliProfileServer = _SleAutoCliProfileServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5)
)
_SleAutoCliProfileServerTable_Object = MibTable
sleAutoCliProfileServerTable = _SleAutoCliProfileServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 1)
)
if mibBuilder.loadTexts:
    sleAutoCliProfileServerTable.setStatus("current")
_SleAutoCliProfileServerEntry_Object = MibTableRow
sleAutoCliProfileServerEntry = _SleAutoCliProfileServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 1, 1)
)
sleAutoCliProfileServerEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileName"),
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerIpAddress"),
)
if mibBuilder.loadTexts:
    sleAutoCliProfileServerEntry.setStatus("current")


class _SleAutoCliProfileServerType_Type(Integer32):
    """Custom type sleAutoCliProfileServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2))
    )


_SleAutoCliProfileServerType_Type.__name__ = "Integer32"
_SleAutoCliProfileServerType_Object = MibTableColumn
sleAutoCliProfileServerType = _SleAutoCliProfileServerType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 1, 1, 1),
    _SleAutoCliProfileServerType_Type()
)
sleAutoCliProfileServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerType.setStatus("current")
_SleAutoCliProfileServerIpAddress_Type = IpAddress
_SleAutoCliProfileServerIpAddress_Object = MibTableColumn
sleAutoCliProfileServerIpAddress = _SleAutoCliProfileServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 1, 1, 2),
    _SleAutoCliProfileServerIpAddress_Type()
)
sleAutoCliProfileServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerIpAddress.setStatus("current")


class _SleAutoCliProfileServerUser_Type(OctetString):
    """Custom type sleAutoCliProfileServerUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleAutoCliProfileServerUser_Type.__name__ = "OctetString"
_SleAutoCliProfileServerUser_Object = MibTableColumn
sleAutoCliProfileServerUser = _SleAutoCliProfileServerUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 1, 1, 3),
    _SleAutoCliProfileServerUser_Type()
)
sleAutoCliProfileServerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerUser.setStatus("current")


class _SleAutoCliProfileServerPassword_Type(OctetString):
    """Custom type sleAutoCliProfileServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleAutoCliProfileServerPassword_Type.__name__ = "OctetString"
_SleAutoCliProfileServerPassword_Object = MibTableColumn
sleAutoCliProfileServerPassword = _SleAutoCliProfileServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 1, 1, 4),
    _SleAutoCliProfileServerPassword_Type()
)
sleAutoCliProfileServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerPassword.setStatus("current")


class _SleAutoCliProfileServerDir_Type(OctetString):
    """Custom type sleAutoCliProfileServerDir based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SleAutoCliProfileServerDir_Type.__name__ = "OctetString"
_SleAutoCliProfileServerDir_Object = MibTableColumn
sleAutoCliProfileServerDir = _SleAutoCliProfileServerDir_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 1, 1, 5),
    _SleAutoCliProfileServerDir_Type()
)
sleAutoCliProfileServerDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerDir.setStatus("current")
_SleAutoCliProfileServerControl_ObjectIdentity = ObjectIdentity
sleAutoCliProfileServerControl = _SleAutoCliProfileServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2)
)


class _SleAutoCliProfileServerControlRequest_Type(Integer32):
    """Custom type sleAutoCliProfileServerControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createAutoCliProfileServer", 1),
          ("destroyAutoCliProfileServer", 2),
          ("destroyAutoCliProfileServerAll", 3))
    )


_SleAutoCliProfileServerControlRequest_Type.__name__ = "Integer32"
_SleAutoCliProfileServerControlRequest_Object = MibScalar
sleAutoCliProfileServerControlRequest = _SleAutoCliProfileServerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 1),
    _SleAutoCliProfileServerControlRequest_Type()
)
sleAutoCliProfileServerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlRequest.setStatus("current")
_SleAutoCliProfileServerControlStatus_Type = SleControlStatusType
_SleAutoCliProfileServerControlStatus_Object = MibScalar
sleAutoCliProfileServerControlStatus = _SleAutoCliProfileServerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 2),
    _SleAutoCliProfileServerControlStatus_Type()
)
sleAutoCliProfileServerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlStatus.setStatus("current")
_SleAutoCliProfileServerControlTimer_Type = Gauge32
_SleAutoCliProfileServerControlTimer_Object = MibScalar
sleAutoCliProfileServerControlTimer = _SleAutoCliProfileServerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 3),
    _SleAutoCliProfileServerControlTimer_Type()
)
sleAutoCliProfileServerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlTimer.setStatus("current")
_SleAutoCliProfileServerControlTimeStamp_Type = TimeTicks
_SleAutoCliProfileServerControlTimeStamp_Object = MibScalar
sleAutoCliProfileServerControlTimeStamp = _SleAutoCliProfileServerControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 4),
    _SleAutoCliProfileServerControlTimeStamp_Type()
)
sleAutoCliProfileServerControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlTimeStamp.setStatus("current")
_SleAutoCliProfileServerControlReqResult_Type = SleControlRequestResultType
_SleAutoCliProfileServerControlReqResult_Object = MibScalar
sleAutoCliProfileServerControlReqResult = _SleAutoCliProfileServerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 5),
    _SleAutoCliProfileServerControlReqResult_Type()
)
sleAutoCliProfileServerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlReqResult.setStatus("current")


class _SleAutoCliProfileServerControlProfName_Type(OctetString):
    """Custom type sleAutoCliProfileServerControlProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleAutoCliProfileServerControlProfName_Type.__name__ = "OctetString"
_SleAutoCliProfileServerControlProfName_Object = MibScalar
sleAutoCliProfileServerControlProfName = _SleAutoCliProfileServerControlProfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 6),
    _SleAutoCliProfileServerControlProfName_Type()
)
sleAutoCliProfileServerControlProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlProfName.setStatus("current")
_SleAutoCliProfileServerControlIpAddress_Type = IpAddress
_SleAutoCliProfileServerControlIpAddress_Object = MibScalar
sleAutoCliProfileServerControlIpAddress = _SleAutoCliProfileServerControlIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 7),
    _SleAutoCliProfileServerControlIpAddress_Type()
)
sleAutoCliProfileServerControlIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlIpAddress.setStatus("current")


class _SleAutoCliProfileServerControlUser_Type(OctetString):
    """Custom type sleAutoCliProfileServerControlUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleAutoCliProfileServerControlUser_Type.__name__ = "OctetString"
_SleAutoCliProfileServerControlUser_Object = MibScalar
sleAutoCliProfileServerControlUser = _SleAutoCliProfileServerControlUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 8),
    _SleAutoCliProfileServerControlUser_Type()
)
sleAutoCliProfileServerControlUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlUser.setStatus("current")


class _SleAutoCliProfileServerControlPassword_Type(OctetString):
    """Custom type sleAutoCliProfileServerControlPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleAutoCliProfileServerControlPassword_Type.__name__ = "OctetString"
_SleAutoCliProfileServerControlPassword_Object = MibScalar
sleAutoCliProfileServerControlPassword = _SleAutoCliProfileServerControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 9),
    _SleAutoCliProfileServerControlPassword_Type()
)
sleAutoCliProfileServerControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlPassword.setStatus("current")


class _SleAutoCliProfileServerControlDir_Type(OctetString):
    """Custom type sleAutoCliProfileServerControlDir based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SleAutoCliProfileServerControlDir_Type.__name__ = "OctetString"
_SleAutoCliProfileServerControlDir_Object = MibScalar
sleAutoCliProfileServerControlDir = _SleAutoCliProfileServerControlDir_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 2, 10),
    _SleAutoCliProfileServerControlDir_Type()
)
sleAutoCliProfileServerControlDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliProfileServerControlDir.setStatus("current")
_SleAutoCliProfileServerNotifications_ObjectIdentity = ObjectIdentity
sleAutoCliProfileServerNotifications = _SleAutoCliProfileServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 3)
)
_SleAutoCliOutputMemory_ObjectIdentity = ObjectIdentity
sleAutoCliOutputMemory = _SleAutoCliOutputMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6)
)
_SleAutoCliOutputMemoryFileTable_Object = MibTable
sleAutoCliOutputMemoryFileTable = _SleAutoCliOutputMemoryFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 1)
)
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileTable.setStatus("current")
_SleAutoCliOutputMemoryFileEntry_Object = MibTableRow
sleAutoCliOutputMemoryFileEntry = _SleAutoCliOutputMemoryFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 1, 1)
)
sleAutoCliOutputMemoryFileEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileId"),
)
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileEntry.setStatus("current")


class _SleAutoCliOutputMemoryFileId_Type(Integer32):
    """Custom type sleAutoCliOutputMemoryFileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleAutoCliOutputMemoryFileId_Type.__name__ = "Integer32"
_SleAutoCliOutputMemoryFileId_Object = MibTableColumn
sleAutoCliOutputMemoryFileId = _SleAutoCliOutputMemoryFileId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 1, 1, 1),
    _SleAutoCliOutputMemoryFileId_Type()
)
sleAutoCliOutputMemoryFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileId.setStatus("current")
_SleAutoCliOutputMemoryFileName_Type = OctetString
_SleAutoCliOutputMemoryFileName_Object = MibTableColumn
sleAutoCliOutputMemoryFileName = _SleAutoCliOutputMemoryFileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 1, 1, 2),
    _SleAutoCliOutputMemoryFileName_Type()
)
sleAutoCliOutputMemoryFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileName.setStatus("current")
_SleAutoCliOutputMemoryFileSize_Type = Integer32
_SleAutoCliOutputMemoryFileSize_Object = MibTableColumn
sleAutoCliOutputMemoryFileSize = _SleAutoCliOutputMemoryFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 1, 1, 3),
    _SleAutoCliOutputMemoryFileSize_Type()
)
sleAutoCliOutputMemoryFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileSize.setStatus("current")
_SleAutoCliOutputMemoryFileUpdatedTime_Type = OctetString
_SleAutoCliOutputMemoryFileUpdatedTime_Object = MibTableColumn
sleAutoCliOutputMemoryFileUpdatedTime = _SleAutoCliOutputMemoryFileUpdatedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 1, 1, 4),
    _SleAutoCliOutputMemoryFileUpdatedTime_Type()
)
sleAutoCliOutputMemoryFileUpdatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileUpdatedTime.setStatus("current")
_SleAutoCliOutputMemoryFileControl_ObjectIdentity = ObjectIdentity
sleAutoCliOutputMemoryFileControl = _SleAutoCliOutputMemoryFileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2)
)


class _SleAutoCliOutputMemoryFileControlRequest_Type(Integer32):
    """Custom type sleAutoCliOutputMemoryFileControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftpputOutputFile", 1),
          ("tftpputOutputFile", 2),
          ("destroyOutputFile", 3))
    )


_SleAutoCliOutputMemoryFileControlRequest_Type.__name__ = "Integer32"
_SleAutoCliOutputMemoryFileControlRequest_Object = MibScalar
sleAutoCliOutputMemoryFileControlRequest = _SleAutoCliOutputMemoryFileControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 1),
    _SleAutoCliOutputMemoryFileControlRequest_Type()
)
sleAutoCliOutputMemoryFileControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlRequest.setStatus("current")
_SleAutoCliOutputMemoryFileControlStatus_Type = SleControlStatusType
_SleAutoCliOutputMemoryFileControlStatus_Object = MibScalar
sleAutoCliOutputMemoryFileControlStatus = _SleAutoCliOutputMemoryFileControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 2),
    _SleAutoCliOutputMemoryFileControlStatus_Type()
)
sleAutoCliOutputMemoryFileControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlStatus.setStatus("current")
_SleAutoCliOutputMemoryFileControlTimer_Type = Gauge32
_SleAutoCliOutputMemoryFileControlTimer_Object = MibScalar
sleAutoCliOutputMemoryFileControlTimer = _SleAutoCliOutputMemoryFileControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 3),
    _SleAutoCliOutputMemoryFileControlTimer_Type()
)
sleAutoCliOutputMemoryFileControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlTimer.setStatus("current")
_SleAutoCliOutputMemoryFileControlTimeStamp_Type = TimeTicks
_SleAutoCliOutputMemoryFileControlTimeStamp_Object = MibScalar
sleAutoCliOutputMemoryFileControlTimeStamp = _SleAutoCliOutputMemoryFileControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 4),
    _SleAutoCliOutputMemoryFileControlTimeStamp_Type()
)
sleAutoCliOutputMemoryFileControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlTimeStamp.setStatus("current")
_SleAutoCliOutputMemoryFileControlReqResult_Type = SleControlRequestResultType
_SleAutoCliOutputMemoryFileControlReqResult_Object = MibScalar
sleAutoCliOutputMemoryFileControlReqResult = _SleAutoCliOutputMemoryFileControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 5),
    _SleAutoCliOutputMemoryFileControlReqResult_Type()
)
sleAutoCliOutputMemoryFileControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlReqResult.setStatus("current")
_SleAutoCliOutputMemoryFileControlServer_Type = IpAddress
_SleAutoCliOutputMemoryFileControlServer_Object = MibScalar
sleAutoCliOutputMemoryFileControlServer = _SleAutoCliOutputMemoryFileControlServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 6),
    _SleAutoCliOutputMemoryFileControlServer_Type()
)
sleAutoCliOutputMemoryFileControlServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlServer.setStatus("current")
_SleAutoCliOutputMemoryFileControlUserName_Type = OctetString
_SleAutoCliOutputMemoryFileControlUserName_Object = MibScalar
sleAutoCliOutputMemoryFileControlUserName = _SleAutoCliOutputMemoryFileControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 7),
    _SleAutoCliOutputMemoryFileControlUserName_Type()
)
sleAutoCliOutputMemoryFileControlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlUserName.setStatus("current")
_SleAutoCliOutputMemoryFileControlPassword_Type = OctetString
_SleAutoCliOutputMemoryFileControlPassword_Object = MibScalar
sleAutoCliOutputMemoryFileControlPassword = _SleAutoCliOutputMemoryFileControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 8),
    _SleAutoCliOutputMemoryFileControlPassword_Type()
)
sleAutoCliOutputMemoryFileControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlPassword.setStatus("current")
_SleAutoCliOutputMemoryFileControlOutputFileName_Type = OctetString
_SleAutoCliOutputMemoryFileControlOutputFileName_Object = MibScalar
sleAutoCliOutputMemoryFileControlOutputFileName = _SleAutoCliOutputMemoryFileControlOutputFileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 9),
    _SleAutoCliOutputMemoryFileControlOutputFileName_Type()
)
sleAutoCliOutputMemoryFileControlOutputFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlOutputFileName.setStatus("current")
_SleAutoCliOutputMemoryFileControlRemotePath_Type = OctetString
_SleAutoCliOutputMemoryFileControlRemotePath_Object = MibScalar
sleAutoCliOutputMemoryFileControlRemotePath = _SleAutoCliOutputMemoryFileControlRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 2, 10),
    _SleAutoCliOutputMemoryFileControlRemotePath_Type()
)
sleAutoCliOutputMemoryFileControlRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileControlRemotePath.setStatus("current")
_SleAutoCliOutputMemoryFileNotification_ObjectIdentity = ObjectIdentity
sleAutoCliOutputMemoryFileNotification = _SleAutoCliOutputMemoryFileNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 3)
)
_SleAutoReset_ObjectIdentity = ObjectIdentity
sleAutoReset = _SleAutoReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12)
)
_SleAutoResetPing_ObjectIdentity = ObjectIdentity
sleAutoResetPing = _SleAutoResetPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1)
)
_SleAutoResetPingInfo_ObjectIdentity = ObjectIdentity
sleAutoResetPingInfo = _SleAutoResetPingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1)
)
_SleAutoResetPingConfStatus_Type = EnableFlag
_SleAutoResetPingConfStatus_Object = MibScalar
sleAutoResetPingConfStatus = _SleAutoResetPingConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 1),
    _SleAutoResetPingConfStatus_Type()
)
sleAutoResetPingConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingConfStatus.setStatus("current")
_SleAutoResetPingIpAddress_Type = IpAddress
_SleAutoResetPingIpAddress_Object = MibScalar
sleAutoResetPingIpAddress = _SleAutoResetPingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 2),
    _SleAutoResetPingIpAddress_Type()
)
sleAutoResetPingIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingIpAddress.setStatus("current")
_SleAutoResetPingTransactionInterval_Type = Integer32
_SleAutoResetPingTransactionInterval_Object = MibScalar
sleAutoResetPingTransactionInterval = _SleAutoResetPingTransactionInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 3),
    _SleAutoResetPingTransactionInterval_Type()
)
sleAutoResetPingTransactionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingTransactionInterval.setStatus("current")
_SleAutoResetPingNumberOfRequest_Type = Integer32
_SleAutoResetPingNumberOfRequest_Object = MibScalar
sleAutoResetPingNumberOfRequest = _SleAutoResetPingNumberOfRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 4),
    _SleAutoResetPingNumberOfRequest_Type()
)
sleAutoResetPingNumberOfRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingNumberOfRequest.setStatus("current")
_SleAutoResetPingRequestInterval_Type = Integer32
_SleAutoResetPingRequestInterval_Object = MibScalar
sleAutoResetPingRequestInterval = _SleAutoResetPingRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 5),
    _SleAutoResetPingRequestInterval_Type()
)
sleAutoResetPingRequestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingRequestInterval.setStatus("current")
_SleAutoResetPingTimeoutOfRequest_Type = Integer32
_SleAutoResetPingTimeoutOfRequest_Object = MibScalar
sleAutoResetPingTimeoutOfRequest = _SleAutoResetPingTimeoutOfRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 6),
    _SleAutoResetPingTimeoutOfRequest_Type()
)
sleAutoResetPingTimeoutOfRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingTimeoutOfRequest.setStatus("current")
_SleAutoResetPingLossThreshold_Type = Integer32
_SleAutoResetPingLossThreshold_Object = MibScalar
sleAutoResetPingLossThreshold = _SleAutoResetPingLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 7),
    _SleAutoResetPingLossThreshold_Type()
)
sleAutoResetPingLossThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingLossThreshold.setStatus("current")
_SleAutoResetPingEnableTime_Type = OctetString
_SleAutoResetPingEnableTime_Object = MibScalar
sleAutoResetPingEnableTime = _SleAutoResetPingEnableTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 8),
    _SleAutoResetPingEnableTime_Type()
)
sleAutoResetPingEnableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingEnableTime.setStatus("current")
_SleAutoResetPingRequestCount_Type = Integer32
_SleAutoResetPingRequestCount_Object = MibScalar
sleAutoResetPingRequestCount = _SleAutoResetPingRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 9),
    _SleAutoResetPingRequestCount_Type()
)
sleAutoResetPingRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingRequestCount.setStatus("current")
_SleAutoResetPingReplyCount_Type = Integer32
_SleAutoResetPingReplyCount_Object = MibScalar
sleAutoResetPingReplyCount = _SleAutoResetPingReplyCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 10),
    _SleAutoResetPingReplyCount_Type()
)
sleAutoResetPingReplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingReplyCount.setStatus("current")
_SleAutoResetPingLossCount_Type = Integer32
_SleAutoResetPingLossCount_Object = MibScalar
sleAutoResetPingLossCount = _SleAutoResetPingLossCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 11),
    _SleAutoResetPingLossCount_Type()
)
sleAutoResetPingLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingLossCount.setStatus("current")
_SleAutoResetPingTotalPingTransaction_Type = Counter64
_SleAutoResetPingTotalPingTransaction_Object = MibScalar
sleAutoResetPingTotalPingTransaction = _SleAutoResetPingTotalPingTransaction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 12),
    _SleAutoResetPingTotalPingTransaction_Type()
)
sleAutoResetPingTotalPingTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingTotalPingTransaction.setStatus("current")
_SleAutoResetPingTotalLossTransaction_Type = Counter64
_SleAutoResetPingTotalLossTransaction_Object = MibScalar
sleAutoResetPingTotalLossTransaction = _SleAutoResetPingTotalLossTransaction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 13),
    _SleAutoResetPingTotalLossTransaction_Type()
)
sleAutoResetPingTotalLossTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingTotalLossTransaction.setStatus("current")


class _SleAutoResetPingRebootThreshold_Type(Integer32):
    """Custom type sleAutoResetPingRebootThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleAutoResetPingRebootThreshold_Type.__name__ = "Integer32"
_SleAutoResetPingRebootThreshold_Object = MibScalar
sleAutoResetPingRebootThreshold = _SleAutoResetPingRebootThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 14),
    _SleAutoResetPingRebootThreshold_Type()
)
sleAutoResetPingRebootThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingRebootThreshold.setStatus("current")
_SleAutoResetPingRebootCounter_Type = Integer32
_SleAutoResetPingRebootCounter_Object = MibScalar
sleAutoResetPingRebootCounter = _SleAutoResetPingRebootCounter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 15),
    _SleAutoResetPingRebootCounter_Type()
)
sleAutoResetPingRebootCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingRebootCounter.setStatus("current")


class _SleAutoResetPingRebootRecoveryTime_Type(Integer32):
    """Custom type sleAutoResetPingRebootRecoveryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 14400),
    )


_SleAutoResetPingRebootRecoveryTime_Type.__name__ = "Integer32"
_SleAutoResetPingRebootRecoveryTime_Object = MibScalar
sleAutoResetPingRebootRecoveryTime = _SleAutoResetPingRebootRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 1, 16),
    _SleAutoResetPingRebootRecoveryTime_Type()
)
sleAutoResetPingRebootRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingRebootRecoveryTime.setStatus("current")
_SleAutoResetPingControl_ObjectIdentity = ObjectIdentity
sleAutoResetPingControl = _SleAutoResetPingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2)
)


class _SleAutoResetPingControlRequest_Type(Integer32):
    """Custom type sleAutoResetPingControlRequest based on Integer32"""
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
        *(("setAutoResetPingStatus", 1),
          ("modifyAutoResetPingInfo", 2),
          ("setAutoResetPingRebootCtrl", 3),
          ("clearAutoResetPingRebootCounter", 4))
    )


_SleAutoResetPingControlRequest_Type.__name__ = "Integer32"
_SleAutoResetPingControlRequest_Object = MibScalar
sleAutoResetPingControlRequest = _SleAutoResetPingControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 1),
    _SleAutoResetPingControlRequest_Type()
)
sleAutoResetPingControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlRequest.setStatus("current")
_SleAutoResetPingControlStatus_Type = SleControlStatusType
_SleAutoResetPingControlStatus_Object = MibScalar
sleAutoResetPingControlStatus = _SleAutoResetPingControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 2),
    _SleAutoResetPingControlStatus_Type()
)
sleAutoResetPingControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingControlStatus.setStatus("current")
_SleAutoResetPingControlTimer_Type = Gauge32
_SleAutoResetPingControlTimer_Object = MibScalar
sleAutoResetPingControlTimer = _SleAutoResetPingControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 3),
    _SleAutoResetPingControlTimer_Type()
)
sleAutoResetPingControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlTimer.setStatus("current")
_SleAutoResetPingControlTimeStamp_Type = TimeTicks
_SleAutoResetPingControlTimeStamp_Object = MibScalar
sleAutoResetPingControlTimeStamp = _SleAutoResetPingControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 4),
    _SleAutoResetPingControlTimeStamp_Type()
)
sleAutoResetPingControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingControlTimeStamp.setStatus("current")
_SleAutoResetPingControlReqResult_Type = SleControlRequestResultType
_SleAutoResetPingControlReqResult_Object = MibScalar
sleAutoResetPingControlReqResult = _SleAutoResetPingControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 5),
    _SleAutoResetPingControlReqResult_Type()
)
sleAutoResetPingControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetPingControlReqResult.setStatus("current")
_SleAutoResetPingControlConfStatus_Type = EnableFlag
_SleAutoResetPingControlConfStatus_Object = MibScalar
sleAutoResetPingControlConfStatus = _SleAutoResetPingControlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 6),
    _SleAutoResetPingControlConfStatus_Type()
)
sleAutoResetPingControlConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlConfStatus.setStatus("current")
_SleAutoResetPingControlIpAddress_Type = IpAddress
_SleAutoResetPingControlIpAddress_Object = MibScalar
sleAutoResetPingControlIpAddress = _SleAutoResetPingControlIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 7),
    _SleAutoResetPingControlIpAddress_Type()
)
sleAutoResetPingControlIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlIpAddress.setStatus("current")
_SleAutoResetPingControlTransactionInterval_Type = Integer32
_SleAutoResetPingControlTransactionInterval_Object = MibScalar
sleAutoResetPingControlTransactionInterval = _SleAutoResetPingControlTransactionInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 8),
    _SleAutoResetPingControlTransactionInterval_Type()
)
sleAutoResetPingControlTransactionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlTransactionInterval.setStatus("current")
_SleAutoResetPingControlNumberOfRequest_Type = Integer32
_SleAutoResetPingControlNumberOfRequest_Object = MibScalar
sleAutoResetPingControlNumberOfRequest = _SleAutoResetPingControlNumberOfRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 9),
    _SleAutoResetPingControlNumberOfRequest_Type()
)
sleAutoResetPingControlNumberOfRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlNumberOfRequest.setStatus("current")
_SleAutoResetPingControlRequestInterval_Type = Integer32
_SleAutoResetPingControlRequestInterval_Object = MibScalar
sleAutoResetPingControlRequestInterval = _SleAutoResetPingControlRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 10),
    _SleAutoResetPingControlRequestInterval_Type()
)
sleAutoResetPingControlRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlRequestInterval.setStatus("current")
_SleAutoResetPingControlTimeoutOfRequest_Type = Integer32
_SleAutoResetPingControlTimeoutOfRequest_Object = MibScalar
sleAutoResetPingControlTimeoutOfRequest = _SleAutoResetPingControlTimeoutOfRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 11),
    _SleAutoResetPingControlTimeoutOfRequest_Type()
)
sleAutoResetPingControlTimeoutOfRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlTimeoutOfRequest.setStatus("current")
_SleAutoResetPingControlPingLossThreshold_Type = Integer32
_SleAutoResetPingControlPingLossThreshold_Object = MibScalar
sleAutoResetPingControlPingLossThreshold = _SleAutoResetPingControlPingLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 12),
    _SleAutoResetPingControlPingLossThreshold_Type()
)
sleAutoResetPingControlPingLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlPingLossThreshold.setStatus("current")


class _SleAutoResetPingControlRebootThreshold_Type(Integer32):
    """Custom type sleAutoResetPingControlRebootThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleAutoResetPingControlRebootThreshold_Type.__name__ = "Integer32"
_SleAutoResetPingControlRebootThreshold_Object = MibScalar
sleAutoResetPingControlRebootThreshold = _SleAutoResetPingControlRebootThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 13),
    _SleAutoResetPingControlRebootThreshold_Type()
)
sleAutoResetPingControlRebootThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlRebootThreshold.setStatus("current")


class _SleAutoResetPingControlRebootRecoveryTime_Type(Integer32):
    """Custom type sleAutoResetPingControlRebootRecoveryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 14400),
    )


_SleAutoResetPingControlRebootRecoveryTime_Type.__name__ = "Integer32"
_SleAutoResetPingControlRebootRecoveryTime_Object = MibScalar
sleAutoResetPingControlRebootRecoveryTime = _SleAutoResetPingControlRebootRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 2, 14),
    _SleAutoResetPingControlRebootRecoveryTime_Type()
)
sleAutoResetPingControlRebootRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetPingControlRebootRecoveryTime.setStatus("current")
_SleAutoResetPingNotification_ObjectIdentity = ObjectIdentity
sleAutoResetPingNotification = _SleAutoResetPingNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 3)
)
_SleAutoResetMemoryleak_ObjectIdentity = ObjectIdentity
sleAutoResetMemoryleak = _SleAutoResetMemoryleak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2)
)
_SleAutoResetMemoryleakInfo_ObjectIdentity = ObjectIdentity
sleAutoResetMemoryleakInfo = _SleAutoResetMemoryleakInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1)
)
_SleAutoResetMemoryleakContStatus_Type = EnableFlag
_SleAutoResetMemoryleakContStatus_Object = MibScalar
sleAutoResetMemoryleakContStatus = _SleAutoResetMemoryleakContStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 1),
    _SleAutoResetMemoryleakContStatus_Type()
)
sleAutoResetMemoryleakContStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakContStatus.setStatus("current")
_SleAutoResetMemoryleakMemThreshold_Type = Integer32
_SleAutoResetMemoryleakMemThreshold_Object = MibScalar
sleAutoResetMemoryleakMemThreshold = _SleAutoResetMemoryleakMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 2),
    _SleAutoResetMemoryleakMemThreshold_Type()
)
sleAutoResetMemoryleakMemThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakMemThreshold.setStatus("current")
_SleAutoResetMemoryleakCheckInterval_Type = Integer32
_SleAutoResetMemoryleakCheckInterval_Object = MibScalar
sleAutoResetMemoryleakCheckInterval = _SleAutoResetMemoryleakCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 3),
    _SleAutoResetMemoryleakCheckInterval_Type()
)
sleAutoResetMemoryleakCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakCheckInterval.setStatus("current")
_SleAutoResetMemoryleakNumberOfVerification_Type = Integer32
_SleAutoResetMemoryleakNumberOfVerification_Object = MibScalar
sleAutoResetMemoryleakNumberOfVerification = _SleAutoResetMemoryleakNumberOfVerification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 4),
    _SleAutoResetMemoryleakNumberOfVerification_Type()
)
sleAutoResetMemoryleakNumberOfVerification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakNumberOfVerification.setStatus("current")
_SleAutoResetMemoryleakVerificationInterval_Type = Integer32
_SleAutoResetMemoryleakVerificationInterval_Object = MibScalar
sleAutoResetMemoryleakVerificationInterval = _SleAutoResetMemoryleakVerificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 5),
    _SleAutoResetMemoryleakVerificationInterval_Type()
)
sleAutoResetMemoryleakVerificationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakVerificationInterval.setStatus("current")
_SleAutoResetMemoryleakCountThreshold_Type = Integer32
_SleAutoResetMemoryleakCountThreshold_Object = MibScalar
sleAutoResetMemoryleakCountThreshold = _SleAutoResetMemoryleakCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 6),
    _SleAutoResetMemoryleakCountThreshold_Type()
)
sleAutoResetMemoryleakCountThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakCountThreshold.setStatus("current")
_SleAutoResetMemoryleakEnableTime_Type = OctetString
_SleAutoResetMemoryleakEnableTime_Object = MibScalar
sleAutoResetMemoryleakEnableTime = _SleAutoResetMemoryleakEnableTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 7),
    _SleAutoResetMemoryleakEnableTime_Type()
)
sleAutoResetMemoryleakEnableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakEnableTime.setStatus("current")
_SleAutoResetMemoryleakLastFreeMemory_Type = Integer32
_SleAutoResetMemoryleakLastFreeMemory_Object = MibScalar
sleAutoResetMemoryleakLastFreeMemory = _SleAutoResetMemoryleakLastFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 8),
    _SleAutoResetMemoryleakLastFreeMemory_Type()
)
sleAutoResetMemoryleakLastFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakLastFreeMemory.setStatus("current")
_SleAutoResetMemoryleakVerificationCount_Type = Integer32
_SleAutoResetMemoryleakVerificationCount_Object = MibScalar
sleAutoResetMemoryleakVerificationCount = _SleAutoResetMemoryleakVerificationCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 9),
    _SleAutoResetMemoryleakVerificationCount_Type()
)
sleAutoResetMemoryleakVerificationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakVerificationCount.setStatus("current")
_SleAutoResetMemoryleakDetectionCount_Type = Integer32
_SleAutoResetMemoryleakDetectionCount_Object = MibScalar
sleAutoResetMemoryleakDetectionCount = _SleAutoResetMemoryleakDetectionCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 10),
    _SleAutoResetMemoryleakDetectionCount_Type()
)
sleAutoResetMemoryleakDetectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakDetectionCount.setStatus("current")
_SleAutoResetMemoryleakTotalVerificationCount_Type = Counter64
_SleAutoResetMemoryleakTotalVerificationCount_Object = MibScalar
sleAutoResetMemoryleakTotalVerificationCount = _SleAutoResetMemoryleakTotalVerificationCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 11),
    _SleAutoResetMemoryleakTotalVerificationCount_Type()
)
sleAutoResetMemoryleakTotalVerificationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakTotalVerificationCount.setStatus("current")
_SleAutoResetMemoryleakTotalDetectionCount_Type = Counter64
_SleAutoResetMemoryleakTotalDetectionCount_Object = MibScalar
sleAutoResetMemoryleakTotalDetectionCount = _SleAutoResetMemoryleakTotalDetectionCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 12),
    _SleAutoResetMemoryleakTotalDetectionCount_Type()
)
sleAutoResetMemoryleakTotalDetectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakTotalDetectionCount.setStatus("current")


class _SleAutoResetMemoryleakReboottimeStartHour_Type(Integer32):
    """Custom type sleAutoResetMemoryleakReboottimeStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_SleAutoResetMemoryleakReboottimeStartHour_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakReboottimeStartHour_Object = MibScalar
sleAutoResetMemoryleakReboottimeStartHour = _SleAutoResetMemoryleakReboottimeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 13),
    _SleAutoResetMemoryleakReboottimeStartHour_Type()
)
sleAutoResetMemoryleakReboottimeStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakReboottimeStartHour.setStatus("current")


class _SleAutoResetMemoryleakReboottimeStartMin_Type(Integer32):
    """Custom type sleAutoResetMemoryleakReboottimeStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 59),
    )


_SleAutoResetMemoryleakReboottimeStartMin_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakReboottimeStartMin_Object = MibScalar
sleAutoResetMemoryleakReboottimeStartMin = _SleAutoResetMemoryleakReboottimeStartMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 14),
    _SleAutoResetMemoryleakReboottimeStartMin_Type()
)
sleAutoResetMemoryleakReboottimeStartMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakReboottimeStartMin.setStatus("current")


class _SleAutoResetMemoryleakReboottimeEndHour_Type(Integer32):
    """Custom type sleAutoResetMemoryleakReboottimeEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_SleAutoResetMemoryleakReboottimeEndHour_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakReboottimeEndHour_Object = MibScalar
sleAutoResetMemoryleakReboottimeEndHour = _SleAutoResetMemoryleakReboottimeEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 15),
    _SleAutoResetMemoryleakReboottimeEndHour_Type()
)
sleAutoResetMemoryleakReboottimeEndHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakReboottimeEndHour.setStatus("current")


class _SleAutoResetMemoryleakReboottimeEndMin_Type(Integer32):
    """Custom type sleAutoResetMemoryleakReboottimeEndMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 59),
    )


_SleAutoResetMemoryleakReboottimeEndMin_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakReboottimeEndMin_Object = MibScalar
sleAutoResetMemoryleakReboottimeEndMin = _SleAutoResetMemoryleakReboottimeEndMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 16),
    _SleAutoResetMemoryleakReboottimeEndMin_Type()
)
sleAutoResetMemoryleakReboottimeEndMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakReboottimeEndMin.setStatus("current")


class _SleAutoResetMemoryleakRebootThreshold_Type(Integer32):
    """Custom type sleAutoResetMemoryleakRebootThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleAutoResetMemoryleakRebootThreshold_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakRebootThreshold_Object = MibScalar
sleAutoResetMemoryleakRebootThreshold = _SleAutoResetMemoryleakRebootThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 17),
    _SleAutoResetMemoryleakRebootThreshold_Type()
)
sleAutoResetMemoryleakRebootThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakRebootThreshold.setStatus("current")
_SleAutoResetMemoryleakRebootCount_Type = Integer32
_SleAutoResetMemoryleakRebootCount_Object = MibScalar
sleAutoResetMemoryleakRebootCount = _SleAutoResetMemoryleakRebootCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 1, 18),
    _SleAutoResetMemoryleakRebootCount_Type()
)
sleAutoResetMemoryleakRebootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakRebootCount.setStatus("current")
_SleAutoResetMemoryleakControl_ObjectIdentity = ObjectIdentity
sleAutoResetMemoryleakControl = _SleAutoResetMemoryleakControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2)
)


class _SleAutoResetMemoryleakControlRequest_Type(Integer32):
    """Custom type sleAutoResetMemoryleakControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("setAutoResetMemoryleakStatus", 1),
          ("modifyAutoResetMemoryleakInfo", 2),
          ("modifyAutoResetMomoryleakReboottime", 3),
          ("setAutoResetMemoryRebootCtrl", 4),
          ("setAutoResetclearAutoResetRebootCounter", 5))
    )


_SleAutoResetMemoryleakControlRequest_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakControlRequest_Object = MibScalar
sleAutoResetMemoryleakControlRequest = _SleAutoResetMemoryleakControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 1),
    _SleAutoResetMemoryleakControlRequest_Type()
)
sleAutoResetMemoryleakControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlRequest.setStatus("current")
_SleAutoResetMemoryleakControlStatus_Type = SleControlStatusType
_SleAutoResetMemoryleakControlStatus_Object = MibScalar
sleAutoResetMemoryleakControlStatus = _SleAutoResetMemoryleakControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 2),
    _SleAutoResetMemoryleakControlStatus_Type()
)
sleAutoResetMemoryleakControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlStatus.setStatus("current")
_SleAutoResetMemoryleakControlTimer_Type = Gauge32
_SleAutoResetMemoryleakControlTimer_Object = MibScalar
sleAutoResetMemoryleakControlTimer = _SleAutoResetMemoryleakControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 3),
    _SleAutoResetMemoryleakControlTimer_Type()
)
sleAutoResetMemoryleakControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlTimer.setStatus("current")
_SleAutoResetMemoryleakControlTimeStamp_Type = TimeTicks
_SleAutoResetMemoryleakControlTimeStamp_Object = MibScalar
sleAutoResetMemoryleakControlTimeStamp = _SleAutoResetMemoryleakControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 4),
    _SleAutoResetMemoryleakControlTimeStamp_Type()
)
sleAutoResetMemoryleakControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlTimeStamp.setStatus("current")
_SleAutoResetMemoryleakControlReqResult_Type = SleControlRequestResultType
_SleAutoResetMemoryleakControlReqResult_Object = MibScalar
sleAutoResetMemoryleakControlReqResult = _SleAutoResetMemoryleakControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 5),
    _SleAutoResetMemoryleakControlReqResult_Type()
)
sleAutoResetMemoryleakControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlReqResult.setStatus("current")
_SleAutoResetMemoryleakControlConfStatus_Type = EnableFlag
_SleAutoResetMemoryleakControlConfStatus_Object = MibScalar
sleAutoResetMemoryleakControlConfStatus = _SleAutoResetMemoryleakControlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 6),
    _SleAutoResetMemoryleakControlConfStatus_Type()
)
sleAutoResetMemoryleakControlConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlConfStatus.setStatus("current")
_SleAutoResetMemoryleakControlMemThreshold_Type = Integer32
_SleAutoResetMemoryleakControlMemThreshold_Object = MibScalar
sleAutoResetMemoryleakControlMemThreshold = _SleAutoResetMemoryleakControlMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 7),
    _SleAutoResetMemoryleakControlMemThreshold_Type()
)
sleAutoResetMemoryleakControlMemThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlMemThreshold.setStatus("current")
_SleAutoResetMemoryleakControlCheckInterval_Type = Integer32
_SleAutoResetMemoryleakControlCheckInterval_Object = MibScalar
sleAutoResetMemoryleakControlCheckInterval = _SleAutoResetMemoryleakControlCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 8),
    _SleAutoResetMemoryleakControlCheckInterval_Type()
)
sleAutoResetMemoryleakControlCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlCheckInterval.setStatus("current")
_SleAutoResetMemoryleakControlNumberOfVerification_Type = Integer32
_SleAutoResetMemoryleakControlNumberOfVerification_Object = MibScalar
sleAutoResetMemoryleakControlNumberOfVerification = _SleAutoResetMemoryleakControlNumberOfVerification_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 9),
    _SleAutoResetMemoryleakControlNumberOfVerification_Type()
)
sleAutoResetMemoryleakControlNumberOfVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlNumberOfVerification.setStatus("current")
_SleAutoResetMemoryleakControlVerificationInterval_Type = Integer32
_SleAutoResetMemoryleakControlVerificationInterval_Object = MibScalar
sleAutoResetMemoryleakControlVerificationInterval = _SleAutoResetMemoryleakControlVerificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 10),
    _SleAutoResetMemoryleakControlVerificationInterval_Type()
)
sleAutoResetMemoryleakControlVerificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlVerificationInterval.setStatus("current")
_SleAutoResetMemoryleakControlCountThreshold_Type = Integer32
_SleAutoResetMemoryleakControlCountThreshold_Object = MibScalar
sleAutoResetMemoryleakControlCountThreshold = _SleAutoResetMemoryleakControlCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 11),
    _SleAutoResetMemoryleakControlCountThreshold_Type()
)
sleAutoResetMemoryleakControlCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlCountThreshold.setStatus("current")


class _SleAutoResetMemoryleakControlReboottimeStartHour_Type(Integer32):
    """Custom type sleAutoResetMemoryleakControlReboottimeStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_SleAutoResetMemoryleakControlReboottimeStartHour_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakControlReboottimeStartHour_Object = MibScalar
sleAutoResetMemoryleakControlReboottimeStartHour = _SleAutoResetMemoryleakControlReboottimeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 12),
    _SleAutoResetMemoryleakControlReboottimeStartHour_Type()
)
sleAutoResetMemoryleakControlReboottimeStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlReboottimeStartHour.setStatus("current")


class _SleAutoResetMemoryleakControlReboottimeStartMin_Type(Integer32):
    """Custom type sleAutoResetMemoryleakControlReboottimeStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 59),
    )


_SleAutoResetMemoryleakControlReboottimeStartMin_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakControlReboottimeStartMin_Object = MibScalar
sleAutoResetMemoryleakControlReboottimeStartMin = _SleAutoResetMemoryleakControlReboottimeStartMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 13),
    _SleAutoResetMemoryleakControlReboottimeStartMin_Type()
)
sleAutoResetMemoryleakControlReboottimeStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlReboottimeStartMin.setStatus("current")


class _SleAutoResetMemoryleakControlReboottimeEndHour_Type(Integer32):
    """Custom type sleAutoResetMemoryleakControlReboottimeEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_SleAutoResetMemoryleakControlReboottimeEndHour_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakControlReboottimeEndHour_Object = MibScalar
sleAutoResetMemoryleakControlReboottimeEndHour = _SleAutoResetMemoryleakControlReboottimeEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 14),
    _SleAutoResetMemoryleakControlReboottimeEndHour_Type()
)
sleAutoResetMemoryleakControlReboottimeEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlReboottimeEndHour.setStatus("current")


class _SleAutoResetMemoryleakControlReboottimeEndMin_Type(Integer32):
    """Custom type sleAutoResetMemoryleakControlReboottimeEndMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 59),
    )


_SleAutoResetMemoryleakControlReboottimeEndMin_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakControlReboottimeEndMin_Object = MibScalar
sleAutoResetMemoryleakControlReboottimeEndMin = _SleAutoResetMemoryleakControlReboottimeEndMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 15),
    _SleAutoResetMemoryleakControlReboottimeEndMin_Type()
)
sleAutoResetMemoryleakControlReboottimeEndMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlReboottimeEndMin.setStatus("current")


class _SleAutoResetMemoryleakControlRebootThreshold_Type(Integer32):
    """Custom type sleAutoResetMemoryleakControlRebootThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleAutoResetMemoryleakControlRebootThreshold_Type.__name__ = "Integer32"
_SleAutoResetMemoryleakControlRebootThreshold_Object = MibScalar
sleAutoResetMemoryleakControlRebootThreshold = _SleAutoResetMemoryleakControlRebootThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 2, 16),
    _SleAutoResetMemoryleakControlRebootThreshold_Type()
)
sleAutoResetMemoryleakControlRebootThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakControlRebootThreshold.setStatus("current")
_SleAutoResetMemoryleakNotification_ObjectIdentity = ObjectIdentity
sleAutoResetMemoryleakNotification = _SleAutoResetMemoryleakNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 3)
)
_SleAutoResetCpu_ObjectIdentity = ObjectIdentity
sleAutoResetCpu = _SleAutoResetCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3)
)
_SleAutoResetCpuInfo_ObjectIdentity = ObjectIdentity
sleAutoResetCpuInfo = _SleAutoResetCpuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 1)
)


class _SleAutoResetCpuStatus_Type(Integer32):
    """Custom type sleAutoResetCpuStatus based on Integer32"""
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


_SleAutoResetCpuStatus_Type.__name__ = "Integer32"
_SleAutoResetCpuStatus_Object = MibScalar
sleAutoResetCpuStatus = _SleAutoResetCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 1, 1),
    _SleAutoResetCpuStatus_Type()
)
sleAutoResetCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetCpuStatus.setStatus("current")


class _SleAutoResetCpuLoad_Type(Integer32):
    """Custom type sleAutoResetCpuLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_SleAutoResetCpuLoad_Type.__name__ = "Integer32"
_SleAutoResetCpuLoad_Object = MibScalar
sleAutoResetCpuLoad = _SleAutoResetCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 1, 2),
    _SleAutoResetCpuLoad_Type()
)
sleAutoResetCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetCpuLoad.setStatus("current")


class _SleAutoResetCpuInterruptLoad_Type(Integer32):
    """Custom type sleAutoResetCpuInterruptLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleAutoResetCpuInterruptLoad_Type.__name__ = "Integer32"
_SleAutoResetCpuInterruptLoad_Object = MibScalar
sleAutoResetCpuInterruptLoad = _SleAutoResetCpuInterruptLoad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 1, 3),
    _SleAutoResetCpuInterruptLoad_Type()
)
sleAutoResetCpuInterruptLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetCpuInterruptLoad.setStatus("current")
_SleAutoResetCpuTime_Type = Integer32
_SleAutoResetCpuTime_Object = MibScalar
sleAutoResetCpuTime = _SleAutoResetCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 1, 4),
    _SleAutoResetCpuTime_Type()
)
sleAutoResetCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetCpuTime.setStatus("current")
_SleAutoResetCpuControl_ObjectIdentity = ObjectIdentity
sleAutoResetCpuControl = _SleAutoResetCpuControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2)
)


class _SleAutoResetCpuControlRequest_Type(Integer32):
    """Custom type sleAutoResetCpuControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setAutoResetCpu", 1),
          ("delAutoResetCpu", 2))
    )


_SleAutoResetCpuControlRequest_Type.__name__ = "Integer32"
_SleAutoResetCpuControlRequest_Object = MibScalar
sleAutoResetCpuControlRequest = _SleAutoResetCpuControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2, 1),
    _SleAutoResetCpuControlRequest_Type()
)
sleAutoResetCpuControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetCpuControlRequest.setStatus("current")
_SleAutoResetCpuControlStatus_Type = SleControlStatusType
_SleAutoResetCpuControlStatus_Object = MibScalar
sleAutoResetCpuControlStatus = _SleAutoResetCpuControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2, 2),
    _SleAutoResetCpuControlStatus_Type()
)
sleAutoResetCpuControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetCpuControlStatus.setStatus("current")
_SleAutoResetCpuControlTimer_Type = Gauge32
_SleAutoResetCpuControlTimer_Object = MibScalar
sleAutoResetCpuControlTimer = _SleAutoResetCpuControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2, 3),
    _SleAutoResetCpuControlTimer_Type()
)
sleAutoResetCpuControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetCpuControlTimer.setStatus("current")
_SleAutoResetCpuControlTimeStamp_Type = TimeTicks
_SleAutoResetCpuControlTimeStamp_Object = MibScalar
sleAutoResetCpuControlTimeStamp = _SleAutoResetCpuControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2, 4),
    _SleAutoResetCpuControlTimeStamp_Type()
)
sleAutoResetCpuControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetCpuControlTimeStamp.setStatus("current")
_SleAutoResetCpuControlReqResult_Type = SleControlRequestResultType
_SleAutoResetCpuControlReqResult_Object = MibScalar
sleAutoResetCpuControlReqResult = _SleAutoResetCpuControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2, 5),
    _SleAutoResetCpuControlReqResult_Type()
)
sleAutoResetCpuControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetCpuControlReqResult.setStatus("current")


class _SleAutoResetCpuControlLoad_Type(Integer32):
    """Custom type sleAutoResetCpuControlLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_SleAutoResetCpuControlLoad_Type.__name__ = "Integer32"
_SleAutoResetCpuControlLoad_Object = MibScalar
sleAutoResetCpuControlLoad = _SleAutoResetCpuControlLoad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2, 6),
    _SleAutoResetCpuControlLoad_Type()
)
sleAutoResetCpuControlLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetCpuControlLoad.setStatus("current")


class _SleAutoResetCpuControlInterruptLoad_Type(Integer32):
    """Custom type sleAutoResetCpuControlInterruptLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleAutoResetCpuControlInterruptLoad_Type.__name__ = "Integer32"
_SleAutoResetCpuControlInterruptLoad_Object = MibScalar
sleAutoResetCpuControlInterruptLoad = _SleAutoResetCpuControlInterruptLoad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2, 7),
    _SleAutoResetCpuControlInterruptLoad_Type()
)
sleAutoResetCpuControlInterruptLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetCpuControlInterruptLoad.setStatus("current")
_SleAutoResetCpuControlTime_Type = Integer32
_SleAutoResetCpuControlTime_Object = MibScalar
sleAutoResetCpuControlTime = _SleAutoResetCpuControlTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 2, 8),
    _SleAutoResetCpuControlTime_Type()
)
sleAutoResetCpuControlTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoResetCpuControlTime.setStatus("current")
_SleAutoResetCpuNotification_ObjectIdentity = ObjectIdentity
sleAutoResetCpuNotification = _SleAutoResetCpuNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 3)
)
_SleAutoResetInfo_ObjectIdentity = ObjectIdentity
sleAutoResetInfo = _SleAutoResetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 4)
)
_SleAutoResetBootReason_Type = OctetString
_SleAutoResetBootReason_Object = MibScalar
sleAutoResetBootReason = _SleAutoResetBootReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 4, 1),
    _SleAutoResetBootReason_Type()
)
sleAutoResetBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoResetBootReason.setStatus("current")
_SleCoreDump_ObjectIdentity = ObjectIdentity
sleCoreDump = _SleCoreDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13)
)
_SleCoreDumpInfoTable_Object = MibTable
sleCoreDumpInfoTable = _SleCoreDumpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 1)
)
if mibBuilder.loadTexts:
    sleCoreDumpInfoTable.setStatus("current")
_SleCoreDumpInfoEntry_Object = MibTableRow
sleCoreDumpInfoEntry = _SleCoreDumpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 1, 1)
)
sleCoreDumpInfoEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpInfoPID"),
)
if mibBuilder.loadTexts:
    sleCoreDumpInfoEntry.setStatus("current")


class _SleCoreDumpInfoPID_Type(Integer32):
    """Custom type sleCoreDumpInfoPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleCoreDumpInfoPID_Type.__name__ = "Integer32"
_SleCoreDumpInfoPID_Object = MibTableColumn
sleCoreDumpInfoPID = _SleCoreDumpInfoPID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 1, 1, 1),
    _SleCoreDumpInfoPID_Type()
)
sleCoreDumpInfoPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCoreDumpInfoPID.setStatus("current")


class _SleCoreDumpInfoStatus_Type(Integer32):
    """Custom type sleCoreDumpInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fail", 2))
    )


_SleCoreDumpInfoStatus_Type.__name__ = "Integer32"
_SleCoreDumpInfoStatus_Object = MibTableColumn
sleCoreDumpInfoStatus = _SleCoreDumpInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 1, 1, 2),
    _SleCoreDumpInfoStatus_Type()
)
sleCoreDumpInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCoreDumpInfoStatus.setStatus("current")
_SleCoreDumpFile_Type = OctetString
_SleCoreDumpFile_Object = MibTableColumn
sleCoreDumpFile = _SleCoreDumpFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 1, 1, 3),
    _SleCoreDumpFile_Type()
)
sleCoreDumpFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCoreDumpFile.setStatus("current")
_SleCoreDumpControl_ObjectIdentity = ObjectIdentity
sleCoreDumpControl = _SleCoreDumpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2)
)


class _SleCoreDumpControlRequest_Type(Integer32):
    """Custom type sleCoreDumpControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createCoredDumpEntry", 1),
          ("destroyCoredDumpEntry", 2),
          ("setCoredDumpEntryToRemote", 3))
    )


_SleCoreDumpControlRequest_Type.__name__ = "Integer32"
_SleCoreDumpControlRequest_Object = MibScalar
sleCoreDumpControlRequest = _SleCoreDumpControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 1),
    _SleCoreDumpControlRequest_Type()
)
sleCoreDumpControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCoreDumpControlRequest.setStatus("current")
_SleCoreDumpControlStatus_Type = SleControlStatusType
_SleCoreDumpControlStatus_Object = MibScalar
sleCoreDumpControlStatus = _SleCoreDumpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 2),
    _SleCoreDumpControlStatus_Type()
)
sleCoreDumpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCoreDumpControlStatus.setStatus("current")
_SleCoreDumpControlTimer_Type = Gauge32
_SleCoreDumpControlTimer_Object = MibScalar
sleCoreDumpControlTimer = _SleCoreDumpControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 3),
    _SleCoreDumpControlTimer_Type()
)
sleCoreDumpControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCoreDumpControlTimer.setStatus("current")
_SleCoreDumpControlTimeStamp_Type = TimeTicks
_SleCoreDumpControlTimeStamp_Object = MibScalar
sleCoreDumpControlTimeStamp = _SleCoreDumpControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 4),
    _SleCoreDumpControlTimeStamp_Type()
)
sleCoreDumpControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCoreDumpControlTimeStamp.setStatus("current")
_SleCoreDumpControlReqResult_Type = SleControlRequestResultType
_SleCoreDumpControlReqResult_Object = MibScalar
sleCoreDumpControlReqResult = _SleCoreDumpControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 5),
    _SleCoreDumpControlReqResult_Type()
)
sleCoreDumpControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleCoreDumpControlReqResult.setStatus("current")


class _SleCoreDumpControlPID_Type(Integer32):
    """Custom type sleCoreDumpControlPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleCoreDumpControlPID_Type.__name__ = "Integer32"
_SleCoreDumpControlPID_Object = MibScalar
sleCoreDumpControlPID = _SleCoreDumpControlPID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 6),
    _SleCoreDumpControlPID_Type()
)
sleCoreDumpControlPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCoreDumpControlPID.setStatus("current")
_SleCoreDumpControlServerIP_Type = IpAddress
_SleCoreDumpControlServerIP_Object = MibScalar
sleCoreDumpControlServerIP = _SleCoreDumpControlServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 7),
    _SleCoreDumpControlServerIP_Type()
)
sleCoreDumpControlServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCoreDumpControlServerIP.setStatus("current")
_SleCoreDumpControlUserID_Type = OctetString
_SleCoreDumpControlUserID_Object = MibScalar
sleCoreDumpControlUserID = _SleCoreDumpControlUserID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 8),
    _SleCoreDumpControlUserID_Type()
)
sleCoreDumpControlUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCoreDumpControlUserID.setStatus("current")
_SleCoreDumpControlPassword_Type = OctetString
_SleCoreDumpControlPassword_Object = MibScalar
sleCoreDumpControlPassword = _SleCoreDumpControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 9),
    _SleCoreDumpControlPassword_Type()
)
sleCoreDumpControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCoreDumpControlPassword.setStatus("current")
_SleCoreDumpControlCoredumpFile_Type = OctetString
_SleCoreDumpControlCoredumpFile_Object = MibScalar
sleCoreDumpControlCoredumpFile = _SleCoreDumpControlCoredumpFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 2, 10),
    _SleCoreDumpControlCoredumpFile_Type()
)
sleCoreDumpControlCoredumpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleCoreDumpControlCoredumpFile.setStatus("current")
_SleCoreDumpNotification_ObjectIdentity = ObjectIdentity
sleCoreDumpNotification = _SleCoreDumpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 3)
)
_SleService_ObjectIdentity = ObjectIdentity
sleService = _SleService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14)
)
_SleServiceTable_Object = MibTable
sleServiceTable = _SleServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 1)
)
if mibBuilder.loadTexts:
    sleServiceTable.setStatus("current")
_SleServiceEntry_Object = MibTableRow
sleServiceEntry = _SleServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 1, 1)
)
sleServiceEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleServiceIndex"),
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleServiceProtocol"),
)
if mibBuilder.loadTexts:
    sleServiceEntry.setStatus("current")


class _SleServiceIndex_Type(Integer32):
    """Custom type sleServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(20,
              21,
              22,
              23,
              69,
              161)
        )
    )
    namedValues = NamedValues(
        *(("ftpdata", 20),
          ("ftp", 21),
          ("ssh", 22),
          ("telnet", 23),
          ("tftp", 69),
          ("snmp", 161))
    )


_SleServiceIndex_Type.__name__ = "Integer32"
_SleServiceIndex_Object = MibTableColumn
sleServiceIndex = _SleServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 1, 1, 1),
    _SleServiceIndex_Type()
)
sleServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleServiceIndex.setStatus("current")


class _SleServiceProtocol_Type(Integer32):
    """Custom type sleServiceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_SleServiceProtocol_Type.__name__ = "Integer32"
_SleServiceProtocol_Object = MibTableColumn
sleServiceProtocol = _SleServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 1, 1, 2),
    _SleServiceProtocol_Type()
)
sleServiceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleServiceProtocol.setStatus("current")
_SleServiceName_Type = OctetString
_SleServiceName_Object = MibTableColumn
sleServiceName = _SleServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 1, 1, 3),
    _SleServiceName_Type()
)
sleServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleServiceName.setStatus("current")


class _SleServicePort_Type(Integer32):
    """Custom type sleServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleServicePort_Type.__name__ = "Integer32"
_SleServicePort_Object = MibTableColumn
sleServicePort = _SleServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 1, 1, 4),
    _SleServicePort_Type()
)
sleServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleServicePort.setStatus("current")


class _SleServiceAdminStatus_Type(Integer32):
    """Custom type sleServiceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleServiceAdminStatus_Type.__name__ = "Integer32"
_SleServiceAdminStatus_Object = MibTableColumn
sleServiceAdminStatus = _SleServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 1, 1, 5),
    _SleServiceAdminStatus_Type()
)
sleServiceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleServiceAdminStatus.setStatus("current")
_SleServiceControl_ObjectIdentity = ObjectIdentity
sleServiceControl = _SleServiceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2)
)


class _SleServiceControlRequest_Type(Integer32):
    """Custom type sleServiceControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setServicePort", 1),
          ("setServiceStatus", 2))
    )


_SleServiceControlRequest_Type.__name__ = "Integer32"
_SleServiceControlRequest_Object = MibScalar
sleServiceControlRequest = _SleServiceControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 1),
    _SleServiceControlRequest_Type()
)
sleServiceControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleServiceControlRequest.setStatus("current")
_SleServiceControlStatus_Type = SleControlStatusType
_SleServiceControlStatus_Object = MibScalar
sleServiceControlStatus = _SleServiceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 2),
    _SleServiceControlStatus_Type()
)
sleServiceControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleServiceControlStatus.setStatus("current")
_SleServiceControlTimer_Type = Gauge32
_SleServiceControlTimer_Object = MibScalar
sleServiceControlTimer = _SleServiceControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 3),
    _SleServiceControlTimer_Type()
)
sleServiceControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleServiceControlTimer.setStatus("current")
_SleServiceControlTimeStamp_Type = TimeTicks
_SleServiceControlTimeStamp_Object = MibScalar
sleServiceControlTimeStamp = _SleServiceControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 4),
    _SleServiceControlTimeStamp_Type()
)
sleServiceControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleServiceControlTimeStamp.setStatus("current")
_SleServiceControlReqResult_Type = SleControlRequestResultType
_SleServiceControlReqResult_Object = MibScalar
sleServiceControlReqResult = _SleServiceControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 5),
    _SleServiceControlReqResult_Type()
)
sleServiceControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleServiceControlReqResult.setStatus("current")


class _SleServiceControlIndex_Type(Integer32):
    """Custom type sleServiceControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(20,
              21,
              22,
              23,
              69,
              161)
        )
    )
    namedValues = NamedValues(
        *(("ftpdata", 20),
          ("ftp", 21),
          ("ssh", 22),
          ("telnet", 23),
          ("tftp", 69),
          ("snmp", 161))
    )


_SleServiceControlIndex_Type.__name__ = "Integer32"
_SleServiceControlIndex_Object = MibScalar
sleServiceControlIndex = _SleServiceControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 6),
    _SleServiceControlIndex_Type()
)
sleServiceControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleServiceControlIndex.setStatus("current")


class _SleServiceControlProtocol_Type(Integer32):
    """Custom type sleServiceControlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_SleServiceControlProtocol_Type.__name__ = "Integer32"
_SleServiceControlProtocol_Object = MibScalar
sleServiceControlProtocol = _SleServiceControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 7),
    _SleServiceControlProtocol_Type()
)
sleServiceControlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleServiceControlProtocol.setStatus("current")


class _SleServiceControlPort_Type(Integer32):
    """Custom type sleServiceControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleServiceControlPort_Type.__name__ = "Integer32"
_SleServiceControlPort_Object = MibScalar
sleServiceControlPort = _SleServiceControlPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 8),
    _SleServiceControlPort_Type()
)
sleServiceControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleServiceControlPort.setStatus("current")


class _SleServiceControlAdminStatus_Type(Integer32):
    """Custom type sleServiceControlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleServiceControlAdminStatus_Type.__name__ = "Integer32"
_SleServiceControlAdminStatus_Object = MibScalar
sleServiceControlAdminStatus = _SleServiceControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 2, 9),
    _SleServiceControlAdminStatus_Type()
)
sleServiceControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleServiceControlAdminStatus.setStatus("current")
_SleServiceNotification_ObjectIdentity = ObjectIdentity
sleServiceNotification = _SleServiceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 3)
)
_SleSystemUser_ObjectIdentity = ObjectIdentity
sleSystemUser = _SleSystemUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15)
)
_SleSystemUserTable_Object = MibTable
sleSystemUserTable = _SleSystemUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 1)
)
if mibBuilder.loadTexts:
    sleSystemUserTable.setStatus("current")
_SleSystemUserEntry_Object = MibTableRow
sleSystemUserEntry = _SleSystemUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 1, 1)
)
sleSystemUserEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserName"),
)
if mibBuilder.loadTexts:
    sleSystemUserEntry.setStatus("current")


class _SleSystemUserName_Type(OctetString):
    """Custom type sleSystemUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleSystemUserName_Type.__name__ = "OctetString"
_SleSystemUserName_Object = MibTableColumn
sleSystemUserName = _SleSystemUserName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 1, 1, 1),
    _SleSystemUserName_Type()
)
sleSystemUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserName.setStatus("current")


class _SleSystemUserLevel_Type(Integer32):
    """Custom type sleSystemUserLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SleSystemUserLevel_Type.__name__ = "Integer32"
_SleSystemUserLevel_Object = MibTableColumn
sleSystemUserLevel = _SleSystemUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 1, 1, 2),
    _SleSystemUserLevel_Type()
)
sleSystemUserLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserLevel.setStatus("current")


class _SleSystemUserPassword_Type(OctetString):
    """Custom type sleSystemUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleSystemUserPassword_Type.__name__ = "OctetString"
_SleSystemUserPassword_Object = MibTableColumn
sleSystemUserPassword = _SleSystemUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 1, 1, 3),
    _SleSystemUserPassword_Type()
)
sleSystemUserPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserPassword.setStatus("current")


class _SleSystemUserDesc_Type(OctetString):
    """Custom type sleSystemUserDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleSystemUserDesc_Type.__name__ = "OctetString"
_SleSystemUserDesc_Object = MibTableColumn
sleSystemUserDesc = _SleSystemUserDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 1, 1, 4),
    _SleSystemUserDesc_Type()
)
sleSystemUserDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserDesc.setStatus("current")


class _SleSystemUserLoginFailureCount_Type(Integer32):
    """Custom type sleSystemUserLoginFailureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SleSystemUserLoginFailureCount_Type.__name__ = "Integer32"
_SleSystemUserLoginFailureCount_Object = MibTableColumn
sleSystemUserLoginFailureCount = _SleSystemUserLoginFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 1, 1, 5),
    _SleSystemUserLoginFailureCount_Type()
)
sleSystemUserLoginFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserLoginFailureCount.setStatus("current")
_SleSystemUserLoginLastFailureTime_Type = OctetString
_SleSystemUserLoginLastFailureTime_Object = MibTableColumn
sleSystemUserLoginLastFailureTime = _SleSystemUserLoginLastFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 1, 1, 6),
    _SleSystemUserLoginLastFailureTime_Type()
)
sleSystemUserLoginLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserLoginLastFailureTime.setStatus("current")
_SleSystemUserControl_ObjectIdentity = ObjectIdentity
sleSystemUserControl = _SleSystemUserControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2)
)


class _SleSystemUserControlRequest_Type(Integer32):
    """Custom type sleSystemUserControlRequest based on Integer32"""
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
        *(("addUser", 1),
          ("renameUser", 2),
          ("setPassword", 3),
          ("deleteUser", 4),
          ("setLevel", 5),
          ("clearLoginAttemptsLog", 6))
    )


_SleSystemUserControlRequest_Type.__name__ = "Integer32"
_SleSystemUserControlRequest_Object = MibScalar
sleSystemUserControlRequest = _SleSystemUserControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 1),
    _SleSystemUserControlRequest_Type()
)
sleSystemUserControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUserControlRequest.setStatus("current")
_SleSystemUserControlStatus_Type = SleControlStatusType
_SleSystemUserControlStatus_Object = MibScalar
sleSystemUserControlStatus = _SleSystemUserControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 2),
    _SleSystemUserControlStatus_Type()
)
sleSystemUserControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserControlStatus.setStatus("current")
_SleSystemUserControlTimer_Type = Gauge32
_SleSystemUserControlTimer_Object = MibScalar
sleSystemUserControlTimer = _SleSystemUserControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 3),
    _SleSystemUserControlTimer_Type()
)
sleSystemUserControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUserControlTimer.setStatus("current")
_SleSystemUserControlTimeStamp_Type = TimeTicks
_SleSystemUserControlTimeStamp_Object = MibScalar
sleSystemUserControlTimeStamp = _SleSystemUserControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 4),
    _SleSystemUserControlTimeStamp_Type()
)
sleSystemUserControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserControlTimeStamp.setStatus("current")
_SleSystemUserControlReqResult_Type = SleControlRequestResultType
_SleSystemUserControlReqResult_Object = MibScalar
sleSystemUserControlReqResult = _SleSystemUserControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 5),
    _SleSystemUserControlReqResult_Type()
)
sleSystemUserControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemUserControlReqResult.setStatus("current")


class _SleSystemUserControlName_Type(OctetString):
    """Custom type sleSystemUserControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleSystemUserControlName_Type.__name__ = "OctetString"
_SleSystemUserControlName_Object = MibScalar
sleSystemUserControlName = _SleSystemUserControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 6),
    _SleSystemUserControlName_Type()
)
sleSystemUserControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUserControlName.setStatus("current")


class _SleSystemUserControlRename_Type(OctetString):
    """Custom type sleSystemUserControlRename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleSystemUserControlRename_Type.__name__ = "OctetString"
_SleSystemUserControlRename_Object = MibScalar
sleSystemUserControlRename = _SleSystemUserControlRename_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 7),
    _SleSystemUserControlRename_Type()
)
sleSystemUserControlRename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUserControlRename.setStatus("current")


class _SleSystemUserControlLevel_Type(Integer32):
    """Custom type sleSystemUserControlLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SleSystemUserControlLevel_Type.__name__ = "Integer32"
_SleSystemUserControlLevel_Object = MibScalar
sleSystemUserControlLevel = _SleSystemUserControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 8),
    _SleSystemUserControlLevel_Type()
)
sleSystemUserControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUserControlLevel.setStatus("current")


class _SleSystemUserControlPwType_Type(Integer32):
    """Custom type sleSystemUserControlPwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plain", 1),
          ("encrypt", 2))
    )


_SleSystemUserControlPwType_Type.__name__ = "Integer32"
_SleSystemUserControlPwType_Object = MibScalar
sleSystemUserControlPwType = _SleSystemUserControlPwType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 9),
    _SleSystemUserControlPwType_Type()
)
sleSystemUserControlPwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUserControlPwType.setStatus("current")


class _SleSystemUserControlPassword_Type(OctetString):
    """Custom type sleSystemUserControlPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleSystemUserControlPassword_Type.__name__ = "OctetString"
_SleSystemUserControlPassword_Object = MibScalar
sleSystemUserControlPassword = _SleSystemUserControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 10),
    _SleSystemUserControlPassword_Type()
)
sleSystemUserControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUserControlPassword.setStatus("current")


class _SleSystemUserControlDesc_Type(OctetString):
    """Custom type sleSystemUserControlDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleSystemUserControlDesc_Type.__name__ = "OctetString"
_SleSystemUserControlDesc_Object = MibScalar
sleSystemUserControlDesc = _SleSystemUserControlDesc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 2, 11),
    _SleSystemUserControlDesc_Type()
)
sleSystemUserControlDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSystemUserControlDesc.setStatus("current")
_SleSystemUserNotification_ObjectIdentity = ObjectIdentity
sleSystemUserNotification = _SleSystemUserNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 3)
)
_SleParameter_ObjectIdentity = ObjectIdentity
sleParameter = _SleParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16)
)
_SleParameterTable_Object = MibTable
sleParameterTable = _SleParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 1)
)
if mibBuilder.loadTexts:
    sleParameterTable.setStatus("current")
_SleParameterEntry_Object = MibTableRow
sleParameterEntry = _SleParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 1, 1)
)
sleParameterEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleParameterName"),
)
if mibBuilder.loadTexts:
    sleParameterEntry.setStatus("current")


class _SleParameterName_Type(OctetString):
    """Custom type sleParameterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleParameterName_Type.__name__ = "OctetString"
_SleParameterName_Object = MibTableColumn
sleParameterName = _SleParameterName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 1, 1, 1),
    _SleParameterName_Type()
)
sleParameterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleParameterName.setStatus("current")


class _SleParameterValue_Type(OctetString):
    """Custom type sleParameterValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleParameterValue_Type.__name__ = "OctetString"
_SleParameterValue_Object = MibTableColumn
sleParameterValue = _SleParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 1, 1, 2),
    _SleParameterValue_Type()
)
sleParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleParameterValue.setStatus("current")


class _SleParameterMode_Type(Integer32):
    """Custom type sleParameterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_SleParameterMode_Type.__name__ = "Integer32"
_SleParameterMode_Object = MibTableColumn
sleParameterMode = _SleParameterMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 1, 1, 3),
    _SleParameterMode_Type()
)
sleParameterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleParameterMode.setStatus("current")
_SleParameterControl_ObjectIdentity = ObjectIdentity
sleParameterControl = _SleParameterControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2)
)


class _SleParameterControlRequest_Type(Integer32):
    """Custom type sleParameterControlRequest based on Integer32"""
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
        *(("createParameter", 1),
          ("destroyParameter", 2),
          ("modifyParameterMode", 3),
          ("modifyParameterValue", 4))
    )


_SleParameterControlRequest_Type.__name__ = "Integer32"
_SleParameterControlRequest_Object = MibScalar
sleParameterControlRequest = _SleParameterControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2, 1),
    _SleParameterControlRequest_Type()
)
sleParameterControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleParameterControlRequest.setStatus("current")
_SleParameterControlStatus_Type = SleControlStatusType
_SleParameterControlStatus_Object = MibScalar
sleParameterControlStatus = _SleParameterControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2, 2),
    _SleParameterControlStatus_Type()
)
sleParameterControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleParameterControlStatus.setStatus("current")
_SleParameterControlTimer_Type = Gauge32
_SleParameterControlTimer_Object = MibScalar
sleParameterControlTimer = _SleParameterControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2, 3),
    _SleParameterControlTimer_Type()
)
sleParameterControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleParameterControlTimer.setStatus("current")
_SleParameterControlTimeStamp_Type = TimeTicks
_SleParameterControlTimeStamp_Object = MibScalar
sleParameterControlTimeStamp = _SleParameterControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2, 4),
    _SleParameterControlTimeStamp_Type()
)
sleParameterControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleParameterControlTimeStamp.setStatus("current")
_SleParameterControlReqResult_Type = SleControlRequestResultType
_SleParameterControlReqResult_Object = MibScalar
sleParameterControlReqResult = _SleParameterControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2, 5),
    _SleParameterControlReqResult_Type()
)
sleParameterControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleParameterControlReqResult.setStatus("current")


class _SleParameterControlName_Type(OctetString):
    """Custom type sleParameterControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SleParameterControlName_Type.__name__ = "OctetString"
_SleParameterControlName_Object = MibScalar
sleParameterControlName = _SleParameterControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2, 6),
    _SleParameterControlName_Type()
)
sleParameterControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleParameterControlName.setStatus("current")


class _SleParameterControlValue_Type(OctetString):
    """Custom type sleParameterControlValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SleParameterControlValue_Type.__name__ = "OctetString"
_SleParameterControlValue_Object = MibScalar
sleParameterControlValue = _SleParameterControlValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2, 7),
    _SleParameterControlValue_Type()
)
sleParameterControlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleParameterControlValue.setStatus("current")


class _SleParameterControlMode_Type(Integer32):
    """Custom type sleParameterControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_SleParameterControlMode_Type.__name__ = "Integer32"
_SleParameterControlMode_Object = MibScalar
sleParameterControlMode = _SleParameterControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 2, 8),
    _SleParameterControlMode_Type()
)
sleParameterControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleParameterControlMode.setStatus("current")
_SleParameterNotification_ObjectIdentity = ObjectIdentity
sleParameterNotification = _SleParameterNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 3)
)
_SleSwWatchdogBase_ObjectIdentity = ObjectIdentity
sleSwWatchdogBase = _SleSwWatchdogBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17)
)
_SleSwWatchdogTable_Object = MibTable
sleSwWatchdogTable = _SleSwWatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 1)
)
if mibBuilder.loadTexts:
    sleSwWatchdogTable.setStatus("current")
_SleSwWatchdogEntry_Object = MibTableRow
sleSwWatchdogEntry = _SleSwWatchdogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 1, 1)
)
sleSwWatchdogEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogType"),
)
if mibBuilder.loadTexts:
    sleSwWatchdogEntry.setStatus("current")


class _SleSwWatchdogType_Type(Integer32):
    """Custom type sleSwWatchdogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daemonMonitoring", 1),
          ("inetMonitoring", 2),
          ("ponMonitoring", 3))
    )


_SleSwWatchdogType_Type.__name__ = "Integer32"
_SleSwWatchdogType_Object = MibTableColumn
sleSwWatchdogType = _SleSwWatchdogType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 1, 1, 1),
    _SleSwWatchdogType_Type()
)
sleSwWatchdogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSwWatchdogType.setStatus("current")


class _SleSwWatchdogInterval_Type(Integer32):
    """Custom type sleSwWatchdogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_SleSwWatchdogInterval_Type.__name__ = "Integer32"
_SleSwWatchdogInterval_Object = MibTableColumn
sleSwWatchdogInterval = _SleSwWatchdogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 1, 1, 2),
    _SleSwWatchdogInterval_Type()
)
sleSwWatchdogInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSwWatchdogInterval.setStatus("current")
if mibBuilder.loadTexts:
    sleSwWatchdogInterval.setUnits("sec")


class _SleSwWatchdogThreshold_Type(Integer32):
    """Custom type sleSwWatchdogThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SleSwWatchdogThreshold_Type.__name__ = "Integer32"
_SleSwWatchdogThreshold_Object = MibTableColumn
sleSwWatchdogThreshold = _SleSwWatchdogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 1, 1, 3),
    _SleSwWatchdogThreshold_Type()
)
sleSwWatchdogThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSwWatchdogThreshold.setStatus("current")


class _SleSwWatchdogAction_Type(Integer32):
    """Custom type sleSwWatchdogAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("daemonRestart", 2),
          ("systemReset", 3),
          ("systemResetWithSaveCfg", 4),
          ("onuPortReset", 5))
    )


_SleSwWatchdogAction_Type.__name__ = "Integer32"
_SleSwWatchdogAction_Object = MibTableColumn
sleSwWatchdogAction = _SleSwWatchdogAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 1, 1, 4),
    _SleSwWatchdogAction_Type()
)
sleSwWatchdogAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSwWatchdogAction.setStatus("current")
_SleSwWatchdogErrcnt_Type = Integer32
_SleSwWatchdogErrcnt_Object = MibTableColumn
sleSwWatchdogErrcnt = _SleSwWatchdogErrcnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 1, 1, 5),
    _SleSwWatchdogErrcnt_Type()
)
sleSwWatchdogErrcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSwWatchdogErrcnt.setStatus("current")
_SleSwWatchdogControl_ObjectIdentity = ObjectIdentity
sleSwWatchdogControl = _SleSwWatchdogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2)
)


class _SleSwWatchdogControlRequest_Type(Integer32):
    """Custom type sleSwWatchdogControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createSwwatchdog", 1),
          ("deleteSwwatchdog", 2))
    )


_SleSwWatchdogControlRequest_Type.__name__ = "Integer32"
_SleSwWatchdogControlRequest_Object = MibScalar
sleSwWatchdogControlRequest = _SleSwWatchdogControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 1),
    _SleSwWatchdogControlRequest_Type()
)
sleSwWatchdogControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSwWatchdogControlRequest.setStatus("current")
_SleSwWatchdogControlStatus_Type = SleControlStatusType
_SleSwWatchdogControlStatus_Object = MibScalar
sleSwWatchdogControlStatus = _SleSwWatchdogControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 2),
    _SleSwWatchdogControlStatus_Type()
)
sleSwWatchdogControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSwWatchdogControlStatus.setStatus("current")
_SleSwWatchdogControlTimer_Type = Gauge32
_SleSwWatchdogControlTimer_Object = MibScalar
sleSwWatchdogControlTimer = _SleSwWatchdogControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 3),
    _SleSwWatchdogControlTimer_Type()
)
sleSwWatchdogControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSwWatchdogControlTimer.setStatus("current")
_SleSwWatchdogControlTimeStamp_Type = TimeTicks
_SleSwWatchdogControlTimeStamp_Object = MibScalar
sleSwWatchdogControlTimeStamp = _SleSwWatchdogControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 4),
    _SleSwWatchdogControlTimeStamp_Type()
)
sleSwWatchdogControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSwWatchdogControlTimeStamp.setStatus("current")
_SleSwWatchdogControlReqResult_Type = SleControlRequestResultType
_SleSwWatchdogControlReqResult_Object = MibScalar
sleSwWatchdogControlReqResult = _SleSwWatchdogControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 5),
    _SleSwWatchdogControlReqResult_Type()
)
sleSwWatchdogControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSwWatchdogControlReqResult.setStatus("current")


class _SleSwWatchdogControlType_Type(Integer32):
    """Custom type sleSwWatchdogControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daemonMonitoring", 1),
          ("inetMonitoring", 2),
          ("ponMonitoring", 3))
    )


_SleSwWatchdogControlType_Type.__name__ = "Integer32"
_SleSwWatchdogControlType_Object = MibScalar
sleSwWatchdogControlType = _SleSwWatchdogControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 6),
    _SleSwWatchdogControlType_Type()
)
sleSwWatchdogControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSwWatchdogControlType.setStatus("current")


class _SleSwWatchdogControlInterval_Type(Integer32):
    """Custom type sleSwWatchdogControlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_SleSwWatchdogControlInterval_Type.__name__ = "Integer32"
_SleSwWatchdogControlInterval_Object = MibScalar
sleSwWatchdogControlInterval = _SleSwWatchdogControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 7),
    _SleSwWatchdogControlInterval_Type()
)
sleSwWatchdogControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSwWatchdogControlInterval.setStatus("current")


class _SleSwWatchdogControlThreshold_Type(Integer32):
    """Custom type sleSwWatchdogControlThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SleSwWatchdogControlThreshold_Type.__name__ = "Integer32"
_SleSwWatchdogControlThreshold_Object = MibScalar
sleSwWatchdogControlThreshold = _SleSwWatchdogControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 8),
    _SleSwWatchdogControlThreshold_Type()
)
sleSwWatchdogControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSwWatchdogControlThreshold.setStatus("current")


class _SleSwWatchdogControlAction_Type(Integer32):
    """Custom type sleSwWatchdogControlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("daemonRestart", 2),
          ("systemReset", 3),
          ("systemResetWithSaveCfg", 4),
          ("onuPortReset", 5))
    )


_SleSwWatchdogControlAction_Type.__name__ = "Integer32"
_SleSwWatchdogControlAction_Object = MibScalar
sleSwWatchdogControlAction = _SleSwWatchdogControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 2, 9),
    _SleSwWatchdogControlAction_Type()
)
sleSwWatchdogControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSwWatchdogControlAction.setStatus("current")
_SleSwWatchdogNotification_ObjectIdentity = ObjectIdentity
sleSwWatchdogNotification = _SleSwWatchdogNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 3)
)
_SleAutoUpgrade_ObjectIdentity = ObjectIdentity
sleAutoUpgrade = _SleAutoUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18)
)
_SleAutoUpgradeProfile_ObjectIdentity = ObjectIdentity
sleAutoUpgradeProfile = _SleAutoUpgradeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1)
)
_SleAutoUpgradeProfileTable_Object = MibTable
sleAutoUpgradeProfileTable = _SleAutoUpgradeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileTable.setStatus("current")
_SleAutoUpgradeProfileEntry_Object = MibTableRow
sleAutoUpgradeProfileEntry = _SleAutoUpgradeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1)
)
sleAutoUpgradeProfileEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileIndex"),
)
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileEntry.setStatus("current")


class _SleAutoUpgradeProfileIndex_Type(Integer32):
    """Custom type sleAutoUpgradeProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleAutoUpgradeProfileIndex_Type.__name__ = "Integer32"
_SleAutoUpgradeProfileIndex_Object = MibTableColumn
sleAutoUpgradeProfileIndex = _SleAutoUpgradeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 1),
    _SleAutoUpgradeProfileIndex_Type()
)
sleAutoUpgradeProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileIndex.setStatus("current")
_SleAutoUpgradeProfileName_Type = OctetString
_SleAutoUpgradeProfileName_Object = MibTableColumn
sleAutoUpgradeProfileName = _SleAutoUpgradeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 2),
    _SleAutoUpgradeProfileName_Type()
)
sleAutoUpgradeProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileName.setStatus("current")
_SleAutoUpgradeProfileOldVer_Type = OctetString
_SleAutoUpgradeProfileOldVer_Object = MibTableColumn
sleAutoUpgradeProfileOldVer = _SleAutoUpgradeProfileOldVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 3),
    _SleAutoUpgradeProfileOldVer_Type()
)
sleAutoUpgradeProfileOldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileOldVer.setStatus("current")
_SleAutoUpgradeProfileNewVer_Type = OctetString
_SleAutoUpgradeProfileNewVer_Object = MibTableColumn
sleAutoUpgradeProfileNewVer = _SleAutoUpgradeProfileNewVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 4),
    _SleAutoUpgradeProfileNewVer_Type()
)
sleAutoUpgradeProfileNewVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileNewVer.setStatus("current")
_SleAutoUpgradeProfileSize_Type = Integer32
_SleAutoUpgradeProfileSize_Object = MibTableColumn
sleAutoUpgradeProfileSize = _SleAutoUpgradeProfileSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 5),
    _SleAutoUpgradeProfileSize_Type()
)
sleAutoUpgradeProfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileSize.setStatus("current")


class _SleAutoUpgradeProfilePeriodType_Type(Integer32):
    """Custom type sleAutoUpgradeProfilePeriodType based on Integer32"""
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
        *(("auto", 1),
          ("daily", 2),
          ("weekly", 3),
          ("monthly", 4),
          ("interval", 5),
          ("once", 6))
    )


_SleAutoUpgradeProfilePeriodType_Type.__name__ = "Integer32"
_SleAutoUpgradeProfilePeriodType_Object = MibTableColumn
sleAutoUpgradeProfilePeriodType = _SleAutoUpgradeProfilePeriodType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 6),
    _SleAutoUpgradeProfilePeriodType_Type()
)
sleAutoUpgradeProfilePeriodType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfilePeriodType.setStatus("current")
_SleAutoUpgradeProfileDate_Type = OctetString
_SleAutoUpgradeProfileDate_Object = MibTableColumn
sleAutoUpgradeProfileDate = _SleAutoUpgradeProfileDate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 7),
    _SleAutoUpgradeProfileDate_Type()
)
sleAutoUpgradeProfileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileDate.setStatus("current")
_SleAutoUpgradeProfilePeriodDate_Type = OctetString
_SleAutoUpgradeProfilePeriodDate_Object = MibTableColumn
sleAutoUpgradeProfilePeriodDate = _SleAutoUpgradeProfilePeriodDate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 8),
    _SleAutoUpgradeProfilePeriodDate_Type()
)
sleAutoUpgradeProfilePeriodDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfilePeriodDate.setStatus("current")
_SleAutoUpgradeProfileTimeout_Type = Integer32
_SleAutoUpgradeProfileTimeout_Object = MibTableColumn
sleAutoUpgradeProfileTimeout = _SleAutoUpgradeProfileTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 9),
    _SleAutoUpgradeProfileTimeout_Type()
)
sleAutoUpgradeProfileTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileTimeout.setStatus("current")


class _SleAutoUpgradeProfileRetry_Type(Integer32):
    """Custom type sleAutoUpgradeProfileRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_SleAutoUpgradeProfileRetry_Type.__name__ = "Integer32"
_SleAutoUpgradeProfileRetry_Object = MibTableColumn
sleAutoUpgradeProfileRetry = _SleAutoUpgradeProfileRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 10),
    _SleAutoUpgradeProfileRetry_Type()
)
sleAutoUpgradeProfileRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileRetry.setStatus("current")
_SleAutoUpgradeProfileRegSec_Type = Integer32
_SleAutoUpgradeProfileRegSec_Object = MibTableColumn
sleAutoUpgradeProfileRegSec = _SleAutoUpgradeProfileRegSec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 11),
    _SleAutoUpgradeProfileRegSec_Type()
)
sleAutoUpgradeProfileRegSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileRegSec.setStatus("current")
_SleAutoUpgradeProfileReloadTime_Type = OctetString
_SleAutoUpgradeProfileReloadTime_Object = MibTableColumn
sleAutoUpgradeProfileReloadTime = _SleAutoUpgradeProfileReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 12),
    _SleAutoUpgradeProfileReloadTime_Type()
)
sleAutoUpgradeProfileReloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileReloadTime.setStatus("current")
_SleAutoUpgradeProfileModel_Type = OctetString
_SleAutoUpgradeProfileModel_Object = MibTableColumn
sleAutoUpgradeProfileModel = _SleAutoUpgradeProfileModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 1, 1, 13),
    _SleAutoUpgradeProfileModel_Type()
)
sleAutoUpgradeProfileModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileModel.setStatus("current")
_SleAutoUpgradeProfileControl_ObjectIdentity = ObjectIdentity
sleAutoUpgradeProfileControl = _SleAutoUpgradeProfileControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2)
)


class _SleAutoUpgradeProfileControlRequest_Type(Integer32):
    """Custom type sleAutoUpgradeProfileControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createAutoUpgrdProfile", 1),
          ("destroyAutoUpgrdProfile", 2),
          ("modifyAutoUpgrdProfile", 3))
    )


_SleAutoUpgradeProfileControlRequest_Type.__name__ = "Integer32"
_SleAutoUpgradeProfileControlRequest_Object = MibScalar
sleAutoUpgradeProfileControlRequest = _SleAutoUpgradeProfileControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 1),
    _SleAutoUpgradeProfileControlRequest_Type()
)
sleAutoUpgradeProfileControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlRequest.setStatus("current")
_SleAutoUpgradeProfileControlStatus_Type = SleControlStatusType
_SleAutoUpgradeProfileControlStatus_Object = MibScalar
sleAutoUpgradeProfileControlStatus = _SleAutoUpgradeProfileControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 2),
    _SleAutoUpgradeProfileControlStatus_Type()
)
sleAutoUpgradeProfileControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlStatus.setStatus("current")
_SleAutoUpgradeProfileControlTimer_Type = Gauge32
_SleAutoUpgradeProfileControlTimer_Object = MibScalar
sleAutoUpgradeProfileControlTimer = _SleAutoUpgradeProfileControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 3),
    _SleAutoUpgradeProfileControlTimer_Type()
)
sleAutoUpgradeProfileControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlTimer.setStatus("current")
_SleAutoUpgradeProfileControlTimeStamp_Type = TimeTicks
_SleAutoUpgradeProfileControlTimeStamp_Object = MibScalar
sleAutoUpgradeProfileControlTimeStamp = _SleAutoUpgradeProfileControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 4),
    _SleAutoUpgradeProfileControlTimeStamp_Type()
)
sleAutoUpgradeProfileControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlTimeStamp.setStatus("current")
_SleAutoUpgradeProfileControlReqResult_Type = SleControlRequestResultType
_SleAutoUpgradeProfileControlReqResult_Object = MibScalar
sleAutoUpgradeProfileControlReqResult = _SleAutoUpgradeProfileControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 5),
    _SleAutoUpgradeProfileControlReqResult_Type()
)
sleAutoUpgradeProfileControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlReqResult.setStatus("current")
_SleAutoUpgradeProfileControlName_Type = OctetString
_SleAutoUpgradeProfileControlName_Object = MibScalar
sleAutoUpgradeProfileControlName = _SleAutoUpgradeProfileControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 6),
    _SleAutoUpgradeProfileControlName_Type()
)
sleAutoUpgradeProfileControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlName.setStatus("current")
_SleAutoUpgradeProfileControlOldVer_Type = OctetString
_SleAutoUpgradeProfileControlOldVer_Object = MibScalar
sleAutoUpgradeProfileControlOldVer = _SleAutoUpgradeProfileControlOldVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 7),
    _SleAutoUpgradeProfileControlOldVer_Type()
)
sleAutoUpgradeProfileControlOldVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlOldVer.setStatus("current")
_SleAutoUpgradeProfileControlNewVer_Type = OctetString
_SleAutoUpgradeProfileControlNewVer_Object = MibScalar
sleAutoUpgradeProfileControlNewVer = _SleAutoUpgradeProfileControlNewVer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 8),
    _SleAutoUpgradeProfileControlNewVer_Type()
)
sleAutoUpgradeProfileControlNewVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlNewVer.setStatus("current")
_SleAutoUpgradeProfileControlSize_Type = Integer32
_SleAutoUpgradeProfileControlSize_Object = MibScalar
sleAutoUpgradeProfileControlSize = _SleAutoUpgradeProfileControlSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 9),
    _SleAutoUpgradeProfileControlSize_Type()
)
sleAutoUpgradeProfileControlSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlSize.setStatus("current")


class _SleAutoUpgradeProfileControlPeriodType_Type(Integer32):
    """Custom type sleAutoUpgradeProfileControlPeriodType based on Integer32"""
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
        *(("auto", 1),
          ("daily", 2),
          ("weekly", 3),
          ("monthly", 4),
          ("interval", 5),
          ("once", 6))
    )


_SleAutoUpgradeProfileControlPeriodType_Type.__name__ = "Integer32"
_SleAutoUpgradeProfileControlPeriodType_Object = MibScalar
sleAutoUpgradeProfileControlPeriodType = _SleAutoUpgradeProfileControlPeriodType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 10),
    _SleAutoUpgradeProfileControlPeriodType_Type()
)
sleAutoUpgradeProfileControlPeriodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlPeriodType.setStatus("current")
_SleAutoUpgradeProfileControlDate_Type = OctetString
_SleAutoUpgradeProfileControlDate_Object = MibScalar
sleAutoUpgradeProfileControlDate = _SleAutoUpgradeProfileControlDate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 11),
    _SleAutoUpgradeProfileControlDate_Type()
)
sleAutoUpgradeProfileControlDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlDate.setStatus("current")
_SleAutoUpgradeProfileControlPeriodDate_Type = OctetString
_SleAutoUpgradeProfileControlPeriodDate_Object = MibScalar
sleAutoUpgradeProfileControlPeriodDate = _SleAutoUpgradeProfileControlPeriodDate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 12),
    _SleAutoUpgradeProfileControlPeriodDate_Type()
)
sleAutoUpgradeProfileControlPeriodDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlPeriodDate.setStatus("current")
_SleAutoUpgradeProfileControlTimeout_Type = Integer32
_SleAutoUpgradeProfileControlTimeout_Object = MibScalar
sleAutoUpgradeProfileControlTimeout = _SleAutoUpgradeProfileControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 13),
    _SleAutoUpgradeProfileControlTimeout_Type()
)
sleAutoUpgradeProfileControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlTimeout.setStatus("current")


class _SleAutoUpgradeProfileControlRetry_Type(Integer32):
    """Custom type sleAutoUpgradeProfileControlRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_SleAutoUpgradeProfileControlRetry_Type.__name__ = "Integer32"
_SleAutoUpgradeProfileControlRetry_Object = MibScalar
sleAutoUpgradeProfileControlRetry = _SleAutoUpgradeProfileControlRetry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 14),
    _SleAutoUpgradeProfileControlRetry_Type()
)
sleAutoUpgradeProfileControlRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlRetry.setStatus("current")
_SleAutoUpgradeProfileControlRegSec_Type = Integer32
_SleAutoUpgradeProfileControlRegSec_Object = MibScalar
sleAutoUpgradeProfileControlRegSec = _SleAutoUpgradeProfileControlRegSec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 15),
    _SleAutoUpgradeProfileControlRegSec_Type()
)
sleAutoUpgradeProfileControlRegSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlRegSec.setStatus("current")
_SleAutoUpgradeProfileControlReloadTime_Type = OctetString
_SleAutoUpgradeProfileControlReloadTime_Object = MibScalar
sleAutoUpgradeProfileControlReloadTime = _SleAutoUpgradeProfileControlReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 16),
    _SleAutoUpgradeProfileControlReloadTime_Type()
)
sleAutoUpgradeProfileControlReloadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlReloadTime.setStatus("current")
_SleAutoUpgradeProfileControlModel_Type = OctetString
_SleAutoUpgradeProfileControlModel_Object = MibScalar
sleAutoUpgradeProfileControlModel = _SleAutoUpgradeProfileControlModel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 2, 17),
    _SleAutoUpgradeProfileControlModel_Type()
)
sleAutoUpgradeProfileControlModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileControlModel.setStatus("current")
_SleAutoUpgradeProfileNotification_ObjectIdentity = ObjectIdentity
sleAutoUpgradeProfileNotification = _SleAutoUpgradeProfileNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 3)
)
_SleAutoUpgradeMgmt_ObjectIdentity = ObjectIdentity
sleAutoUpgradeMgmt = _SleAutoUpgradeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2)
)
_SleAutoUpgradeOltTable_Object = MibTable
sleAutoUpgradeOltTable = _SleAutoUpgradeOltTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    sleAutoUpgradeOltTable.setStatus("current")
_SleAutoUpgradeOltEntry_Object = MibTableRow
sleAutoUpgradeOltEntry = _SleAutoUpgradeOltEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 1, 1)
)
sleAutoUpgradeOltEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOltSlotIndex"),
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOltFwType"),
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOltProfileName"),
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOltSlotType"),
)
if mibBuilder.loadTexts:
    sleAutoUpgradeOltEntry.setStatus("current")


class _SleAutoUpgradeOltSlotIndex_Type(Integer32):
    """Custom type sleAutoUpgradeOltSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SleAutoUpgradeOltSlotIndex_Type.__name__ = "Integer32"
_SleAutoUpgradeOltSlotIndex_Object = MibTableColumn
sleAutoUpgradeOltSlotIndex = _SleAutoUpgradeOltSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 1, 1, 1),
    _SleAutoUpgradeOltSlotIndex_Type()
)
sleAutoUpgradeOltSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeOltSlotIndex.setStatus("current")


class _SleAutoUpgradeOltFwType_Type(Integer32):
    """Custom type sleAutoUpgradeOltFwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("os", 1),
          ("bootloader", 2))
    )


_SleAutoUpgradeOltFwType_Type.__name__ = "Integer32"
_SleAutoUpgradeOltFwType_Object = MibTableColumn
sleAutoUpgradeOltFwType = _SleAutoUpgradeOltFwType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 1, 1, 2),
    _SleAutoUpgradeOltFwType_Type()
)
sleAutoUpgradeOltFwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeOltFwType.setStatus("current")
_SleAutoUpgradeOltProfileName_Type = OctetString
_SleAutoUpgradeOltProfileName_Object = MibTableColumn
sleAutoUpgradeOltProfileName = _SleAutoUpgradeOltProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 1, 1, 3),
    _SleAutoUpgradeOltProfileName_Type()
)
sleAutoUpgradeOltProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeOltProfileName.setStatus("current")


class _SleAutoUpgradeOltSlotType_Type(Integer32):
    """Custom type sleAutoUpgradeOltSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("sfu", 1),
          ("siuge12", 2),
          ("siuepon12", 3),
          ("siugpon4", 4),
          ("niuge12", 5))
    )


_SleAutoUpgradeOltSlotType_Type.__name__ = "Integer32"
_SleAutoUpgradeOltSlotType_Object = MibTableColumn
sleAutoUpgradeOltSlotType = _SleAutoUpgradeOltSlotType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 1, 1, 4),
    _SleAutoUpgradeOltSlotType_Type()
)
sleAutoUpgradeOltSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeOltSlotType.setStatus("current")
_SleAutoUpgradeOntTable_Object = MibTable
sleAutoUpgradeOntTable = _SleAutoUpgradeOntTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 2)
)
if mibBuilder.loadTexts:
    sleAutoUpgradeOntTable.setStatus("current")
_SleAutoUpgradeOntEntry_Object = MibTableRow
sleAutoUpgradeOntEntry = _SleAutoUpgradeOntEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 2, 1)
)
sleAutoUpgradeOntEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOntOltIndex"),
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOntIndex"),
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOntFwType"),
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOntProfileName"),
)
if mibBuilder.loadTexts:
    sleAutoUpgradeOntEntry.setStatus("current")


class _SleAutoUpgradeOntOltIndex_Type(Integer32):
    """Custom type sleAutoUpgradeOntOltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SleAutoUpgradeOntOltIndex_Type.__name__ = "Integer32"
_SleAutoUpgradeOntOltIndex_Object = MibTableColumn
sleAutoUpgradeOntOltIndex = _SleAutoUpgradeOntOltIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 2, 1, 1),
    _SleAutoUpgradeOntOltIndex_Type()
)
sleAutoUpgradeOntOltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeOntOltIndex.setStatus("current")


class _SleAutoUpgradeOntIndex_Type(Integer32):
    """Custom type sleAutoUpgradeOntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SleAutoUpgradeOntIndex_Type.__name__ = "Integer32"
_SleAutoUpgradeOntIndex_Object = MibTableColumn
sleAutoUpgradeOntIndex = _SleAutoUpgradeOntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 2, 1, 2),
    _SleAutoUpgradeOntIndex_Type()
)
sleAutoUpgradeOntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeOntIndex.setStatus("current")


class _SleAutoUpgradeOntFwType_Type(Integer32):
    """Custom type sleAutoUpgradeOntFwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("os", 1),
          ("bootloader", 2))
    )


_SleAutoUpgradeOntFwType_Type.__name__ = "Integer32"
_SleAutoUpgradeOntFwType_Object = MibTableColumn
sleAutoUpgradeOntFwType = _SleAutoUpgradeOntFwType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 2, 1, 3),
    _SleAutoUpgradeOntFwType_Type()
)
sleAutoUpgradeOntFwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeOntFwType.setStatus("current")
_SleAutoUpgradeOntProfileName_Type = OctetString
_SleAutoUpgradeOntProfileName_Object = MibTableColumn
sleAutoUpgradeOntProfileName = _SleAutoUpgradeOntProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 2, 1, 4),
    _SleAutoUpgradeOntProfileName_Type()
)
sleAutoUpgradeOntProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeOntProfileName.setStatus("current")
_SleAutoUpgradeMgmtControl_ObjectIdentity = ObjectIdentity
sleAutoUpgradeMgmtControl = _SleAutoUpgradeMgmtControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3)
)


class _SleAutoUpgradeMgmtControlRequest_Type(Integer32):
    """Custom type sleAutoUpgradeMgmtControlRequest based on Integer32"""
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
        *(("setAutoUpgrdOltProfile", 1),
          ("unsetAutoUpgrdOltProfile", 2),
          ("setAutoUpgrdOntProfile", 3),
          ("unsetAutoUpgrdOntProfile", 4))
    )


_SleAutoUpgradeMgmtControlRequest_Type.__name__ = "Integer32"
_SleAutoUpgradeMgmtControlRequest_Object = MibScalar
sleAutoUpgradeMgmtControlRequest = _SleAutoUpgradeMgmtControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 1),
    _SleAutoUpgradeMgmtControlRequest_Type()
)
sleAutoUpgradeMgmtControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlRequest.setStatus("current")
_SleAutoUpgradeMgmtControlStatus_Type = SleControlStatusType
_SleAutoUpgradeMgmtControlStatus_Object = MibScalar
sleAutoUpgradeMgmtControlStatus = _SleAutoUpgradeMgmtControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 2),
    _SleAutoUpgradeMgmtControlStatus_Type()
)
sleAutoUpgradeMgmtControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlStatus.setStatus("current")
_SleAutoUpgradeMgmtControlTimer_Type = Gauge32
_SleAutoUpgradeMgmtControlTimer_Object = MibScalar
sleAutoUpgradeMgmtControlTimer = _SleAutoUpgradeMgmtControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 3),
    _SleAutoUpgradeMgmtControlTimer_Type()
)
sleAutoUpgradeMgmtControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlTimer.setStatus("current")
_SleAutoUpgradeMgmtControlTimeStamp_Type = TimeTicks
_SleAutoUpgradeMgmtControlTimeStamp_Object = MibScalar
sleAutoUpgradeMgmtControlTimeStamp = _SleAutoUpgradeMgmtControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 4),
    _SleAutoUpgradeMgmtControlTimeStamp_Type()
)
sleAutoUpgradeMgmtControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlTimeStamp.setStatus("current")
_SleAutoUpgradeMgmtControlReqResult_Type = SleControlRequestResultType
_SleAutoUpgradeMgmtControlReqResult_Object = MibScalar
sleAutoUpgradeMgmtControlReqResult = _SleAutoUpgradeMgmtControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 5),
    _SleAutoUpgradeMgmtControlReqResult_Type()
)
sleAutoUpgradeMgmtControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlReqResult.setStatus("current")
_SleAutoUpgradeMgmtControlOltIndex_Type = OctetString
_SleAutoUpgradeMgmtControlOltIndex_Object = MibScalar
sleAutoUpgradeMgmtControlOltIndex = _SleAutoUpgradeMgmtControlOltIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 6),
    _SleAutoUpgradeMgmtControlOltIndex_Type()
)
sleAutoUpgradeMgmtControlOltIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlOltIndex.setStatus("current")
_SleAutoUpgradeMgmtControlOntIndex_Type = OctetString
_SleAutoUpgradeMgmtControlOntIndex_Object = MibScalar
sleAutoUpgradeMgmtControlOntIndex = _SleAutoUpgradeMgmtControlOntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 7),
    _SleAutoUpgradeMgmtControlOntIndex_Type()
)
sleAutoUpgradeMgmtControlOntIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlOntIndex.setStatus("current")


class _SleAutoUpgradeMgmtControlFwType_Type(Integer32):
    """Custom type sleAutoUpgradeMgmtControlFwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("os", 1),
          ("bootloader", 2))
    )


_SleAutoUpgradeMgmtControlFwType_Type.__name__ = "Integer32"
_SleAutoUpgradeMgmtControlFwType_Object = MibScalar
sleAutoUpgradeMgmtControlFwType = _SleAutoUpgradeMgmtControlFwType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 8),
    _SleAutoUpgradeMgmtControlFwType_Type()
)
sleAutoUpgradeMgmtControlFwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlFwType.setStatus("current")
_SleAutoUpgradeMgmtControlProfileName_Type = OctetString
_SleAutoUpgradeMgmtControlProfileName_Object = MibScalar
sleAutoUpgradeMgmtControlProfileName = _SleAutoUpgradeMgmtControlProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 9),
    _SleAutoUpgradeMgmtControlProfileName_Type()
)
sleAutoUpgradeMgmtControlProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlProfileName.setStatus("current")


class _SleAutoUpgradeMgmtControlSlotType_Type(Integer32):
    """Custom type sleAutoUpgradeMgmtControlSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("sfu", 1),
          ("siuge12", 2),
          ("siuepon12", 3),
          ("siugpon4", 4),
          ("niuge12", 5))
    )


_SleAutoUpgradeMgmtControlSlotType_Type.__name__ = "Integer32"
_SleAutoUpgradeMgmtControlSlotType_Object = MibScalar
sleAutoUpgradeMgmtControlSlotType = _SleAutoUpgradeMgmtControlSlotType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 3, 10),
    _SleAutoUpgradeMgmtControlSlotType_Type()
)
sleAutoUpgradeMgmtControlSlotType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeMgmtControlSlotType.setStatus("current")
_SleAutoUpgradeMgmtNotification_ObjectIdentity = ObjectIdentity
sleAutoUpgradeMgmtNotification = _SleAutoUpgradeMgmtNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 4)
)
_SleAutoUpgradeLog_ObjectIdentity = ObjectIdentity
sleAutoUpgradeLog = _SleAutoUpgradeLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3)
)
_SleAutoUpgradeLogInfo_ObjectIdentity = ObjectIdentity
sleAutoUpgradeLogInfo = _SleAutoUpgradeLogInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 1)
)
_SleAutoUpgradeLogControl_ObjectIdentity = ObjectIdentity
sleAutoUpgradeLogControl = _SleAutoUpgradeLogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2)
)


class _SleAutoUpgradeLogControlRequest_Type(Integer32):
    """Custom type sleAutoUpgradeLogControlRequest based on Integer32"""
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
        *(("delAutoUpgradeOltLog", 1),
          ("delAutoUpgradeOltLogAll", 2),
          ("delAutoUpgradeOntLog", 3),
          ("delAutoUpgradeOntLogAll", 4),
          ("exportAutoUpgradeOltLog", 5),
          ("exportAutoUpgradeOntLog", 6))
    )


_SleAutoUpgradeLogControlRequest_Type.__name__ = "Integer32"
_SleAutoUpgradeLogControlRequest_Object = MibScalar
sleAutoUpgradeLogControlRequest = _SleAutoUpgradeLogControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 1),
    _SleAutoUpgradeLogControlRequest_Type()
)
sleAutoUpgradeLogControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlRequest.setStatus("current")
_SleAutoUpgradeLogControlStatus_Type = SleControlStatusType
_SleAutoUpgradeLogControlStatus_Object = MibScalar
sleAutoUpgradeLogControlStatus = _SleAutoUpgradeLogControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 2),
    _SleAutoUpgradeLogControlStatus_Type()
)
sleAutoUpgradeLogControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlStatus.setStatus("current")
_SleAutoUpgradeLogControlTimer_Type = Gauge32
_SleAutoUpgradeLogControlTimer_Object = MibScalar
sleAutoUpgradeLogControlTimer = _SleAutoUpgradeLogControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 3),
    _SleAutoUpgradeLogControlTimer_Type()
)
sleAutoUpgradeLogControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlTimer.setStatus("current")
_SleAutoUpgradeLogControlTimeStamp_Type = TimeTicks
_SleAutoUpgradeLogControlTimeStamp_Object = MibScalar
sleAutoUpgradeLogControlTimeStamp = _SleAutoUpgradeLogControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 4),
    _SleAutoUpgradeLogControlTimeStamp_Type()
)
sleAutoUpgradeLogControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlTimeStamp.setStatus("current")
_SleAutoUpgradeLogControlReqResult_Type = SleControlRequestResultType
_SleAutoUpgradeLogControlReqResult_Object = MibScalar
sleAutoUpgradeLogControlReqResult = _SleAutoUpgradeLogControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 5),
    _SleAutoUpgradeLogControlReqResult_Type()
)
sleAutoUpgradeLogControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlReqResult.setStatus("current")
_SleAutoUpgradeLogControlSlotIndex_Type = OctetString
_SleAutoUpgradeLogControlSlotIndex_Object = MibScalar
sleAutoUpgradeLogControlSlotIndex = _SleAutoUpgradeLogControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 6),
    _SleAutoUpgradeLogControlSlotIndex_Type()
)
sleAutoUpgradeLogControlSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlSlotIndex.setStatus("current")
_SleAutoUpgradeLogControlOntIndex_Type = OctetString
_SleAutoUpgradeLogControlOntIndex_Object = MibScalar
sleAutoUpgradeLogControlOntIndex = _SleAutoUpgradeLogControlOntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 7),
    _SleAutoUpgradeLogControlOntIndex_Type()
)
sleAutoUpgradeLogControlOntIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlOntIndex.setStatus("current")


class _SleAutoUpgradeLogControlExportMethod_Type(Integer32):
    """Custom type sleAutoUpgradeLogControlExportMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("tftp", 2))
    )


_SleAutoUpgradeLogControlExportMethod_Type.__name__ = "Integer32"
_SleAutoUpgradeLogControlExportMethod_Object = MibScalar
sleAutoUpgradeLogControlExportMethod = _SleAutoUpgradeLogControlExportMethod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 8),
    _SleAutoUpgradeLogControlExportMethod_Type()
)
sleAutoUpgradeLogControlExportMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlExportMethod.setStatus("current")
_SleAutoUpgradeLogControlServer_Type = IpAddress
_SleAutoUpgradeLogControlServer_Object = MibScalar
sleAutoUpgradeLogControlServer = _SleAutoUpgradeLogControlServer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 9),
    _SleAutoUpgradeLogControlServer_Type()
)
sleAutoUpgradeLogControlServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlServer.setStatus("current")
_SleAutoUpgradeLogControlUser_Type = OctetString
_SleAutoUpgradeLogControlUser_Object = MibScalar
sleAutoUpgradeLogControlUser = _SleAutoUpgradeLogControlUser_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 10),
    _SleAutoUpgradeLogControlUser_Type()
)
sleAutoUpgradeLogControlUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlUser.setStatus("current")
_SleAutoUpgradeLogControlPasswd_Type = OctetString
_SleAutoUpgradeLogControlPasswd_Object = MibScalar
sleAutoUpgradeLogControlPasswd = _SleAutoUpgradeLogControlPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 2, 11),
    _SleAutoUpgradeLogControlPasswd_Type()
)
sleAutoUpgradeLogControlPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAutoUpgradeLogControlPasswd.setStatus("current")
_SleAutoUpgradeLogNotification_ObjectIdentity = ObjectIdentity
sleAutoUpgradeLogNotification = _SleAutoUpgradeLogNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 3)
)
_SleWatchdog_ObjectIdentity = ObjectIdentity
sleWatchdog = _SleWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19)
)
_SleWatchdogInfo_ObjectIdentity = ObjectIdentity
sleWatchdogInfo = _SleWatchdogInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 1)
)


class _SleWatchdogAdminStatus_Type(Integer32):
    """Custom type sleWatchdogAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleWatchdogAdminStatus_Type.__name__ = "Integer32"
_SleWatchdogAdminStatus_Object = MibScalar
sleWatchdogAdminStatus = _SleWatchdogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 1, 1),
    _SleWatchdogAdminStatus_Type()
)
sleWatchdogAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleWatchdogAdminStatus.setStatus("current")
_SleWatchdogTimeout_Type = Integer32
_SleWatchdogTimeout_Object = MibScalar
sleWatchdogTimeout = _SleWatchdogTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 1, 2),
    _SleWatchdogTimeout_Type()
)
sleWatchdogTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleWatchdogTimeout.setStatus("current")


class _SleWatchdogMode_Type(Integer32):
    """Custom type sleWatchdogMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("top", 1),
          ("timer", 2),
          ("thread", 3))
    )


_SleWatchdogMode_Type.__name__ = "Integer32"
_SleWatchdogMode_Object = MibScalar
sleWatchdogMode = _SleWatchdogMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 1, 3),
    _SleWatchdogMode_Type()
)
sleWatchdogMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleWatchdogMode.setStatus("current")
_SleWatchdogControl_ObjectIdentity = ObjectIdentity
sleWatchdogControl = _SleWatchdogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2)
)


class _SleWatchdogControlRequest_Type(Integer32):
    """Custom type sleWatchdogControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setWatchdogStatus", 1),
          ("setWatchdogTimeout", 2),
          ("setWatchdogMode", 3))
    )


_SleWatchdogControlRequest_Type.__name__ = "Integer32"
_SleWatchdogControlRequest_Object = MibScalar
sleWatchdogControlRequest = _SleWatchdogControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2, 1),
    _SleWatchdogControlRequest_Type()
)
sleWatchdogControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleWatchdogControlRequest.setStatus("current")
_SleWatchdogControlStatus_Type = SleControlStatusType
_SleWatchdogControlStatus_Object = MibScalar
sleWatchdogControlStatus = _SleWatchdogControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2, 2),
    _SleWatchdogControlStatus_Type()
)
sleWatchdogControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleWatchdogControlStatus.setStatus("current")
_SleWatchdogControlTimer_Type = Gauge32
_SleWatchdogControlTimer_Object = MibScalar
sleWatchdogControlTimer = _SleWatchdogControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2, 3),
    _SleWatchdogControlTimer_Type()
)
sleWatchdogControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleWatchdogControlTimer.setStatus("current")
_SleWatchdogControlTimeStamp_Type = TimeTicks
_SleWatchdogControlTimeStamp_Object = MibScalar
sleWatchdogControlTimeStamp = _SleWatchdogControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2, 4),
    _SleWatchdogControlTimeStamp_Type()
)
sleWatchdogControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleWatchdogControlTimeStamp.setStatus("current")
_SleWatchdogControlReqResult_Type = SleControlRequestResultType
_SleWatchdogControlReqResult_Object = MibScalar
sleWatchdogControlReqResult = _SleWatchdogControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2, 5),
    _SleWatchdogControlReqResult_Type()
)
sleWatchdogControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleWatchdogControlReqResult.setStatus("current")


class _SleWatchdogControlAdminStatus_Type(Integer32):
    """Custom type sleWatchdogControlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleWatchdogControlAdminStatus_Type.__name__ = "Integer32"
_SleWatchdogControlAdminStatus_Object = MibScalar
sleWatchdogControlAdminStatus = _SleWatchdogControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2, 6),
    _SleWatchdogControlAdminStatus_Type()
)
sleWatchdogControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleWatchdogControlAdminStatus.setStatus("current")
_SleWatchdogControlTimeout_Type = Integer32
_SleWatchdogControlTimeout_Object = MibScalar
sleWatchdogControlTimeout = _SleWatchdogControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2, 7),
    _SleWatchdogControlTimeout_Type()
)
sleWatchdogControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleWatchdogControlTimeout.setStatus("current")


class _SleWatchdogControlMode_Type(Integer32):
    """Custom type sleWatchdogControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("top", 1),
          ("timer", 2),
          ("thread", 3))
    )


_SleWatchdogControlMode_Type.__name__ = "Integer32"
_SleWatchdogControlMode_Object = MibScalar
sleWatchdogControlMode = _SleWatchdogControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 2, 8),
    _SleWatchdogControlMode_Type()
)
sleWatchdogControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleWatchdogControlMode.setStatus("current")
_SleWatchdogNotification_ObjectIdentity = ObjectIdentity
sleWatchdogNotification = _SleWatchdogNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 3)
)
_SleFtpclient_ObjectIdentity = ObjectIdentity
sleFtpclient = _SleFtpclient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100)
)
_SleFtpclientTable_Object = MibTable
sleFtpclientTable = _SleFtpclientTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 1)
)
if mibBuilder.loadTexts:
    sleFtpclientTable.setStatus("current")
_SleFtpclientEntry_Object = MibTableRow
sleFtpclientEntry = _SleFtpclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 1, 1)
)
sleFtpclientEntry.setIndexNames(
    (0, "SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientIndex"),
)
if mibBuilder.loadTexts:
    sleFtpclientEntry.setStatus("current")


class _SleFtpclientIndex_Type(Integer32):
    """Custom type sleFtpclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleFtpclientIndex_Type.__name__ = "Integer32"
_SleFtpclientIndex_Object = MibTableColumn
sleFtpclientIndex = _SleFtpclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 1, 1, 1),
    _SleFtpclientIndex_Type()
)
sleFtpclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFtpclientIndex.setStatus("current")
_SleFtpclientFileName_Type = OctetString
_SleFtpclientFileName_Object = MibTableColumn
sleFtpclientFileName = _SleFtpclientFileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 1, 1, 2),
    _SleFtpclientFileName_Type()
)
sleFtpclientFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFtpclientFileName.setStatus("current")
_SleFtpclientFileSize_Type = Integer32
_SleFtpclientFileSize_Object = MibTableColumn
sleFtpclientFileSize = _SleFtpclientFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 1, 1, 3),
    _SleFtpclientFileSize_Type()
)
sleFtpclientFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFtpclientFileSize.setStatus("current")
_SleFtpclientControl_ObjectIdentity = ObjectIdentity
sleFtpclientControl = _SleFtpclientControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2)
)


class _SleFtpclientControlRequest_Type(Integer32):
    """Custom type sleFtpclientControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("updateDirectoryInfo", 1)
    )


_SleFtpclientControlRequest_Type.__name__ = "Integer32"
_SleFtpclientControlRequest_Object = MibScalar
sleFtpclientControlRequest = _SleFtpclientControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 1),
    _SleFtpclientControlRequest_Type()
)
sleFtpclientControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFtpclientControlRequest.setStatus("current")
_SleFtpclientControlStatus_Type = SleControlStatusType
_SleFtpclientControlStatus_Object = MibScalar
sleFtpclientControlStatus = _SleFtpclientControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 2),
    _SleFtpclientControlStatus_Type()
)
sleFtpclientControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFtpclientControlStatus.setStatus("current")
_SleFtpclientControlTimer_Type = Gauge32
_SleFtpclientControlTimer_Object = MibScalar
sleFtpclientControlTimer = _SleFtpclientControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 3),
    _SleFtpclientControlTimer_Type()
)
sleFtpclientControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFtpclientControlTimer.setStatus("current")
_SleFtpclientControlTimeStamp_Type = TimeTicks
_SleFtpclientControlTimeStamp_Object = MibScalar
sleFtpclientControlTimeStamp = _SleFtpclientControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 4),
    _SleFtpclientControlTimeStamp_Type()
)
sleFtpclientControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFtpclientControlTimeStamp.setStatus("current")
_SleFtpclientControlReqResult_Type = SleControlRequestResultType
_SleFtpclientControlReqResult_Object = MibScalar
sleFtpclientControlReqResult = _SleFtpclientControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 5),
    _SleFtpclientControlReqResult_Type()
)
sleFtpclientControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFtpclientControlReqResult.setStatus("current")
_SleFtpclientControlServerIp_Type = IpAddress
_SleFtpclientControlServerIp_Object = MibScalar
sleFtpclientControlServerIp = _SleFtpclientControlServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 6),
    _SleFtpclientControlServerIp_Type()
)
sleFtpclientControlServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFtpclientControlServerIp.setStatus("current")
_SleFtpclientControlUserId_Type = OctetString
_SleFtpclientControlUserId_Object = MibScalar
sleFtpclientControlUserId = _SleFtpclientControlUserId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 7),
    _SleFtpclientControlUserId_Type()
)
sleFtpclientControlUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFtpclientControlUserId.setStatus("current")
_SleFtpclientControlPassword_Type = OctetString
_SleFtpclientControlPassword_Object = MibScalar
sleFtpclientControlPassword = _SleFtpclientControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 8),
    _SleFtpclientControlPassword_Type()
)
sleFtpclientControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFtpclientControlPassword.setStatus("current")
_SleFtpclientControlDirectoryPath_Type = OctetString
_SleFtpclientControlDirectoryPath_Object = MibScalar
sleFtpclientControlDirectoryPath = _SleFtpclientControlDirectoryPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 2, 9),
    _SleFtpclientControlDirectoryPath_Type()
)
sleFtpclientControlDirectoryPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFtpclientControlDirectoryPath.setStatus("current")
_SleFtpclientNotification_ObjectIdentity = ObjectIdentity
sleFtpclientNotification = _SleFtpclientNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 3)
)

# Managed Objects groups

sleSystemMaintenanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 101)
)
sleSystemMaintenanceGroup.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemModelName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSerialNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemHWVersion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBLVersion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSWCompatibility"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemOSVersion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMacAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemHostName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPULoadAll"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPULoadInterrupt"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPUThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPUInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemoryTotal"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemoryFree"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemoryShared"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemoryBuffers"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemoryCached"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemorySwapTotal"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemorySwapFree"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDefaultOS"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemOS1Version"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemOS1Size"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemOS1BuildNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemOS2Version"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemOS2Size"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemOS2BuildNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFlashTotalSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFlashOSSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFlashConfigSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFlashOSUsedSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFlashConfigUsedSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemClock"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemTimezone"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDNSDomainName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemInitBanner"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSuccessBanner"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFailBanner"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogNonVolatileNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogLocalCode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSSHState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNTPState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBackupInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDhcpActivity"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDefaultTTL"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindInterfaceName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSessionTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemExecTimeout"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemWatchdogStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleLoginIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleLoginUser"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleLoginTTY"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleLoginRemote"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleLoginTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupConfigFile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessID"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessUser"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessCPU"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessMemory"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessVSZ"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessRSS"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessTerminal"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessStartTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessUsedTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleProcessCommand"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfFacility"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfSeverity"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfTarget"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfStorage"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfTargetAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogHistVolIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogHistVolMsgText"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogHistVolTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogHistNVolIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogHistNVolMsgText"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogHistNVolTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteUser"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteHost"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliConfStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliMemoryMaxSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliMemoryUsedsize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliMemoryFreesize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliTransferInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptId"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileUser"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileUpdateTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleYear"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleMonth"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleDay"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleMinute"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleScriptName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleTransferType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleLastExecutedTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleOutputRule"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleLastResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileId"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileUpdatedTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingConfStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingIpAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingTransactionInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingNumberOfRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRequestInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingTimeoutOfRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingEnableTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRequestCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingReplyCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingLossCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingTotalPingTransaction"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingTotalLossTransaction"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakContStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakMemThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakCheckInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakNumberOfVerification"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakVerificationInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakRebootCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakEnableTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakLastFreeMemory"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakVerificationCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakDetectionCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakTotalVerificationCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakTotalDetectionCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeStartHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeStartMin"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeEndHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeEndMin"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpInfoPID"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpInfoStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpFile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceProtocol"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServicePort"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindInterface"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFtpBindInterface"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemRedundancyPort"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakRebootThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakCountThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRebootCounter"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileMaxLine"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterValue"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRebootThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingLossThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserLevel"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerIpAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerUser"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerDir"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogAction"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogErrcnt"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBootInfo"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemTempHighThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemTempLowThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemLowCPUThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemLowCPUInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlHostName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlCPUThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlCPUInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlDefaultOS"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlClock"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimezone"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlDNSDomainName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlInitBanner"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSuccessBanner"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlFailBanner"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogVolatileNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogNonVolatileNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogBindAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogLocalCode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSSHState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlNTPState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlOSUpgradeNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlServerAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlUpDownFlag"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlUserID"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlFileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlBackupFlag"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReloadOS"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlBackupInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlDhcpActivity"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlDefaultTTL"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogVolatileSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogBindInterfaceName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSrcPort"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlDstPort"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSessionTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlExecTimeout"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlWatchdogStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlClearOs"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlNtpBindInterface"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlFtpBindInterface"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogVolMaxLine"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTempHighThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTempLowThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlMemThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlLowCPUThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlLowCPUInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlCreateMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlServerIP"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlUserID"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlSrcConfigFile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlDstConfigFile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlSeverity"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlFacility"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlTarget"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlStorage"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlTargetAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlConfStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlMemoryMaxsize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlTransferInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlIpAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlUserName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlFilePath"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlScriptName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlYear"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlMonth"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlDay"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlMinute"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlScriptName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlTransferType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlOutputRule"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlProfName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlIpAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlUser"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlDir"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlServer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlUserName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlOutputFileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlRemotePath"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlConfStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlIpAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlTransactionInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlNumberOfRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlRequestInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlTimeoutOfRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlPingLossThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlRebootThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlConfStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlMemThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlCheckInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlNumberOfVerification"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlVerificationInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlCountThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReboottimeStartHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReboottimeStartMin"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReboottimeEndHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReboottimeEndMin"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlRebootThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlPID"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlServerIP"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlUserID"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlCoredumpFile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlProtocol"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlPort"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRename"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlLevel"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlPwType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlDesc"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlValue"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlAction"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemRunningOS"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotUptime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotModelName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotSerialNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotHWVersion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotBLVersion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotSWCompatibility"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotOSVersion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotMacAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotCPULoadAll"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotCPULoadInterrupt"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotMemoryTotal"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotMemoryFree"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotMemoryShared"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotMemoryBuffers"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotMemoryCached"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotMemorySwapTotal"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotMemorySwapFree"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotBootReason"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotBootTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotVoltage"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileOldVer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileNewVer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfilePeriodType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfilePeriodDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileTimeout"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileRetry"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileRegSec"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileReloadTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlOldVer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlNewVer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlPeriodType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlPeriodDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlTimeout"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRetry"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRegSec"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlReloadTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOltSlotIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOltFwType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOltSlotType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOntOltIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOntIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOntFwType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlOltIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlOntIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlFwType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlSlotIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlOntIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlExportMethod"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlServer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlUser"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlPasswd"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlSlotType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemEnablePasswdType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemEnablePasswd"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemServicePasswdEncryption"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlNtpBindAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlEnablePasswdType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlEnablePasswd"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlServicePasswdEncryption"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceAdminStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlAdminStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUptime64"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpPollnterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlNtpPollInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPUDuration"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemLowCPUDuration"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlCPUDuration"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlLowCPUDuration"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuLoad"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuInterruptLoad"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlLoad"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlInterruptLoad"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserDesc"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOltProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeOntProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBarcode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetBootReason"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRebootRecoveryTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlRebootRecoveryTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemEnhancedFeature"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemGetBranchModel"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientFileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientFileSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlServerIp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlUserId"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlDirectoryPath"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemTargetId"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNodeName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNetworkName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemShelfId"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSlotId"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemWebMgmt"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlWebMgmt"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemManufacturer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemManufactureDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileModel"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlModel"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogAdminStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogTimeout"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlAdminStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlTimeout"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAdministeredMac"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlAdministeredMac"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadInHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadInMinutes"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadDailyHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadDailyMinutes"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadAtYear"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadAtMonth"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadAtDay"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutpReloadAtHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutpReloadAtMinutes"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlAutoReloadYear"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlAutoReloadMonth"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlAutoReloadDay"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlAutoReloadHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlAutoReloadMinutes"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBaseMac"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindIPAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindIPAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogBindAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSyslogBindIPAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlNtpBindAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlNtpBindIPAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDnsServerAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDnsServerAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDnsServerControlAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDnsServerControlAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlServerAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlServerAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfRemoteAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfRemoteAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfVRFIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlRemoteAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlRemoteAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlVRFIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemPLDversion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlWriteMemRetryCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlWriteMemRetryInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSysetmGlobalTimeoutMin"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSysetmGlobalTimeoutSec"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlGlobalTimeoutMin"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlGlobalTimeoutSec"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfSlotIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlSlotIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerAuthenticationKey"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerVRFIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerControlAuthenticationKey"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerControlVRFIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerPrefer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerVersion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerControlType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerControlPrefer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerControlVersion"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPULoad5s"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPULoad1m"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPULoad10m"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNosUpgradeStatus"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteFromHost"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserLoginFailureCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserLoginLastFailureTime"))
)
if mibBuilder.loadTexts:
    sleSystemMaintenanceGroup.setStatus("current")


# Notification objects

sleSystemSystemInfoProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 1)
)
sleSystemSystemInfoProfileChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemHostName"))
)
if mibBuilder.loadTexts:
    sleSystemSystemInfoProfileChanged.setStatus(
        "current"
    )

sleSystemCPUThresholdProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 2)
)
sleSystemCPUThresholdProfileChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPUThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPUInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemLowCPUThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemLowCPUInterval"))
)
if mibBuilder.loadTexts:
    sleSystemCPUThresholdProfileChanged.setStatus(
        "current"
    )

sleSystemDefaultOSChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 3)
)
sleSystemDefaultOSChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDefaultOS"))
)
if mibBuilder.loadTexts:
    sleSystemDefaultOSChanged.setStatus(
        "current"
    )

sleSystemRTCProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 4)
)
sleSystemRTCProfileChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemClock"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemTimezone"))
)
if mibBuilder.loadTexts:
    sleSystemRTCProfileChanged.setStatus(
        "current"
    )

sleSystemDNSDomainNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 5)
)
sleSystemDNSDomainNameChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDNSDomainName"))
)
if mibBuilder.loadTexts:
    sleSystemDNSDomainNameChanged.setStatus(
        "current"
    )

sleSystemBannerProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 6)
)
sleSystemBannerProfileChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemInitBanner"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSuccessBanner"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFailBanner"))
)
if mibBuilder.loadTexts:
    sleSystemBannerProfileChanged.setStatus(
        "current"
    )

sleSystemSyslogProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 7)
)
sleSystemSyslogProfileChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileMaxLine"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogNonVolatileNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogLocalCode"))
)
if mibBuilder.loadTexts:
    sleSystemSyslogProfileChanged.setStatus(
        "current"
    )

sleSystemSSHStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 8)
)
sleSystemSSHStateChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSSHState"))
)
if mibBuilder.loadTexts:
    sleSystemSSHStateChanged.setStatus(
        "current"
    )

sleSystemNTPStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 9)
)
sleSystemNTPStateChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNTPState"))
)
if mibBuilder.loadTexts:
    sleSystemNTPStateChanged.setStatus(
        "current"
    )

sleSystemOSProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 10)
)
sleSystemOSProfileChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlOSUpgradeNumber"))
)
if mibBuilder.loadTexts:
    sleSystemOSProfileChanged.setStatus(
        "current"
    )

sleSystemBackupChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 11)
)
sleSystemBackupChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlBackupFlag"))
)
if mibBuilder.loadTexts:
    sleSystemBackupChanged.setStatus(
        "current"
    )

sleSystemBackupIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 12)
)
sleSystemBackupIntervalChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBackupInterval"))
)
if mibBuilder.loadTexts:
    sleSystemBackupIntervalChanged.setStatus(
        "current"
    )

sleSystemDhcpActivityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 13)
)
sleSystemDhcpActivityChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDhcpActivity"))
)
if mibBuilder.loadTexts:
    sleSystemDhcpActivityChanged.setStatus(
        "current"
    )

sleSystemDefaultTTLChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 14)
)
sleSystemDefaultTTLChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDefaultTTL"))
)
if mibBuilder.loadTexts:
    sleSystemDefaultTTLChanged.setStatus(
        "current"
    )

sleSystemSyslogBindInterfaceNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 15)
)
sleSystemSyslogBindInterfaceNameChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindInterfaceName"))
)
if mibBuilder.loadTexts:
    sleSystemSyslogBindInterfaceNameChanged.setStatus(
        "current"
    )

sleSystemSyslogBindInterfaceNameCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 16)
)
sleSystemSyslogBindInterfaceNameCleared.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSystemSyslogBindInterfaceNameCleared.setStatus(
        "current"
    )

sleSystemConfigPortMoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 17)
)
sleSystemConfigPortMoved.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSrcPort"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlDstPort"))
)
if mibBuilder.loadTexts:
    sleSystemConfigPortMoved.setStatus(
        "current"
    )

sleSystemConfigPortCopied = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 18)
)
sleSystemConfigPortCopied.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSrcPort"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlDstPort"))
)
if mibBuilder.loadTexts:
    sleSystemConfigPortCopied.setStatus(
        "current"
    )

sleSystemConfigPortCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 19)
)
sleSystemConfigPortCleared.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSrcPort"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlDstPort"))
)
if mibBuilder.loadTexts:
    sleSystemConfigPortCleared.setStatus(
        "current"
    )

sleSystemSessionTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 20)
)
sleSystemSessionTimeChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSessionTime"))
)
if mibBuilder.loadTexts:
    sleSystemSessionTimeChanged.setStatus(
        "current"
    )

sleSystemExecTimeoutChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 21)
)
sleSystemExecTimeoutChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemExecTimeout"))
)
if mibBuilder.loadTexts:
    sleSystemExecTimeoutChanged.setStatus(
        "current"
    )

sleSystemWatchdogStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 22)
)
sleSystemWatchdogStatusChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemWatchdogStatus"))
)
if mibBuilder.loadTexts:
    sleSystemWatchdogStatusChanged.setStatus(
        "current"
    )

sleSystemNosDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 23)
)
sleSystemNosDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlClearOs"))
)
if mibBuilder.loadTexts:
    sleSystemNosDestroyed.setStatus(
        "current"
    )

sleSystemNtpBindInterfaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 24)
)
sleSystemNtpBindInterfaceChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindInterface"))
)
if mibBuilder.loadTexts:
    sleSystemNtpBindInterfaceChanged.setStatus(
        "current"
    )

sleSystemFtpBindInterfaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 25)
)
sleSystemFtpBindInterfaceChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFtpBindInterface"))
)
if mibBuilder.loadTexts:
    sleSystemFtpBindInterfaceChanged.setStatus(
        "current"
    )

sleSystemRedundancyPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 26)
)
sleSystemRedundancyPortChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlSrcPort"))
)
if mibBuilder.loadTexts:
    sleSystemRedundancyPortChanged.setStatus(
        "current"
    )

sleRedundancyPortCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 27)
)
sleRedundancyPortCleared.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRedundancyPortCleared.setStatus(
        "current"
    )

sleSystemTempThresholdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 28)
)
sleSystemTempThresholdChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTempHighThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTempLowThreshold"))
)
if mibBuilder.loadTexts:
    sleSystemTempThresholdChanged.setStatus(
        "current"
    )

sleSystemMemThresholdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 29)
)
sleSystemMemThresholdChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlMemThreshold"))
)
if mibBuilder.loadTexts:
    sleSystemMemThresholdChanged.setStatus(
        "current"
    )

sleSystemBootloaderProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 30)
)
sleSystemBootloaderProfileChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSystemBootloaderProfileChanged.setStatus(
        "current"
    )

sleSystemNtpBindAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 31)
)
sleSystemNtpBindAddressChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlNtpBindAddress"))
)
if mibBuilder.loadTexts:
    sleSystemNtpBindAddressChanged.setStatus(
        "current"
    )

sleSystemEnablePasswdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 32)
)
sleSystemEnablePasswdChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlEnablePasswdType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlEnablePasswd"))
)
if mibBuilder.loadTexts:
    sleSystemEnablePasswdChanged.setStatus(
        "current"
    )

sleSystemEnableServicePasswdEncryptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 33)
)
sleSystemEnableServicePasswdEncryptionChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlServicePasswdEncryption"))
)
if mibBuilder.loadTexts:
    sleSystemEnableServicePasswdEncryptionChanged.setStatus(
        "current"
    )

sleSystemPasswdRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 34)
)
sleSystemPasswdRestored.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSystemPasswdRestored.setStatus(
        "current"
    )

sleSystemNtpPollIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 35)
)
sleSystemNtpPollIntervalChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpPollnterval"))
)
if mibBuilder.loadTexts:
    sleSystemNtpPollIntervalChanged.setStatus(
        "current"
    )

sleSystemRestoreFactoryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 36)
)
sleSystemRestoreFactoryChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSystemRestoreFactoryChanged.setStatus(
        "current"
    )

sleSystemWebMgmtChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 37)
)
sleSystemWebMgmtChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlWebMgmt"))
)
if mibBuilder.loadTexts:
    sleSystemWebMgmtChanged.setStatus(
        "current"
    )

sleSystemAutoReloadInTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 38)
)
sleSystemAutoReloadInTimeChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadInHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadInMinutes"))
)
if mibBuilder.loadTexts:
    sleSystemAutoReloadInTimeChanged.setStatus(
        "current"
    )

sleSystemAutoReloadDailyTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 39)
)
sleSystemAutoReloadDailyTimeChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadDailyMinutes"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadDailyHour"))
)
if mibBuilder.loadTexts:
    sleSystemAutoReloadDailyTimeChanged.setStatus(
        "current"
    )

sleSystemAutoReloadAtTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 40)
)
sleSystemAutoReloadAtTimeChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutpReloadAtMinutes"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutpReloadAtHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadAtDay"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadAtMonth"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadAtYear"))
)
if mibBuilder.loadTexts:
    sleSystemAutoReloadAtTimeChanged.setStatus(
        "current"
    )

sleSystemAdministeredMacChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 41)
)
sleSystemAdministeredMacChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlAdministeredMac"))
)
if mibBuilder.loadTexts:
    sleSystemAdministeredMacChanged.setStatus(
        "current"
    )

sleSystemSyslogProfileExChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 42)
)
sleSystemSyslogProfileExChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogState"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogNonVolatileNumber"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogLocalCode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogVolatileMaxLine"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindIPAddress"))
)
if mibBuilder.loadTexts:
    sleSystemSyslogProfileExChanged.setStatus(
        "current"
    )

sleSystemNtpBindAddressExChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 43)
)
sleSystemNtpBindAddressExChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindIPAddress"))
)
if mibBuilder.loadTexts:
    sleSystemNtpBindAddressExChanged.setStatus(
        "current"
    )

sleSystemRetryWriteMemoryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 44)
)
sleSystemRetryWriteMemoryChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlWriteMemRetryCount"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlWriteMemRetryInterval"))
)
if mibBuilder.loadTexts:
    sleSystemRetryWriteMemoryChanged.setStatus(
        "current"
    )

sleSystemGlobalTimeoutChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 1, 3, 48)
)
sleSystemGlobalTimeoutChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemControlGlobalTimeoutMin"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "copyOfsleSystemControlGlobalTimeoutSec"))
)
if mibBuilder.loadTexts:
    sleSystemGlobalTimeoutChanged.setStatus(
        "current"
    )

sleDNSServerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 3, 1)
)
sleDNSServerCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerName"))
)
if mibBuilder.loadTexts:
    sleDNSServerCreated.setStatus(
        "current"
    )

sleDNSServerDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 3, 2)
)
sleDNSServerDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlIndex"))
)
if mibBuilder.loadTexts:
    sleDNSServerDestroyed.setStatus(
        "current"
    )

sleDNSServerExCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 2, 3, 3)
)
sleDNSServerExCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDnsServerAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDnsServerAddress"))
)
if mibBuilder.loadTexts:
    sleDNSServerExCreated.setStatus(
        "current"
    )

sleBackupCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 3, 1)
)
sleBackupCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlSrcConfigFile"))
)
if mibBuilder.loadTexts:
    sleBackupCreated.setStatus(
        "current"
    )

sleBackupDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 3, 2)
)
sleBackupDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlSrcConfigFile"))
)
if mibBuilder.loadTexts:
    sleBackupDestroyed.setStatus(
        "current"
    )

sleBackupChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 3, 3)
)
sleBackupChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlSrcConfigFile"))
)
if mibBuilder.loadTexts:
    sleBackupChanged.setStatus(
        "current"
    )

sleBackupConfigBySftpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 3, 4)
)
sleBackupConfigBySftpChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlSrcConfigFile"))
)
if mibBuilder.loadTexts:
    sleBackupConfigBySftpChanged.setStatus(
        "current"
    )

sleBackupConfigByScpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 3, 5)
)
sleBackupConfigByScpChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlSrcConfigFile"))
)
if mibBuilder.loadTexts:
    sleBackupConfigByScpChanged.setStatus(
        "current"
    )

sleBackupKeyBySftpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 3, 6)
)
sleBackupKeyBySftpChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlSrcConfigFile"))
)
if mibBuilder.loadTexts:
    sleBackupKeyBySftpChanged.setStatus(
        "current"
    )

sleBackupKeyByScpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 4, 3, 7)
)
sleBackupKeyByScpChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupControlSrcConfigFile"))
)
if mibBuilder.loadTexts:
    sleBackupKeyByScpChanged.setStatus(
        "current"
    )

sleNTPServerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 3, 1)
)
sleNTPServerCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerAuthenticationKey"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNtpServerVRFIndex"))
)
if mibBuilder.loadTexts:
    sleNTPServerCreated.setStatus(
        "current"
    )

sleNTPServerDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 6, 3, 2)
)
sleNTPServerDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerControlName"))
)
if mibBuilder.loadTexts:
    sleNTPServerDestroyed.setStatus(
        "current"
    )

sleSyslogConfCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 3, 1)
)
sleSyslogConfCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfFacility"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfSeverity"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfTarget"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfStorage"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfTargetAddress"))
)
if mibBuilder.loadTexts:
    sleSyslogConfCreated.setStatus(
        "current"
    )

sleSyslogConfDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 3, 2)
)
sleSyslogConfDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlIndex"))
)
if mibBuilder.loadTexts:
    sleSyslogConfDestroyed.setStatus(
        "current"
    )

sleSyslogConfExCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 3, 3)
)
sleSyslogConfExCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfMode"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfFacility"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfSeverity"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfTarget"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfStorage"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfRemoteAddrType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfRemoteAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfVRFIndex"))
)
if mibBuilder.loadTexts:
    sleSyslogConfExCreated.setStatus(
        "current"
    )

sleSyslogConfExDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 7, 3, 4)
)
sleSyslogConfExDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfControlTimeStamp"))
)
if mibBuilder.loadTexts:
    sleSyslogConfExDestroyed.setStatus(
        "current"
    )

sleSSHRemoteConnectiondestoryed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 10, 3, 1)
)
sleSSHRemoteConnectiondestoryed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlTImeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteControlIndex"))
)
if mibBuilder.loadTexts:
    sleSSHRemoteConnectiondestoryed.setStatus(
        "current"
    )

sleAutoCliStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 3, 1)
)
sleAutoCliStatusChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliConfStatus"))
)
if mibBuilder.loadTexts:
    sleAutoCliStatusChanged.setStatus(
        "current"
    )

sleAutoCliMemoryMaxsizeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 3, 2)
)
sleAutoCliMemoryMaxsizeChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliMemoryMaxSize"))
)
if mibBuilder.loadTexts:
    sleAutoCliMemoryMaxsizeChanged.setStatus(
        "current"
    )

sleAutoCliTransferIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 1, 3, 3)
)
sleAutoCliTransferIntervalChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliTransferInterval"))
)
if mibBuilder.loadTexts:
    sleAutoCliTransferIntervalChanged.setStatus(
        "current"
    )

sleAutoCliScriptFileFtpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 3, 1)
)
sleAutoCliScriptFileFtpCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileName"))
)
if mibBuilder.loadTexts:
    sleAutoCliScriptFileFtpCreated.setStatus(
        "current"
    )

sleAutoCliScriptFileTftpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 3, 2)
)
sleAutoCliScriptFileTftpCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileName"))
)
if mibBuilder.loadTexts:
    sleAutoCliScriptFileTftpCreated.setStatus(
        "current"
    )

sleAutoCliScriptFileDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 2, 3, 3)
)
sleAutoCliScriptFileDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileControlScriptName"))
)
if mibBuilder.loadTexts:
    sleAutoCliScriptFileDestroyed.setStatus(
        "current"
    )

sleAutoCliScheduleCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 3, 1)
)
sleAutoCliScheduleCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleYear"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleMonth"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleDay"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleMinute"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleScriptName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleTransferType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleOutputRule"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleProfileName"))
)
if mibBuilder.loadTexts:
    sleAutoCliScheduleCreated.setStatus(
        "current"
    )

sleAutoCliScheduleDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 3, 3, 2)
)
sleAutoCliScheduleDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlTimer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleControlName"))
)
if mibBuilder.loadTexts:
    sleAutoCliScheduleDestroyed.setStatus(
        "current"
    )

sleAutoCliProfileCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 3, 1)
)
sleAutoCliProfileCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileType"))
)
if mibBuilder.loadTexts:
    sleAutoCliProfileCreated.setStatus(
        "current"
    )

sleAutoCliProfileDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 4, 3, 2)
)
sleAutoCliProfileDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileControlName"))
)
if mibBuilder.loadTexts:
    sleAutoCliProfileDestroyed.setStatus(
        "current"
    )

sleAutoCliProfileServerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 3, 1)
)
sleAutoCliProfileServerCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerUser"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerDir"))
)
if mibBuilder.loadTexts:
    sleAutoCliProfileServerCreated.setStatus(
        "current"
    )

sleAutoCliProfileServerDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 3, 2)
)
sleAutoCliProfileServerDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlProfName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlIpAddress"))
)
if mibBuilder.loadTexts:
    sleAutoCliProfileServerDestroyed.setStatus(
        "current"
    )

sleAutoCliProfileServerAllDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 5, 3, 3)
)
sleAutoCliProfileServerAllDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerControlProfName"))
)
if mibBuilder.loadTexts:
    sleAutoCliProfileServerAllDestroyed.setStatus(
        "current"
    )

sleAutoCliOutputMemoryFileFtpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 3, 1)
)
sleAutoCliOutputMemoryFileFtpCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileName"))
)
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileFtpCreated.setStatus(
        "current"
    )

sleAutoCliOutputMemoryFileTftpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 3, 2)
)
sleAutoCliOutputMemoryFileTftpCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileName"))
)
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileTftpCreated.setStatus(
        "current"
    )

sleAutoCliOutputMemoryFileDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 11, 6, 3, 3)
)
sleAutoCliOutputMemoryFileDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlOutputFileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAutoCliOutputMemoryFileDestroyed.setStatus(
        "current"
    )

sleAutoResetPingStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 3, 1)
)
sleAutoResetPingStatusChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingConfStatus"))
)
if mibBuilder.loadTexts:
    sleAutoResetPingStatusChanged.setStatus(
        "current"
    )

sleAutoResetPingInfoModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 3, 2)
)
sleAutoResetPingInfoModified.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingIpAddress"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingTransactionInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingNumberOfRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRequestInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingTimeoutOfRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingLossThreshold"))
)
if mibBuilder.loadTexts:
    sleAutoResetPingInfoModified.setStatus(
        "current"
    )

sleAutoResetPingRebootCtrlModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 3, 3)
)
sleAutoResetPingRebootCtrlModified.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRebootThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRebootRecoveryTime"))
)
if mibBuilder.loadTexts:
    sleAutoResetPingRebootCtrlModified.setStatus(
        "current"
    )

sleAutoResetPingRebootCountClearSetted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 1, 3, 4)
)
sleAutoResetPingRebootCountClearSetted.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAutoResetPingRebootCountClearSetted.setStatus(
        "current"
    )

sleAutoResetMemoryleakStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 3, 1)
)
sleAutoResetMemoryleakStatusChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakContStatus"))
)
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakStatusChanged.setStatus(
        "current"
    )

sleAutoResetMemoryleakInfoModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 3, 2)
)
sleAutoResetMemoryleakInfoModified.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakMemThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakCheckInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakNumberOfVerification"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakVerificationInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakCountThreshold"))
)
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakInfoModified.setStatus(
        "current"
    )

sleAutoResetMemoryleakReboottimeModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 3, 3)
)
sleAutoResetMemoryleakReboottimeModified.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeStartHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeStartMin"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeEndHour"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeEndMin"))
)
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakReboottimeModified.setStatus(
        "current"
    )

sleAutoResetMemoryleakRebootCtrlModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 3, 4)
)
sleAutoResetMemoryleakRebootCtrlModified.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakRebootThreshold"))
)
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakRebootCtrlModified.setStatus(
        "current"
    )

sleAutoResetMemoryleakRebootCountClearSetted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 2, 3, 5)
)
sleAutoResetMemoryleakRebootCountClearSetted.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAutoResetMemoryleakRebootCountClearSetted.setStatus(
        "current"
    )

sleAutoResetCpuChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 3, 1)
)
sleAutoResetCpuChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlLoad"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlInterruptLoad"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlTime"))
)
if mibBuilder.loadTexts:
    sleAutoResetCpuChanged.setStatus(
        "current"
    )

sleAutoResetCpuDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 12, 3, 3, 2)
)
sleAutoResetCpuDeleted.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAutoResetCpuDeleted.setStatus(
        "current"
    )

sleCoreDumpEntryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 3, 1)
)
sleCoreDumpEntryCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpInfoPID"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpInfoStatus"))
)
if mibBuilder.loadTexts:
    sleCoreDumpEntryCreated.setStatus(
        "current"
    )

sleCoreDumpEntryDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 3, 2)
)
sleCoreDumpEntryDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpInfoPID"))
)
if mibBuilder.loadTexts:
    sleCoreDumpEntryDestroyed.setStatus(
        "current"
    )

sleCoreDumpEntryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 13, 3, 3)
)
sleCoreDumpEntryChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpFile"))
)
if mibBuilder.loadTexts:
    sleCoreDumpEntryChanged.setStatus(
        "current"
    )

sleServicePortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 3, 1)
)
sleServicePortChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServicePort"))
)
if mibBuilder.loadTexts:
    sleServicePortChanged.setStatus(
        "current"
    )

sleServiceAdminStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 14, 3, 2)
)
sleServiceAdminStatusChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceControlAdminStatus"))
)
if mibBuilder.loadTexts:
    sleServiceAdminStatusChanged.setStatus(
        "current"
    )

sleSystemUserCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 3, 1)
)
sleSystemUserCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserLevel"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserDesc"))
)
if mibBuilder.loadTexts:
    sleSystemUserCreated.setStatus(
        "current"
    )

sleSystemUserNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 3, 2)
)
sleSystemUserNameChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRename"))
)
if mibBuilder.loadTexts:
    sleSystemUserNameChanged.setStatus(
        "current"
    )

sleSystemUserPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 3, 3)
)
sleSystemUserPasswordChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserPassword"))
)
if mibBuilder.loadTexts:
    sleSystemUserPasswordChanged.setStatus(
        "current"
    )

sleSystemUserDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 3, 4)
)
sleSystemUserDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlName"))
)
if mibBuilder.loadTexts:
    sleSystemUserDestroyed.setStatus(
        "current"
    )

sleSystemUserLevelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 3, 5)
)
sleSystemUserLevelChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRequest"))
)
if mibBuilder.loadTexts:
    sleSystemUserLevelChanged.setStatus(
        "current"
    )

sleSystemUserLoginAttemptsFailureLogCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 15, 3, 6)
)
sleSystemUserLoginAttemptsFailureLogCleared.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserControlName"))
)
if mibBuilder.loadTexts:
    sleSystemUserLoginAttemptsFailureLogCleared.setStatus(
        "current"
    )

sleParameterCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 3, 1)
)
sleParameterCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterValue"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterMode"))
)
if mibBuilder.loadTexts:
    sleParameterCreated.setStatus(
        "current"
    )

sleParameterDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 3, 2)
)
sleParameterDestroyed.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlName"))
)
if mibBuilder.loadTexts:
    sleParameterDestroyed.setStatus(
        "current"
    )

sleParameterModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 3, 3)
)
sleParameterModeChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterMode"))
)
if mibBuilder.loadTexts:
    sleParameterModeChanged.setStatus(
        "current"
    )

sleParameterValueChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 16, 3, 4)
)
sleParameterValueChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterValue"))
)
if mibBuilder.loadTexts:
    sleParameterValueChanged.setStatus(
        "current"
    )

sleSwWatchdogCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 3, 1)
)
sleSwWatchdogCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogInterval"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogThreshold"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogAction"))
)
if mibBuilder.loadTexts:
    sleSwWatchdogCreated.setStatus(
        "current"
    )

sleSwWatchdogDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 17, 3, 2)
)
sleSwWatchdogDeleted.setObjects(
    ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogControlType")
)
if mibBuilder.loadTexts:
    sleSwWatchdogDeleted.setStatus(
        "current"
    )

sleAutoUpgradeProfileCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 3, 1)
)
sleAutoUpgradeProfileCreated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlOldVer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlNewVer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlPeriodType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlPeriodDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlTimeout"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRetry"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRegSec"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlReloadTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlModel"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileCreated.setStatus(
        "current"
    )

sleAutoUpgradeProfileDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 3, 2)
)
sleAutoUpgradeProfileDeleted.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlName"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileDeleted.setStatus(
        "current"
    )

sleAutoUpgradeProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 1, 3, 3)
)
sleAutoUpgradeProfileChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlOldVer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlNewVer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlSize"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlPeriodType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlPeriodDate"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlTimeout"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRetry"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlRegSec"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlReloadTime"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileControlModel"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeProfileChanged.setStatus(
        "current"
    )

sleAutoUpgradeSetOltProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 4, 1)
)
sleAutoUpgradeSetOltProfile.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlOltIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlFwType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlSlotType"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeSetOltProfile.setStatus(
        "current"
    )

sleAutoUpgradeUnSetOltProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 4, 2)
)
sleAutoUpgradeUnSetOltProfile.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlOltIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlFwType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlProfileName"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlSlotType"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeUnSetOltProfile.setStatus(
        "current"
    )

sleAutoUpgradeSetOntProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 4, 3)
)
sleAutoUpgradeSetOntProfile.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlOntIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlFwType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlProfileName"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeSetOntProfile.setStatus(
        "current"
    )

sleAutoUpgradeUnSetOntProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 2, 4, 4)
)
sleAutoUpgradeUnSetOntProfile.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlOntIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlFwType"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeMgmtControlProfileName"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeUnSetOntProfile.setStatus(
        "current"
    )

sleAutoUpgradeDeleteOltLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 3, 1)
)
sleAutoUpgradeDeleteOltLog.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlSlotIndex"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeDeleteOltLog.setStatus(
        "current"
    )

sleAutoUpgradeDeleteAllOltLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 3, 2)
)
sleAutoUpgradeDeleteAllOltLog.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeDeleteAllOltLog.setStatus(
        "current"
    )

sleAutoUpgradeDeleteOntLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 3, 3)
)
sleAutoUpgradeDeleteOntLog.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlOntIndex"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeDeleteOntLog.setStatus(
        "current"
    )

sleAutoUpgradeDeleteAllOntLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 3, 4)
)
sleAutoUpgradeDeleteAllOntLog.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlReqResult"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeDeleteAllOntLog.setStatus(
        "current"
    )

sleAutoUpgradeExportOltLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 3, 5)
)
sleAutoUpgradeExportOltLog.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlSlotIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlExportMethod"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlServer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlUser"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeExportOltLog.setStatus(
        "current"
    )

sleAutoUpgradeExportOntLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 18, 3, 3, 6)
)
sleAutoUpgradeExportOntLog.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlOntIndex"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlExportMethod"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlServer"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeLogControlUser"))
)
if mibBuilder.loadTexts:
    sleAutoUpgradeExportOntLog.setStatus(
        "current"
    )

sleWatchdogAdminStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 3, 1)
)
sleWatchdogAdminStatusChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlAdminStatus"))
)
if mibBuilder.loadTexts:
    sleWatchdogAdminStatusChanged.setStatus(
        "current"
    )

sleWatchdogTimeoutChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 3, 2)
)
sleWatchdogTimeoutChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlTimeout"))
)
if mibBuilder.loadTexts:
    sleWatchdogTimeoutChanged.setStatus(
        "current"
    )

sleWatchdogModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 19, 3, 3)
)
sleWatchdogModeChanged.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogControlMode"))
)
if mibBuilder.loadTexts:
    sleWatchdogModeChanged.setStatus(
        "current"
    )

sleFtpclientDirectoryInfoUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 100, 3, 1)
)
sleFtpclientDirectoryInfoUpdated.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlRequest"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlTimeStamp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlReqResult"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlServerIp"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlUserId"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlPassword"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientControlDirectoryPath"))
)
if mibBuilder.loadTexts:
    sleFtpclientDirectoryInfoUpdated.setStatus(
        "current"
    )


# Notifications groups

sleSystemMaintenanceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 1, 102)
)
sleSystemMaintenanceNotificationGroup.setObjects(
      *(("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSystemInfoProfileChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemCPUThresholdProfileChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDefaultOSChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemRTCProfileChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDNSDomainNameChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBannerProfileChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogProfileChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSSHStateChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNTPStateChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemOSProfileChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBackupChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBackupIntervalChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDhcpActivityChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemDefaultTTLChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindInterfaceNameChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogBindInterfaceNameCleared"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemConfigPortMoved"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemConfigPortCopied"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemConfigPortCleared"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSessionTimeChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemExecTimeoutChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemWatchdogStatusChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNosDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleNTPServerDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSSHRemoteConnectiondestoryed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliStatusChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliMemoryMaxsizeChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliTransferIntervalChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileFtpCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScheduleDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileFtpCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingStatusChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingInfoModified"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakStatusChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakInfoModified"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakReboottimeModified"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpEntryCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpEntryDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleCoreDumpEntryChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServicePortChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakRebootCountClearSetted"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetMemoryleakRebootCtrlModified"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRebootCountClearSetted"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterValueChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterModeChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleParameterCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetPingRebootCtrlModified"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindInterfaceChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemFtpBindInterfaceChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemRedundancyPortChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleRedundancyPortCleared"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupConfigBySftpChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupConfigByScpChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupKeyBySftpChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleBackupKeyByScpChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserNameChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserPasswordChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliScriptFileTftpCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileServerAllDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliOutputMemoryFileTftpCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSwWatchdogDeleted"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemTempThresholdChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemMemThresholdChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileDeleted"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeProfileChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeSetOltProfile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeUnSetOltProfile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeSetOntProfile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeUnSetOntProfile"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeDeleteOltLog"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeDeleteAllOltLog"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeDeleteOntLog"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeDeleteAllOntLog"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeExportOltLog"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoUpgradeExportOntLog"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemBootloaderProfileChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindAddressChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemEnablePasswdChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemEnableServicePasswdEncryptionChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleServiceAdminStatusChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserLevelChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemPasswdRestored"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpPollIntervalChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoResetCpuDeleted"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleFtpclientDirectoryInfoUpdated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemWebMgmtChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemUserLoginAttemptsFailureLogCleared"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAdministeredMacChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadInTimeChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadDailyTimeChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemAutoReloadAtTimeChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleAutoCliProfileDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemRestoreFactoryChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogAdminStatusChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogTimeoutChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemRetryWriteMemoryChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemGlobalTimeoutChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfExDestroyed"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleWatchdogModeChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemSyslogProfileExChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSystemNtpBindAddressExChanged"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleDNSServerExCreated"),
        ("SLE-SYSTEMMAINTENANCE-MIB", "sleSyslogConfExCreated"))
)
if mibBuilder.loadTexts:
    sleSystemMaintenanceNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-SYSTEMMAINTENANCE-MIB",
    **{"EnableFlag": EnableFlag,
       "SleDefAutoCliScheduleType": SleDefAutoCliScheduleType,
       "SleDefAutoCliScheduleTransferType": SleDefAutoCliScheduleTransferType,
       "SleDefAutoCliScheduleResult": SleDefAutoCliScheduleResult,
       "sleSystemMaintenance": sleSystemMaintenance,
       "sleSystemBase": sleSystemBase,
       "sleSystemBaseInfo": sleSystemBaseInfo,
       "sleSystemModelName": sleSystemModelName,
       "sleSystemSerialNumber": sleSystemSerialNumber,
       "sleSystemHWVersion": sleSystemHWVersion,
       "sleSystemBLVersion": sleSystemBLVersion,
       "sleSystemSWCompatibility": sleSystemSWCompatibility,
       "sleSystemOSVersion": sleSystemOSVersion,
       "sleSystemMacAddress": sleSystemMacAddress,
       "sleSystemHostName": sleSystemHostName,
       "sleSystemCPULoadAll": sleSystemCPULoadAll,
       "sleSystemCPULoadInterrupt": sleSystemCPULoadInterrupt,
       "sleSystemCPUThreshold": sleSystemCPUThreshold,
       "sleSystemCPUInterval": sleSystemCPUInterval,
       "sleSystemMemoryTotal": sleSystemMemoryTotal,
       "sleSystemMemoryFree": sleSystemMemoryFree,
       "sleSystemMemoryShared": sleSystemMemoryShared,
       "sleSystemMemoryBuffers": sleSystemMemoryBuffers,
       "sleSystemMemoryCached": sleSystemMemoryCached,
       "sleSystemMemorySwapTotal": sleSystemMemorySwapTotal,
       "sleSystemMemorySwapFree": sleSystemMemorySwapFree,
       "sleSystemDefaultOS": sleSystemDefaultOS,
       "sleSystemOS1Version": sleSystemOS1Version,
       "sleSystemOS1Size": sleSystemOS1Size,
       "sleSystemOS1BuildNumber": sleSystemOS1BuildNumber,
       "sleSystemOS2Version": sleSystemOS2Version,
       "sleSystemOS2Size": sleSystemOS2Size,
       "sleSystemOS2BuildNumber": sleSystemOS2BuildNumber,
       "sleSystemFlashTotalSize": sleSystemFlashTotalSize,
       "sleSystemFlashOSSize": sleSystemFlashOSSize,
       "sleSystemFlashConfigSize": sleSystemFlashConfigSize,
       "sleSystemFlashOSUsedSize": sleSystemFlashOSUsedSize,
       "sleSystemFlashConfigUsedSize": sleSystemFlashConfigUsedSize,
       "sleSystemClock": sleSystemClock,
       "sleSystemTimezone": sleSystemTimezone,
       "sleSystemDNSDomainName": sleSystemDNSDomainName,
       "sleSystemInitBanner": sleSystemInitBanner,
       "sleSystemSuccessBanner": sleSystemSuccessBanner,
       "sleSystemFailBanner": sleSystemFailBanner,
       "sleSystemSyslogState": sleSystemSyslogState,
       "sleSystemSyslogVolatileNumber": sleSystemSyslogVolatileNumber,
       "sleSystemSyslogNonVolatileNumber": sleSystemSyslogNonVolatileNumber,
       "sleSystemSyslogBindAddress": sleSystemSyslogBindAddress,
       "sleSystemSyslogLocalCode": sleSystemSyslogLocalCode,
       "sleSystemSSHState": sleSystemSSHState,
       "sleSystemNTPState": sleSystemNTPState,
       "sleSystemBackupInterval": sleSystemBackupInterval,
       "sleSystemDhcpActivity": sleSystemDhcpActivity,
       "sleSystemDefaultTTL": sleSystemDefaultTTL,
       "sleSystemSyslogVolatileSize": sleSystemSyslogVolatileSize,
       "sleSystemSyslogBindInterfaceName": sleSystemSyslogBindInterfaceName,
       "sleSystemSessionTime": sleSystemSessionTime,
       "sleSystemExecTimeout": sleSystemExecTimeout,
       "sleSystemWatchdogStatus": sleSystemWatchdogStatus,
       "sleSystemNtpBindInterface": sleSystemNtpBindInterface,
       "sleSystemFtpBindInterface": sleSystemFtpBindInterface,
       "sleSystemRedundancyPort": sleSystemRedundancyPort,
       "sleSystemSyslogVolatileMaxLine": sleSystemSyslogVolatileMaxLine,
       "sleSystemBootInfo": sleSystemBootInfo,
       "sleSystemTempHighThreshold": sleSystemTempHighThreshold,
       "sleSystemTempLowThreshold": sleSystemTempLowThreshold,
       "sleSystemMemThreshold": sleSystemMemThreshold,
       "sleSystemLowCPUThreshold": sleSystemLowCPUThreshold,
       "sleSystemLowCPUInterval": sleSystemLowCPUInterval,
       "sleSystemRunningOS": sleSystemRunningOS,
       "sleSystemNtpBindAddress": sleSystemNtpBindAddress,
       "sleSystemEnablePasswdType": sleSystemEnablePasswdType,
       "sleSystemEnablePasswd": sleSystemEnablePasswd,
       "sleSystemServicePasswdEncryption": sleSystemServicePasswdEncryption,
       "sleSystemUptime64": sleSystemUptime64,
       "sleSystemNtpPollnterval": sleSystemNtpPollnterval,
       "sleSystemCPUDuration": sleSystemCPUDuration,
       "sleSystemLowCPUDuration": sleSystemLowCPUDuration,
       "sleSystemBarcode": sleSystemBarcode,
       "sleSystemEnhancedFeature": sleSystemEnhancedFeature,
       "sleSystemGetBranchModel": sleSystemGetBranchModel,
       "sleSystemTargetId": sleSystemTargetId,
       "sleSystemNodeName": sleSystemNodeName,
       "sleSystemNetworkName": sleSystemNetworkName,
       "sleSystemShelfId": sleSystemShelfId,
       "sleSystemSlotId": sleSystemSlotId,
       "sleSystemWebMgmt": sleSystemWebMgmt,
       "sleSystemManufacturer": sleSystemManufacturer,
       "sleSystemManufactureDate": sleSystemManufactureDate,
       "sleSystemNosUpgradeStatus": sleSystemNosUpgradeStatus,
       "sleSystemAutoReloadInHour": sleSystemAutoReloadInHour,
       "sleSystemAutoReloadInMinutes": sleSystemAutoReloadInMinutes,
       "sleSystemAutoReloadDailyHour": sleSystemAutoReloadDailyHour,
       "sleSystemAutoReloadDailyMinutes": sleSystemAutoReloadDailyMinutes,
       "sleSystemAutoReloadAtYear": sleSystemAutoReloadAtYear,
       "sleSystemAutoReloadAtMonth": sleSystemAutoReloadAtMonth,
       "sleSystemAutoReloadAtDay": sleSystemAutoReloadAtDay,
       "sleSystemAutpReloadAtHour": sleSystemAutpReloadAtHour,
       "sleSystemAutpReloadAtMinutes": sleSystemAutpReloadAtMinutes,
       "sleSystemAdministeredMac": sleSystemAdministeredMac,
       "sleSystemBaseMac": sleSystemBaseMac,
       "sleSystemSyslogBindAddrType": sleSystemSyslogBindAddrType,
       "sleSystemSyslogBindIPAddress": sleSystemSyslogBindIPAddress,
       "sleSystemNtpBindAddrType": sleSystemNtpBindAddrType,
       "sleSystemNtpBindIPAddress": sleSystemNtpBindIPAddress,
       "sleSystemPLDversion": sleSystemPLDversion,
       "sleSysetmGlobalTimeoutMin": sleSysetmGlobalTimeoutMin,
       "sleSysetmGlobalTimeoutSec": sleSysetmGlobalTimeoutSec,
       "sleSystemCPULoad5s": sleSystemCPULoad5s,
       "sleSystemCPULoad1m": sleSystemCPULoad1m,
       "sleSystemCPULoad10m": sleSystemCPULoad10m,
       "sleSystemBaseControl": sleSystemBaseControl,
       "sleSystemControlRequest": sleSystemControlRequest,
       "sleSystemControlStatus": sleSystemControlStatus,
       "sleSystemControlTimer": sleSystemControlTimer,
       "sleSystemControlTimeStamp": sleSystemControlTimeStamp,
       "sleSystemControlReqResult": sleSystemControlReqResult,
       "sleSystemControlHostName": sleSystemControlHostName,
       "sleSystemControlCPUThreshold": sleSystemControlCPUThreshold,
       "sleSystemControlCPUInterval": sleSystemControlCPUInterval,
       "sleSystemControlDefaultOS": sleSystemControlDefaultOS,
       "sleSystemControlClock": sleSystemControlClock,
       "sleSystemControlTimezone": sleSystemControlTimezone,
       "sleSystemControlDNSDomainName": sleSystemControlDNSDomainName,
       "sleSystemControlInitBanner": sleSystemControlInitBanner,
       "sleSystemControlSuccessBanner": sleSystemControlSuccessBanner,
       "sleSystemControlFailBanner": sleSystemControlFailBanner,
       "sleSystemControlSyslogState": sleSystemControlSyslogState,
       "sleSystemControlSyslogVolatileNumber": sleSystemControlSyslogVolatileNumber,
       "sleSystemControlSyslogNonVolatileNumber": sleSystemControlSyslogNonVolatileNumber,
       "sleSystemControlSyslogBindAddress": sleSystemControlSyslogBindAddress,
       "sleSystemControlSyslogLocalCode": sleSystemControlSyslogLocalCode,
       "sleSystemControlSSHState": sleSystemControlSSHState,
       "sleSystemControlNTPState": sleSystemControlNTPState,
       "sleSystemControlOSUpgradeNumber": sleSystemControlOSUpgradeNumber,
       "sleSystemControlServerAddress": sleSystemControlServerAddress,
       "sleSystemControlUpDownFlag": sleSystemControlUpDownFlag,
       "sleSystemControlUserID": sleSystemControlUserID,
       "sleSystemControlPassword": sleSystemControlPassword,
       "sleSystemControlFileName": sleSystemControlFileName,
       "sleSystemControlBackupFlag": sleSystemControlBackupFlag,
       "sleSystemControlReloadOS": sleSystemControlReloadOS,
       "sleSystemControlBackupInterval": sleSystemControlBackupInterval,
       "sleSystemControlDhcpActivity": sleSystemControlDhcpActivity,
       "sleSystemControlDefaultTTL": sleSystemControlDefaultTTL,
       "sleSystemControlSyslogVolatileSize": sleSystemControlSyslogVolatileSize,
       "sleSystemControlSyslogBindInterfaceName": sleSystemControlSyslogBindInterfaceName,
       "sleSystemControlSrcPort": sleSystemControlSrcPort,
       "sleSystemControlDstPort": sleSystemControlDstPort,
       "sleSystemControlSessionTime": sleSystemControlSessionTime,
       "sleSystemControlExecTimeout": sleSystemControlExecTimeout,
       "sleSystemControlWatchdogStatus": sleSystemControlWatchdogStatus,
       "sleSystemControlClearOs": sleSystemControlClearOs,
       "sleSystemControlNtpBindInterface": sleSystemControlNtpBindInterface,
       "sleSystemControlFtpBindInterface": sleSystemControlFtpBindInterface,
       "sleSystemControlSyslogVolMaxLine": sleSystemControlSyslogVolMaxLine,
       "sleSystemControlTempHighThreshold": sleSystemControlTempHighThreshold,
       "sleSystemControlTempLowThreshold": sleSystemControlTempLowThreshold,
       "sleSystemControlMemThreshold": sleSystemControlMemThreshold,
       "sleSystemControlLowCPUThreshold": sleSystemControlLowCPUThreshold,
       "sleSystemControlLowCPUInterval": sleSystemControlLowCPUInterval,
       "sleSystemControlNtpBindAddress": sleSystemControlNtpBindAddress,
       "sleSystemControlEnablePasswdType": sleSystemControlEnablePasswdType,
       "sleSystemControlEnablePasswd": sleSystemControlEnablePasswd,
       "sleSystemControlServicePasswdEncryption": sleSystemControlServicePasswdEncryption,
       "sleSystemControlNtpPollInterval": sleSystemControlNtpPollInterval,
       "sleSystemControlCPUDuration": sleSystemControlCPUDuration,
       "sleSystemControlLowCPUDuration": sleSystemControlLowCPUDuration,
       "sleSystemControlWebMgmt": sleSystemControlWebMgmt,
       "sleSystemControlAutoReloadYear": sleSystemControlAutoReloadYear,
       "sleSystemControlAutoReloadMonth": sleSystemControlAutoReloadMonth,
       "sleSystemControlAutoReloadDay": sleSystemControlAutoReloadDay,
       "sleSystemControlAutoReloadHour": sleSystemControlAutoReloadHour,
       "sleSystemControlAutoReloadMinutes": sleSystemControlAutoReloadMinutes,
       "sleSystemControlAdministeredMac": sleSystemControlAdministeredMac,
       "sleSystemControlSyslogBindAddrType": sleSystemControlSyslogBindAddrType,
       "sleSystemControlSyslogBindIPAddress": sleSystemControlSyslogBindIPAddress,
       "sleSystemControlNtpBindAddrType": sleSystemControlNtpBindAddrType,
       "sleSystemControlNtpBindIPAddress": sleSystemControlNtpBindIPAddress,
       "sleSystemControlWriteMemRetryCount": sleSystemControlWriteMemRetryCount,
       "sleSystemControlWriteMemRetryInterval": sleSystemControlWriteMemRetryInterval,
       "sleSystemControlGlobalTimeoutMin": sleSystemControlGlobalTimeoutMin,
       "sleSystemControlGlobalTimeoutSec": sleSystemControlGlobalTimeoutSec,
       "sleSystemBaseNotification": sleSystemBaseNotification,
       "sleSystemSystemInfoProfileChanged": sleSystemSystemInfoProfileChanged,
       "sleSystemCPUThresholdProfileChanged": sleSystemCPUThresholdProfileChanged,
       "sleSystemDefaultOSChanged": sleSystemDefaultOSChanged,
       "sleSystemRTCProfileChanged": sleSystemRTCProfileChanged,
       "sleSystemDNSDomainNameChanged": sleSystemDNSDomainNameChanged,
       "sleSystemBannerProfileChanged": sleSystemBannerProfileChanged,
       "sleSystemSyslogProfileChanged": sleSystemSyslogProfileChanged,
       "sleSystemSSHStateChanged": sleSystemSSHStateChanged,
       "sleSystemNTPStateChanged": sleSystemNTPStateChanged,
       "sleSystemOSProfileChanged": sleSystemOSProfileChanged,
       "sleSystemBackupChanged": sleSystemBackupChanged,
       "sleSystemBackupIntervalChanged": sleSystemBackupIntervalChanged,
       "sleSystemDhcpActivityChanged": sleSystemDhcpActivityChanged,
       "sleSystemDefaultTTLChanged": sleSystemDefaultTTLChanged,
       "sleSystemSyslogBindInterfaceNameChanged": sleSystemSyslogBindInterfaceNameChanged,
       "sleSystemSyslogBindInterfaceNameCleared": sleSystemSyslogBindInterfaceNameCleared,
       "sleSystemConfigPortMoved": sleSystemConfigPortMoved,
       "sleSystemConfigPortCopied": sleSystemConfigPortCopied,
       "sleSystemConfigPortCleared": sleSystemConfigPortCleared,
       "sleSystemSessionTimeChanged": sleSystemSessionTimeChanged,
       "sleSystemExecTimeoutChanged": sleSystemExecTimeoutChanged,
       "sleSystemWatchdogStatusChanged": sleSystemWatchdogStatusChanged,
       "sleSystemNosDestroyed": sleSystemNosDestroyed,
       "sleSystemNtpBindInterfaceChanged": sleSystemNtpBindInterfaceChanged,
       "sleSystemFtpBindInterfaceChanged": sleSystemFtpBindInterfaceChanged,
       "sleSystemRedundancyPortChanged": sleSystemRedundancyPortChanged,
       "sleRedundancyPortCleared": sleRedundancyPortCleared,
       "sleSystemTempThresholdChanged": sleSystemTempThresholdChanged,
       "sleSystemMemThresholdChanged": sleSystemMemThresholdChanged,
       "sleSystemBootloaderProfileChanged": sleSystemBootloaderProfileChanged,
       "sleSystemNtpBindAddressChanged": sleSystemNtpBindAddressChanged,
       "sleSystemEnablePasswdChanged": sleSystemEnablePasswdChanged,
       "sleSystemEnableServicePasswdEncryptionChanged": sleSystemEnableServicePasswdEncryptionChanged,
       "sleSystemPasswdRestored": sleSystemPasswdRestored,
       "sleSystemNtpPollIntervalChanged": sleSystemNtpPollIntervalChanged,
       "sleSystemRestoreFactoryChanged": sleSystemRestoreFactoryChanged,
       "sleSystemWebMgmtChanged": sleSystemWebMgmtChanged,
       "sleSystemAutoReloadInTimeChanged": sleSystemAutoReloadInTimeChanged,
       "sleSystemAutoReloadDailyTimeChanged": sleSystemAutoReloadDailyTimeChanged,
       "sleSystemAutoReloadAtTimeChanged": sleSystemAutoReloadAtTimeChanged,
       "sleSystemAdministeredMacChanged": sleSystemAdministeredMacChanged,
       "sleSystemSyslogProfileExChanged": sleSystemSyslogProfileExChanged,
       "sleSystemNtpBindAddressExChanged": sleSystemNtpBindAddressExChanged,
       "sleSystemRetryWriteMemoryChanged": sleSystemRetryWriteMemoryChanged,
       "sleSystemGlobalTimeoutChanged": sleSystemGlobalTimeoutChanged,
       "sleSystemBaseSlotInfo": sleSystemBaseSlotInfo,
       "sleSystemBaseSlotInfoTable": sleSystemBaseSlotInfoTable,
       "sleSystemBaseSlotInfoEntry": sleSystemBaseSlotInfoEntry,
       "sleSystemSlotIndex": sleSystemSlotIndex,
       "sleSystemSlotUptime": sleSystemSlotUptime,
       "sleSystemSlotModelName": sleSystemSlotModelName,
       "sleSystemSlotSerialNumber": sleSystemSlotSerialNumber,
       "sleSystemSlotHWVersion": sleSystemSlotHWVersion,
       "sleSystemSlotBLVersion": sleSystemSlotBLVersion,
       "sleSystemSlotSWCompatibility": sleSystemSlotSWCompatibility,
       "sleSystemSlotOSVersion": sleSystemSlotOSVersion,
       "sleSystemSlotMacAddress": sleSystemSlotMacAddress,
       "sleSystemSlotCPULoadAll": sleSystemSlotCPULoadAll,
       "sleSystemSlotCPULoadInterrupt": sleSystemSlotCPULoadInterrupt,
       "sleSystemSlotMemoryTotal": sleSystemSlotMemoryTotal,
       "sleSystemSlotMemoryFree": sleSystemSlotMemoryFree,
       "sleSystemSlotMemoryShared": sleSystemSlotMemoryShared,
       "sleSystemSlotMemoryBuffers": sleSystemSlotMemoryBuffers,
       "sleSystemSlotMemoryCached": sleSystemSlotMemoryCached,
       "sleSystemSlotMemorySwapTotal": sleSystemSlotMemorySwapTotal,
       "sleSystemSlotMemorySwapFree": sleSystemSlotMemorySwapFree,
       "sleSystemSlotBootReason": sleSystemSlotBootReason,
       "sleSystemSlotBootTime": sleSystemSlotBootTime,
       "sleSystemSlotVoltage": sleSystemSlotVoltage,
       "sleDNSServer": sleDNSServer,
       "sleDNSServerTable": sleDNSServerTable,
       "sleDNSServerEntry": sleDNSServerEntry,
       "sleDNSServerIndex": sleDNSServerIndex,
       "sleDNSServerName": sleDNSServerName,
       "sleDnsServerAddrType": sleDnsServerAddrType,
       "sleDnsServerAddress": sleDnsServerAddress,
       "sleDNSServerControl": sleDNSServerControl,
       "sleDNSServerControlRequest": sleDNSServerControlRequest,
       "sleDNSServerControlStatus": sleDNSServerControlStatus,
       "sleDNSServerControlTimer": sleDNSServerControlTimer,
       "sleDNSServerControlTImeStamp": sleDNSServerControlTImeStamp,
       "sleDNSServerControlReqResult": sleDNSServerControlReqResult,
       "sleDNSServerControlIndex": sleDNSServerControlIndex,
       "sleDNSServerControlName": sleDNSServerControlName,
       "sleDnsServerControlAddrType": sleDnsServerControlAddrType,
       "sleDnsServerControlAddress": sleDnsServerControlAddress,
       "sleDNSServerNotification": sleDNSServerNotification,
       "sleDNSServerCreated": sleDNSServerCreated,
       "sleDNSServerDestroyed": sleDNSServerDestroyed,
       "sleDNSServerExCreated": sleDNSServerExCreated,
       "sleLogin": sleLogin,
       "sleLoginTable": sleLoginTable,
       "sleLoginEntry": sleLoginEntry,
       "sleLoginIndex": sleLoginIndex,
       "sleLoginUser": sleLoginUser,
       "sleLoginTTY": sleLoginTTY,
       "sleLoginRemote": sleLoginRemote,
       "sleLoginTime": sleLoginTime,
       "sleBackup": sleBackup,
       "sleBackupTable": sleBackupTable,
       "sleBackupEntry": sleBackupEntry,
       "sleBackupConfigFile": sleBackupConfigFile,
       "sleBackupControl": sleBackupControl,
       "sleBackupControlRequest": sleBackupControlRequest,
       "sleBackupControlStatus": sleBackupControlStatus,
       "sleBackupControlTimer": sleBackupControlTimer,
       "sleBackupControlTimeStamp": sleBackupControlTimeStamp,
       "sleBackupControlReqResult": sleBackupControlReqResult,
       "sleBackupControlCreateMode": sleBackupControlCreateMode,
       "sleBackupControlServerIP": sleBackupControlServerIP,
       "sleBackupControlUserID": sleBackupControlUserID,
       "sleBackupControlPassword": sleBackupControlPassword,
       "sleBackupControlSrcConfigFile": sleBackupControlSrcConfigFile,
       "sleBackupControlDstConfigFile": sleBackupControlDstConfigFile,
       "sleBackupControlServerAddrType": sleBackupControlServerAddrType,
       "sleBackupControlServerAddress": sleBackupControlServerAddress,
       "sleBackupNotification": sleBackupNotification,
       "sleBackupCreated": sleBackupCreated,
       "sleBackupDestroyed": sleBackupDestroyed,
       "sleBackupChanged": sleBackupChanged,
       "sleBackupConfigBySftpChanged": sleBackupConfigBySftpChanged,
       "sleBackupConfigByScpChanged": sleBackupConfigByScpChanged,
       "sleBackupKeyBySftpChanged": sleBackupKeyBySftpChanged,
       "sleBackupKeyByScpChanged": sleBackupKeyByScpChanged,
       "sleProcess": sleProcess,
       "sleProcessTable": sleProcessTable,
       "sleProcessEntry": sleProcessEntry,
       "sleProcessID": sleProcessID,
       "sleProcessUser": sleProcessUser,
       "sleProcessCPU": sleProcessCPU,
       "sleProcessMemory": sleProcessMemory,
       "sleProcessVSZ": sleProcessVSZ,
       "sleProcessRSS": sleProcessRSS,
       "sleProcessTerminal": sleProcessTerminal,
       "sleProcessStatus": sleProcessStatus,
       "sleProcessStartTime": sleProcessStartTime,
       "sleProcessUsedTime": sleProcessUsedTime,
       "sleProcessCommand": sleProcessCommand,
       "sleNTP": sleNTP,
       "sleNTPServerTable": sleNTPServerTable,
       "sleNTPServerEntry": sleNTPServerEntry,
       "sleNTPServerName": sleNTPServerName,
       "sleNtpServerAuthenticationKey": sleNtpServerAuthenticationKey,
       "sleNtpServerVRFIndex": sleNtpServerVRFIndex,
       "sleNtpServerPrefer": sleNtpServerPrefer,
       "sleNtpServerVersion": sleNtpServerVersion,
       "sleNTPServerControl": sleNTPServerControl,
       "sleNTPServerControlRequest": sleNTPServerControlRequest,
       "sleNTPServerControlStatus": sleNTPServerControlStatus,
       "sleNTPServerControlTimer": sleNTPServerControlTimer,
       "sleNTPServerControlTImeStamp": sleNTPServerControlTImeStamp,
       "sleNTPServerControlReqResult": sleNTPServerControlReqResult,
       "sleNTPServerControlName": sleNTPServerControlName,
       "sleNtpServerControlAuthenticationKey": sleNtpServerControlAuthenticationKey,
       "sleNtpServerControlVRFIndex": sleNtpServerControlVRFIndex,
       "sleNtpServerControlType": sleNtpServerControlType,
       "sleNtpServerControlPrefer": sleNtpServerControlPrefer,
       "sleNtpServerControlVersion": sleNtpServerControlVersion,
       "sleNTPServerNotification": sleNTPServerNotification,
       "sleNTPServerCreated": sleNTPServerCreated,
       "sleNTPServerDestroyed": sleNTPServerDestroyed,
       "sleSyslogConf": sleSyslogConf,
       "sleSyslogConfTable": sleSyslogConfTable,
       "sleSyslogConfEntry": sleSyslogConfEntry,
       "sleSyslogConfIndex": sleSyslogConfIndex,
       "sleSyslogConfMode": sleSyslogConfMode,
       "sleSyslogConfFacility": sleSyslogConfFacility,
       "sleSyslogConfSeverity": sleSyslogConfSeverity,
       "sleSyslogConfTarget": sleSyslogConfTarget,
       "sleSyslogConfStorage": sleSyslogConfStorage,
       "sleSyslogConfTargetAddress": sleSyslogConfTargetAddress,
       "sleSyslogConfRemoteAddrType": sleSyslogConfRemoteAddrType,
       "sleSyslogConfRemoteAddress": sleSyslogConfRemoteAddress,
       "sleSyslogConfVRFIndex": sleSyslogConfVRFIndex,
       "sleSyslogConfSlotIndex": sleSyslogConfSlotIndex,
       "sleSyslogConfControl": sleSyslogConfControl,
       "sleSyslogConfControlRequest": sleSyslogConfControlRequest,
       "sleSyslogConfControlStatus": sleSyslogConfControlStatus,
       "sleSyslogConfControlTimer": sleSyslogConfControlTimer,
       "sleSyslogConfControlTimeStamp": sleSyslogConfControlTimeStamp,
       "sleSyslogConfControlReqResult": sleSyslogConfControlReqResult,
       "sleSyslogConfControlIndex": sleSyslogConfControlIndex,
       "sleSyslogConfControlMode": sleSyslogConfControlMode,
       "sleSyslogConfControlSeverity": sleSyslogConfControlSeverity,
       "sleSyslogConfControlFacility": sleSyslogConfControlFacility,
       "sleSyslogConfControlTarget": sleSyslogConfControlTarget,
       "sleSyslogConfControlStorage": sleSyslogConfControlStorage,
       "sleSyslogConfControlTargetAddress": sleSyslogConfControlTargetAddress,
       "sleSyslogConfControlRemoteAddrType": sleSyslogConfControlRemoteAddrType,
       "sleSyslogConfControlRemoteAddress": sleSyslogConfControlRemoteAddress,
       "sleSyslogConfControlVRFIndex": sleSyslogConfControlVRFIndex,
       "sleSyslogConfControlSlotIndex": sleSyslogConfControlSlotIndex,
       "sleSyslogConfNotification": sleSyslogConfNotification,
       "sleSyslogConfCreated": sleSyslogConfCreated,
       "sleSyslogConfDestroyed": sleSyslogConfDestroyed,
       "sleSyslogConfExCreated": sleSyslogConfExCreated,
       "sleSyslogConfExDestroyed": sleSyslogConfExDestroyed,
       "sleSyslogHistVol": sleSyslogHistVol,
       "sleSyslogHistVolTable": sleSyslogHistVolTable,
       "sleSyslogHistVolEntry": sleSyslogHistVolEntry,
       "sleSyslogHistVolIndex": sleSyslogHistVolIndex,
       "sleSyslogHistVolMsgText": sleSyslogHistVolMsgText,
       "sleSyslogHistVolTime": sleSyslogHistVolTime,
       "sleSyslogHistNVol": sleSyslogHistNVol,
       "sleSyslogHistNVolTable": sleSyslogHistNVolTable,
       "sleSyslogHistNVolEntry": sleSyslogHistNVolEntry,
       "sleSyslogHistNVolIndex": sleSyslogHistNVolIndex,
       "sleSyslogHistNVolMsgText": sleSyslogHistNVolMsgText,
       "sleSyslogHistNVolTime": sleSyslogHistNVolTime,
       "sleSSHRemote": sleSSHRemote,
       "sleSSHRemoteTable": sleSSHRemoteTable,
       "sleSSHRemoteEntry": sleSSHRemoteEntry,
       "sleSSHRemoteIndex": sleSSHRemoteIndex,
       "sleSSHRemoteUser": sleSSHRemoteUser,
       "sleSSHRemoteHost": sleSSHRemoteHost,
       "sleSSHRemoteTime": sleSSHRemoteTime,
       "sleSSHRemoteFromHost": sleSSHRemoteFromHost,
       "sleSSHRemoteControl": sleSSHRemoteControl,
       "sleSSHRemoteControlRequest": sleSSHRemoteControlRequest,
       "sleSSHRemoteControlStatus": sleSSHRemoteControlStatus,
       "sleSSHRemoteControlTimer": sleSSHRemoteControlTimer,
       "sleSSHRemoteControlTImeStamp": sleSSHRemoteControlTImeStamp,
       "sleSSHRemoteControlReqResult": sleSSHRemoteControlReqResult,
       "sleSSHRemoteControlIndex": sleSSHRemoteControlIndex,
       "sleSSHRemoteNotification": sleSSHRemoteNotification,
       "sleSSHRemoteConnectiondestoryed": sleSSHRemoteConnectiondestoryed,
       "sleAutoCli": sleAutoCli,
       "sleAutoCliInfo": sleAutoCliInfo,
       "sleAutoCliBase": sleAutoCliBase,
       "sleAutoCliConfStatus": sleAutoCliConfStatus,
       "sleAutoCliMemoryMaxSize": sleAutoCliMemoryMaxSize,
       "sleAutoCliMemoryUsedsize": sleAutoCliMemoryUsedsize,
       "sleAutoCliMemoryFreesize": sleAutoCliMemoryFreesize,
       "sleAutoCliTransferInterval": sleAutoCliTransferInterval,
       "sleAutoCliBaseControl": sleAutoCliBaseControl,
       "sleAutoCliControlRequest": sleAutoCliControlRequest,
       "sleAutoCliControlStatus": sleAutoCliControlStatus,
       "sleAutoCliControlTimer": sleAutoCliControlTimer,
       "sleAutoCliControlTimeStamp": sleAutoCliControlTimeStamp,
       "sleAutoCliControlReqResult": sleAutoCliControlReqResult,
       "sleAutoCliControlConfStatus": sleAutoCliControlConfStatus,
       "sleAutoCliControlMemoryMaxsize": sleAutoCliControlMemoryMaxsize,
       "sleAutoCliControlTransferInterval": sleAutoCliControlTransferInterval,
       "sleAutoCliBaseNotification": sleAutoCliBaseNotification,
       "sleAutoCliStatusChanged": sleAutoCliStatusChanged,
       "sleAutoCliMemoryMaxsizeChanged": sleAutoCliMemoryMaxsizeChanged,
       "sleAutoCliTransferIntervalChanged": sleAutoCliTransferIntervalChanged,
       "sleAutoCliScriptFile": sleAutoCliScriptFile,
       "sleAutoCliScriptFileTable": sleAutoCliScriptFileTable,
       "sleAutoCliScriptFileEntry": sleAutoCliScriptFileEntry,
       "sleAutoCliScriptId": sleAutoCliScriptId,
       "sleAutoCliScriptFileName": sleAutoCliScriptFileName,
       "sleAutoCliScriptFileUser": sleAutoCliScriptFileUser,
       "sleAutoCliScriptFileSize": sleAutoCliScriptFileSize,
       "sleAutoCliScriptFileUpdateTime": sleAutoCliScriptFileUpdateTime,
       "sleAutoCliScriptFileControl": sleAutoCliScriptFileControl,
       "sleAutoCliScriptFileControlRequest": sleAutoCliScriptFileControlRequest,
       "sleAutoCliScriptFileControlStatus": sleAutoCliScriptFileControlStatus,
       "sleAutoCliScriptFileControlTimer": sleAutoCliScriptFileControlTimer,
       "sleAutoCliScriptFileControlTimeStamp": sleAutoCliScriptFileControlTimeStamp,
       "sleAutoCliScriptFileControlReqResult": sleAutoCliScriptFileControlReqResult,
       "sleAutoCliScriptFileControlIpAddress": sleAutoCliScriptFileControlIpAddress,
       "sleAutoCliScriptFileControlUserName": sleAutoCliScriptFileControlUserName,
       "sleAutoCliScriptFileControlPassword": sleAutoCliScriptFileControlPassword,
       "sleAutoCliScriptFileControlFilePath": sleAutoCliScriptFileControlFilePath,
       "sleAutoCliScriptFileControlScriptName": sleAutoCliScriptFileControlScriptName,
       "sleAutoCliScriptFileNotifications": sleAutoCliScriptFileNotifications,
       "sleAutoCliScriptFileFtpCreated": sleAutoCliScriptFileFtpCreated,
       "sleAutoCliScriptFileTftpCreated": sleAutoCliScriptFileTftpCreated,
       "sleAutoCliScriptFileDestroyed": sleAutoCliScriptFileDestroyed,
       "sleAutoCliSchedule": sleAutoCliSchedule,
       "sleAutoCliScheduleTable": sleAutoCliScheduleTable,
       "sleAutoCliScheduleEntry": sleAutoCliScheduleEntry,
       "sleAutoCliScheduleName": sleAutoCliScheduleName,
       "sleAutoCliScheduleType": sleAutoCliScheduleType,
       "sleAutoCliScheduleInterval": sleAutoCliScheduleInterval,
       "sleAutoCliScheduleYear": sleAutoCliScheduleYear,
       "sleAutoCliScheduleMonth": sleAutoCliScheduleMonth,
       "sleAutoCliScheduleDay": sleAutoCliScheduleDay,
       "sleAutoCliScheduleHour": sleAutoCliScheduleHour,
       "sleAutoCliScheduleMinute": sleAutoCliScheduleMinute,
       "sleAutoCliScheduleScriptName": sleAutoCliScheduleScriptName,
       "sleAutoCliScheduleTransferType": sleAutoCliScheduleTransferType,
       "sleAutoCliScheduleLastExecutedTime": sleAutoCliScheduleLastExecutedTime,
       "sleAutoCliScheduleOutputRule": sleAutoCliScheduleOutputRule,
       "sleAutoCliScheduleLastResult": sleAutoCliScheduleLastResult,
       "sleAutoCliScheduleProfileName": sleAutoCliScheduleProfileName,
       "sleAutoCliScheduleControl": sleAutoCliScheduleControl,
       "sleAutoCliScheduleControlRequest": sleAutoCliScheduleControlRequest,
       "sleAutoCliScheduleControlStatus": sleAutoCliScheduleControlStatus,
       "sleAutoCliScheduleControlTimer": sleAutoCliScheduleControlTimer,
       "sleAutoCliScheduleControlTimeStamp": sleAutoCliScheduleControlTimeStamp,
       "sleAutoCliScheduleControlReqResult": sleAutoCliScheduleControlReqResult,
       "sleAutoCliScheduleControlName": sleAutoCliScheduleControlName,
       "sleAutoCliScheduleControlType": sleAutoCliScheduleControlType,
       "sleAutoCliScheduleControlInterval": sleAutoCliScheduleControlInterval,
       "sleAutoCliScheduleControlYear": sleAutoCliScheduleControlYear,
       "sleAutoCliScheduleControlMonth": sleAutoCliScheduleControlMonth,
       "sleAutoCliScheduleControlDay": sleAutoCliScheduleControlDay,
       "sleAutoCliScheduleControlHour": sleAutoCliScheduleControlHour,
       "sleAutoCliScheduleControlMinute": sleAutoCliScheduleControlMinute,
       "sleAutoCliScheduleControlScriptName": sleAutoCliScheduleControlScriptName,
       "sleAutoCliScheduleControlTransferType": sleAutoCliScheduleControlTransferType,
       "sleAutoCliScheduleControlOutputRule": sleAutoCliScheduleControlOutputRule,
       "sleAutoCliScheduleControlProfileName": sleAutoCliScheduleControlProfileName,
       "sleAutoCliScheduleNotifications": sleAutoCliScheduleNotifications,
       "sleAutoCliScheduleCreated": sleAutoCliScheduleCreated,
       "sleAutoCliScheduleDestroyed": sleAutoCliScheduleDestroyed,
       "sleAutoCliProfile": sleAutoCliProfile,
       "sleAutoCliProfileTable": sleAutoCliProfileTable,
       "sleAutoCliProfileEntry": sleAutoCliProfileEntry,
       "sleAutoCliProfileName": sleAutoCliProfileName,
       "sleAutoCliProfileType": sleAutoCliProfileType,
       "sleAutoCliProfileControl": sleAutoCliProfileControl,
       "sleAutoCliProfileControlRequest": sleAutoCliProfileControlRequest,
       "sleAutoCliProfileControlStatus": sleAutoCliProfileControlStatus,
       "sleAutoCliProfileControlTimer": sleAutoCliProfileControlTimer,
       "sleAutoCliProfileControlTimeStamp": sleAutoCliProfileControlTimeStamp,
       "sleAutoCliProfileControlReqResult": sleAutoCliProfileControlReqResult,
       "sleAutoCliProfileControlName": sleAutoCliProfileControlName,
       "sleAutoCliProfileControlType": sleAutoCliProfileControlType,
       "sleAutoCliProfileNotifications": sleAutoCliProfileNotifications,
       "sleAutoCliProfileCreated": sleAutoCliProfileCreated,
       "sleAutoCliProfileDestroyed": sleAutoCliProfileDestroyed,
       "sleAutoCliProfileServer": sleAutoCliProfileServer,
       "sleAutoCliProfileServerTable": sleAutoCliProfileServerTable,
       "sleAutoCliProfileServerEntry": sleAutoCliProfileServerEntry,
       "sleAutoCliProfileServerType": sleAutoCliProfileServerType,
       "sleAutoCliProfileServerIpAddress": sleAutoCliProfileServerIpAddress,
       "sleAutoCliProfileServerUser": sleAutoCliProfileServerUser,
       "sleAutoCliProfileServerPassword": sleAutoCliProfileServerPassword,
       "sleAutoCliProfileServerDir": sleAutoCliProfileServerDir,
       "sleAutoCliProfileServerControl": sleAutoCliProfileServerControl,
       "sleAutoCliProfileServerControlRequest": sleAutoCliProfileServerControlRequest,
       "sleAutoCliProfileServerControlStatus": sleAutoCliProfileServerControlStatus,
       "sleAutoCliProfileServerControlTimer": sleAutoCliProfileServerControlTimer,
       "sleAutoCliProfileServerControlTimeStamp": sleAutoCliProfileServerControlTimeStamp,
       "sleAutoCliProfileServerControlReqResult": sleAutoCliProfileServerControlReqResult,
       "sleAutoCliProfileServerControlProfName": sleAutoCliProfileServerControlProfName,
       "sleAutoCliProfileServerControlIpAddress": sleAutoCliProfileServerControlIpAddress,
       "sleAutoCliProfileServerControlUser": sleAutoCliProfileServerControlUser,
       "sleAutoCliProfileServerControlPassword": sleAutoCliProfileServerControlPassword,
       "sleAutoCliProfileServerControlDir": sleAutoCliProfileServerControlDir,
       "sleAutoCliProfileServerNotifications": sleAutoCliProfileServerNotifications,
       "sleAutoCliProfileServerCreated": sleAutoCliProfileServerCreated,
       "sleAutoCliProfileServerDestroyed": sleAutoCliProfileServerDestroyed,
       "sleAutoCliProfileServerAllDestroyed": sleAutoCliProfileServerAllDestroyed,
       "sleAutoCliOutputMemory": sleAutoCliOutputMemory,
       "sleAutoCliOutputMemoryFileTable": sleAutoCliOutputMemoryFileTable,
       "sleAutoCliOutputMemoryFileEntry": sleAutoCliOutputMemoryFileEntry,
       "sleAutoCliOutputMemoryFileId": sleAutoCliOutputMemoryFileId,
       "sleAutoCliOutputMemoryFileName": sleAutoCliOutputMemoryFileName,
       "sleAutoCliOutputMemoryFileSize": sleAutoCliOutputMemoryFileSize,
       "sleAutoCliOutputMemoryFileUpdatedTime": sleAutoCliOutputMemoryFileUpdatedTime,
       "sleAutoCliOutputMemoryFileControl": sleAutoCliOutputMemoryFileControl,
       "sleAutoCliOutputMemoryFileControlRequest": sleAutoCliOutputMemoryFileControlRequest,
       "sleAutoCliOutputMemoryFileControlStatus": sleAutoCliOutputMemoryFileControlStatus,
       "sleAutoCliOutputMemoryFileControlTimer": sleAutoCliOutputMemoryFileControlTimer,
       "sleAutoCliOutputMemoryFileControlTimeStamp": sleAutoCliOutputMemoryFileControlTimeStamp,
       "sleAutoCliOutputMemoryFileControlReqResult": sleAutoCliOutputMemoryFileControlReqResult,
       "sleAutoCliOutputMemoryFileControlServer": sleAutoCliOutputMemoryFileControlServer,
       "sleAutoCliOutputMemoryFileControlUserName": sleAutoCliOutputMemoryFileControlUserName,
       "sleAutoCliOutputMemoryFileControlPassword": sleAutoCliOutputMemoryFileControlPassword,
       "sleAutoCliOutputMemoryFileControlOutputFileName": sleAutoCliOutputMemoryFileControlOutputFileName,
       "sleAutoCliOutputMemoryFileControlRemotePath": sleAutoCliOutputMemoryFileControlRemotePath,
       "sleAutoCliOutputMemoryFileNotification": sleAutoCliOutputMemoryFileNotification,
       "sleAutoCliOutputMemoryFileFtpCreated": sleAutoCliOutputMemoryFileFtpCreated,
       "sleAutoCliOutputMemoryFileTftpCreated": sleAutoCliOutputMemoryFileTftpCreated,
       "sleAutoCliOutputMemoryFileDestroyed": sleAutoCliOutputMemoryFileDestroyed,
       "sleAutoReset": sleAutoReset,
       "sleAutoResetPing": sleAutoResetPing,
       "sleAutoResetPingInfo": sleAutoResetPingInfo,
       "sleAutoResetPingConfStatus": sleAutoResetPingConfStatus,
       "sleAutoResetPingIpAddress": sleAutoResetPingIpAddress,
       "sleAutoResetPingTransactionInterval": sleAutoResetPingTransactionInterval,
       "sleAutoResetPingNumberOfRequest": sleAutoResetPingNumberOfRequest,
       "sleAutoResetPingRequestInterval": sleAutoResetPingRequestInterval,
       "sleAutoResetPingTimeoutOfRequest": sleAutoResetPingTimeoutOfRequest,
       "sleAutoResetPingLossThreshold": sleAutoResetPingLossThreshold,
       "sleAutoResetPingEnableTime": sleAutoResetPingEnableTime,
       "sleAutoResetPingRequestCount": sleAutoResetPingRequestCount,
       "sleAutoResetPingReplyCount": sleAutoResetPingReplyCount,
       "sleAutoResetPingLossCount": sleAutoResetPingLossCount,
       "sleAutoResetPingTotalPingTransaction": sleAutoResetPingTotalPingTransaction,
       "sleAutoResetPingTotalLossTransaction": sleAutoResetPingTotalLossTransaction,
       "sleAutoResetPingRebootThreshold": sleAutoResetPingRebootThreshold,
       "sleAutoResetPingRebootCounter": sleAutoResetPingRebootCounter,
       "sleAutoResetPingRebootRecoveryTime": sleAutoResetPingRebootRecoveryTime,
       "sleAutoResetPingControl": sleAutoResetPingControl,
       "sleAutoResetPingControlRequest": sleAutoResetPingControlRequest,
       "sleAutoResetPingControlStatus": sleAutoResetPingControlStatus,
       "sleAutoResetPingControlTimer": sleAutoResetPingControlTimer,
       "sleAutoResetPingControlTimeStamp": sleAutoResetPingControlTimeStamp,
       "sleAutoResetPingControlReqResult": sleAutoResetPingControlReqResult,
       "sleAutoResetPingControlConfStatus": sleAutoResetPingControlConfStatus,
       "sleAutoResetPingControlIpAddress": sleAutoResetPingControlIpAddress,
       "sleAutoResetPingControlTransactionInterval": sleAutoResetPingControlTransactionInterval,
       "sleAutoResetPingControlNumberOfRequest": sleAutoResetPingControlNumberOfRequest,
       "sleAutoResetPingControlRequestInterval": sleAutoResetPingControlRequestInterval,
       "sleAutoResetPingControlTimeoutOfRequest": sleAutoResetPingControlTimeoutOfRequest,
       "sleAutoResetPingControlPingLossThreshold": sleAutoResetPingControlPingLossThreshold,
       "sleAutoResetPingControlRebootThreshold": sleAutoResetPingControlRebootThreshold,
       "sleAutoResetPingControlRebootRecoveryTime": sleAutoResetPingControlRebootRecoveryTime,
       "sleAutoResetPingNotification": sleAutoResetPingNotification,
       "sleAutoResetPingStatusChanged": sleAutoResetPingStatusChanged,
       "sleAutoResetPingInfoModified": sleAutoResetPingInfoModified,
       "sleAutoResetPingRebootCtrlModified": sleAutoResetPingRebootCtrlModified,
       "sleAutoResetPingRebootCountClearSetted": sleAutoResetPingRebootCountClearSetted,
       "sleAutoResetMemoryleak": sleAutoResetMemoryleak,
       "sleAutoResetMemoryleakInfo": sleAutoResetMemoryleakInfo,
       "sleAutoResetMemoryleakContStatus": sleAutoResetMemoryleakContStatus,
       "sleAutoResetMemoryleakMemThreshold": sleAutoResetMemoryleakMemThreshold,
       "sleAutoResetMemoryleakCheckInterval": sleAutoResetMemoryleakCheckInterval,
       "sleAutoResetMemoryleakNumberOfVerification": sleAutoResetMemoryleakNumberOfVerification,
       "sleAutoResetMemoryleakVerificationInterval": sleAutoResetMemoryleakVerificationInterval,
       "sleAutoResetMemoryleakCountThreshold": sleAutoResetMemoryleakCountThreshold,
       "sleAutoResetMemoryleakEnableTime": sleAutoResetMemoryleakEnableTime,
       "sleAutoResetMemoryleakLastFreeMemory": sleAutoResetMemoryleakLastFreeMemory,
       "sleAutoResetMemoryleakVerificationCount": sleAutoResetMemoryleakVerificationCount,
       "sleAutoResetMemoryleakDetectionCount": sleAutoResetMemoryleakDetectionCount,
       "sleAutoResetMemoryleakTotalVerificationCount": sleAutoResetMemoryleakTotalVerificationCount,
       "sleAutoResetMemoryleakTotalDetectionCount": sleAutoResetMemoryleakTotalDetectionCount,
       "sleAutoResetMemoryleakReboottimeStartHour": sleAutoResetMemoryleakReboottimeStartHour,
       "sleAutoResetMemoryleakReboottimeStartMin": sleAutoResetMemoryleakReboottimeStartMin,
       "sleAutoResetMemoryleakReboottimeEndHour": sleAutoResetMemoryleakReboottimeEndHour,
       "sleAutoResetMemoryleakReboottimeEndMin": sleAutoResetMemoryleakReboottimeEndMin,
       "sleAutoResetMemoryleakRebootThreshold": sleAutoResetMemoryleakRebootThreshold,
       "sleAutoResetMemoryleakRebootCount": sleAutoResetMemoryleakRebootCount,
       "sleAutoResetMemoryleakControl": sleAutoResetMemoryleakControl,
       "sleAutoResetMemoryleakControlRequest": sleAutoResetMemoryleakControlRequest,
       "sleAutoResetMemoryleakControlStatus": sleAutoResetMemoryleakControlStatus,
       "sleAutoResetMemoryleakControlTimer": sleAutoResetMemoryleakControlTimer,
       "sleAutoResetMemoryleakControlTimeStamp": sleAutoResetMemoryleakControlTimeStamp,
       "sleAutoResetMemoryleakControlReqResult": sleAutoResetMemoryleakControlReqResult,
       "sleAutoResetMemoryleakControlConfStatus": sleAutoResetMemoryleakControlConfStatus,
       "sleAutoResetMemoryleakControlMemThreshold": sleAutoResetMemoryleakControlMemThreshold,
       "sleAutoResetMemoryleakControlCheckInterval": sleAutoResetMemoryleakControlCheckInterval,
       "sleAutoResetMemoryleakControlNumberOfVerification": sleAutoResetMemoryleakControlNumberOfVerification,
       "sleAutoResetMemoryleakControlVerificationInterval": sleAutoResetMemoryleakControlVerificationInterval,
       "sleAutoResetMemoryleakControlCountThreshold": sleAutoResetMemoryleakControlCountThreshold,
       "sleAutoResetMemoryleakControlReboottimeStartHour": sleAutoResetMemoryleakControlReboottimeStartHour,
       "sleAutoResetMemoryleakControlReboottimeStartMin": sleAutoResetMemoryleakControlReboottimeStartMin,
       "sleAutoResetMemoryleakControlReboottimeEndHour": sleAutoResetMemoryleakControlReboottimeEndHour,
       "sleAutoResetMemoryleakControlReboottimeEndMin": sleAutoResetMemoryleakControlReboottimeEndMin,
       "sleAutoResetMemoryleakControlRebootThreshold": sleAutoResetMemoryleakControlRebootThreshold,
       "sleAutoResetMemoryleakNotification": sleAutoResetMemoryleakNotification,
       "sleAutoResetMemoryleakStatusChanged": sleAutoResetMemoryleakStatusChanged,
       "sleAutoResetMemoryleakInfoModified": sleAutoResetMemoryleakInfoModified,
       "sleAutoResetMemoryleakReboottimeModified": sleAutoResetMemoryleakReboottimeModified,
       "sleAutoResetMemoryleakRebootCtrlModified": sleAutoResetMemoryleakRebootCtrlModified,
       "sleAutoResetMemoryleakRebootCountClearSetted": sleAutoResetMemoryleakRebootCountClearSetted,
       "sleAutoResetCpu": sleAutoResetCpu,
       "sleAutoResetCpuInfo": sleAutoResetCpuInfo,
       "sleAutoResetCpuStatus": sleAutoResetCpuStatus,
       "sleAutoResetCpuLoad": sleAutoResetCpuLoad,
       "sleAutoResetCpuInterruptLoad": sleAutoResetCpuInterruptLoad,
       "sleAutoResetCpuTime": sleAutoResetCpuTime,
       "sleAutoResetCpuControl": sleAutoResetCpuControl,
       "sleAutoResetCpuControlRequest": sleAutoResetCpuControlRequest,
       "sleAutoResetCpuControlStatus": sleAutoResetCpuControlStatus,
       "sleAutoResetCpuControlTimer": sleAutoResetCpuControlTimer,
       "sleAutoResetCpuControlTimeStamp": sleAutoResetCpuControlTimeStamp,
       "sleAutoResetCpuControlReqResult": sleAutoResetCpuControlReqResult,
       "sleAutoResetCpuControlLoad": sleAutoResetCpuControlLoad,
       "sleAutoResetCpuControlInterruptLoad": sleAutoResetCpuControlInterruptLoad,
       "sleAutoResetCpuControlTime": sleAutoResetCpuControlTime,
       "sleAutoResetCpuNotification": sleAutoResetCpuNotification,
       "sleAutoResetCpuChanged": sleAutoResetCpuChanged,
       "sleAutoResetCpuDeleted": sleAutoResetCpuDeleted,
       "sleAutoResetInfo": sleAutoResetInfo,
       "sleAutoResetBootReason": sleAutoResetBootReason,
       "sleCoreDump": sleCoreDump,
       "sleCoreDumpInfoTable": sleCoreDumpInfoTable,
       "sleCoreDumpInfoEntry": sleCoreDumpInfoEntry,
       "sleCoreDumpInfoPID": sleCoreDumpInfoPID,
       "sleCoreDumpInfoStatus": sleCoreDumpInfoStatus,
       "sleCoreDumpFile": sleCoreDumpFile,
       "sleCoreDumpControl": sleCoreDumpControl,
       "sleCoreDumpControlRequest": sleCoreDumpControlRequest,
       "sleCoreDumpControlStatus": sleCoreDumpControlStatus,
       "sleCoreDumpControlTimer": sleCoreDumpControlTimer,
       "sleCoreDumpControlTimeStamp": sleCoreDumpControlTimeStamp,
       "sleCoreDumpControlReqResult": sleCoreDumpControlReqResult,
       "sleCoreDumpControlPID": sleCoreDumpControlPID,
       "sleCoreDumpControlServerIP": sleCoreDumpControlServerIP,
       "sleCoreDumpControlUserID": sleCoreDumpControlUserID,
       "sleCoreDumpControlPassword": sleCoreDumpControlPassword,
       "sleCoreDumpControlCoredumpFile": sleCoreDumpControlCoredumpFile,
       "sleCoreDumpNotification": sleCoreDumpNotification,
       "sleCoreDumpEntryCreated": sleCoreDumpEntryCreated,
       "sleCoreDumpEntryDestroyed": sleCoreDumpEntryDestroyed,
       "sleCoreDumpEntryChanged": sleCoreDumpEntryChanged,
       "sleService": sleService,
       "sleServiceTable": sleServiceTable,
       "sleServiceEntry": sleServiceEntry,
       "sleServiceIndex": sleServiceIndex,
       "sleServiceProtocol": sleServiceProtocol,
       "sleServiceName": sleServiceName,
       "sleServicePort": sleServicePort,
       "sleServiceAdminStatus": sleServiceAdminStatus,
       "sleServiceControl": sleServiceControl,
       "sleServiceControlRequest": sleServiceControlRequest,
       "sleServiceControlStatus": sleServiceControlStatus,
       "sleServiceControlTimer": sleServiceControlTimer,
       "sleServiceControlTimeStamp": sleServiceControlTimeStamp,
       "sleServiceControlReqResult": sleServiceControlReqResult,
       "sleServiceControlIndex": sleServiceControlIndex,
       "sleServiceControlProtocol": sleServiceControlProtocol,
       "sleServiceControlPort": sleServiceControlPort,
       "sleServiceControlAdminStatus": sleServiceControlAdminStatus,
       "sleServiceNotification": sleServiceNotification,
       "sleServicePortChanged": sleServicePortChanged,
       "sleServiceAdminStatusChanged": sleServiceAdminStatusChanged,
       "sleSystemUser": sleSystemUser,
       "sleSystemUserTable": sleSystemUserTable,
       "sleSystemUserEntry": sleSystemUserEntry,
       "sleSystemUserName": sleSystemUserName,
       "sleSystemUserLevel": sleSystemUserLevel,
       "sleSystemUserPassword": sleSystemUserPassword,
       "sleSystemUserDesc": sleSystemUserDesc,
       "sleSystemUserLoginFailureCount": sleSystemUserLoginFailureCount,
       "sleSystemUserLoginLastFailureTime": sleSystemUserLoginLastFailureTime,
       "sleSystemUserControl": sleSystemUserControl,
       "sleSystemUserControlRequest": sleSystemUserControlRequest,
       "sleSystemUserControlStatus": sleSystemUserControlStatus,
       "sleSystemUserControlTimer": sleSystemUserControlTimer,
       "sleSystemUserControlTimeStamp": sleSystemUserControlTimeStamp,
       "sleSystemUserControlReqResult": sleSystemUserControlReqResult,
       "sleSystemUserControlName": sleSystemUserControlName,
       "sleSystemUserControlRename": sleSystemUserControlRename,
       "sleSystemUserControlLevel": sleSystemUserControlLevel,
       "sleSystemUserControlPwType": sleSystemUserControlPwType,
       "sleSystemUserControlPassword": sleSystemUserControlPassword,
       "sleSystemUserControlDesc": sleSystemUserControlDesc,
       "sleSystemUserNotification": sleSystemUserNotification,
       "sleSystemUserCreated": sleSystemUserCreated,
       "sleSystemUserNameChanged": sleSystemUserNameChanged,
       "sleSystemUserPasswordChanged": sleSystemUserPasswordChanged,
       "sleSystemUserDestroyed": sleSystemUserDestroyed,
       "sleSystemUserLevelChanged": sleSystemUserLevelChanged,
       "sleSystemUserLoginAttemptsFailureLogCleared": sleSystemUserLoginAttemptsFailureLogCleared,
       "sleParameter": sleParameter,
       "sleParameterTable": sleParameterTable,
       "sleParameterEntry": sleParameterEntry,
       "sleParameterName": sleParameterName,
       "sleParameterValue": sleParameterValue,
       "sleParameterMode": sleParameterMode,
       "sleParameterControl": sleParameterControl,
       "sleParameterControlRequest": sleParameterControlRequest,
       "sleParameterControlStatus": sleParameterControlStatus,
       "sleParameterControlTimer": sleParameterControlTimer,
       "sleParameterControlTimeStamp": sleParameterControlTimeStamp,
       "sleParameterControlReqResult": sleParameterControlReqResult,
       "sleParameterControlName": sleParameterControlName,
       "sleParameterControlValue": sleParameterControlValue,
       "sleParameterControlMode": sleParameterControlMode,
       "sleParameterNotification": sleParameterNotification,
       "sleParameterCreated": sleParameterCreated,
       "sleParameterDestroyed": sleParameterDestroyed,
       "sleParameterModeChanged": sleParameterModeChanged,
       "sleParameterValueChanged": sleParameterValueChanged,
       "sleSwWatchdogBase": sleSwWatchdogBase,
       "sleSwWatchdogTable": sleSwWatchdogTable,
       "sleSwWatchdogEntry": sleSwWatchdogEntry,
       "sleSwWatchdogType": sleSwWatchdogType,
       "sleSwWatchdogInterval": sleSwWatchdogInterval,
       "sleSwWatchdogThreshold": sleSwWatchdogThreshold,
       "sleSwWatchdogAction": sleSwWatchdogAction,
       "sleSwWatchdogErrcnt": sleSwWatchdogErrcnt,
       "sleSwWatchdogControl": sleSwWatchdogControl,
       "sleSwWatchdogControlRequest": sleSwWatchdogControlRequest,
       "sleSwWatchdogControlStatus": sleSwWatchdogControlStatus,
       "sleSwWatchdogControlTimer": sleSwWatchdogControlTimer,
       "sleSwWatchdogControlTimeStamp": sleSwWatchdogControlTimeStamp,
       "sleSwWatchdogControlReqResult": sleSwWatchdogControlReqResult,
       "sleSwWatchdogControlType": sleSwWatchdogControlType,
       "sleSwWatchdogControlInterval": sleSwWatchdogControlInterval,
       "sleSwWatchdogControlThreshold": sleSwWatchdogControlThreshold,
       "sleSwWatchdogControlAction": sleSwWatchdogControlAction,
       "sleSwWatchdogNotification": sleSwWatchdogNotification,
       "sleSwWatchdogCreated": sleSwWatchdogCreated,
       "sleSwWatchdogDeleted": sleSwWatchdogDeleted,
       "sleAutoUpgrade": sleAutoUpgrade,
       "sleAutoUpgradeProfile": sleAutoUpgradeProfile,
       "sleAutoUpgradeProfileTable": sleAutoUpgradeProfileTable,
       "sleAutoUpgradeProfileEntry": sleAutoUpgradeProfileEntry,
       "sleAutoUpgradeProfileIndex": sleAutoUpgradeProfileIndex,
       "sleAutoUpgradeProfileName": sleAutoUpgradeProfileName,
       "sleAutoUpgradeProfileOldVer": sleAutoUpgradeProfileOldVer,
       "sleAutoUpgradeProfileNewVer": sleAutoUpgradeProfileNewVer,
       "sleAutoUpgradeProfileSize": sleAutoUpgradeProfileSize,
       "sleAutoUpgradeProfilePeriodType": sleAutoUpgradeProfilePeriodType,
       "sleAutoUpgradeProfileDate": sleAutoUpgradeProfileDate,
       "sleAutoUpgradeProfilePeriodDate": sleAutoUpgradeProfilePeriodDate,
       "sleAutoUpgradeProfileTimeout": sleAutoUpgradeProfileTimeout,
       "sleAutoUpgradeProfileRetry": sleAutoUpgradeProfileRetry,
       "sleAutoUpgradeProfileRegSec": sleAutoUpgradeProfileRegSec,
       "sleAutoUpgradeProfileReloadTime": sleAutoUpgradeProfileReloadTime,
       "sleAutoUpgradeProfileModel": sleAutoUpgradeProfileModel,
       "sleAutoUpgradeProfileControl": sleAutoUpgradeProfileControl,
       "sleAutoUpgradeProfileControlRequest": sleAutoUpgradeProfileControlRequest,
       "sleAutoUpgradeProfileControlStatus": sleAutoUpgradeProfileControlStatus,
       "sleAutoUpgradeProfileControlTimer": sleAutoUpgradeProfileControlTimer,
       "sleAutoUpgradeProfileControlTimeStamp": sleAutoUpgradeProfileControlTimeStamp,
       "sleAutoUpgradeProfileControlReqResult": sleAutoUpgradeProfileControlReqResult,
       "sleAutoUpgradeProfileControlName": sleAutoUpgradeProfileControlName,
       "sleAutoUpgradeProfileControlOldVer": sleAutoUpgradeProfileControlOldVer,
       "sleAutoUpgradeProfileControlNewVer": sleAutoUpgradeProfileControlNewVer,
       "sleAutoUpgradeProfileControlSize": sleAutoUpgradeProfileControlSize,
       "sleAutoUpgradeProfileControlPeriodType": sleAutoUpgradeProfileControlPeriodType,
       "sleAutoUpgradeProfileControlDate": sleAutoUpgradeProfileControlDate,
       "sleAutoUpgradeProfileControlPeriodDate": sleAutoUpgradeProfileControlPeriodDate,
       "sleAutoUpgradeProfileControlTimeout": sleAutoUpgradeProfileControlTimeout,
       "sleAutoUpgradeProfileControlRetry": sleAutoUpgradeProfileControlRetry,
       "sleAutoUpgradeProfileControlRegSec": sleAutoUpgradeProfileControlRegSec,
       "sleAutoUpgradeProfileControlReloadTime": sleAutoUpgradeProfileControlReloadTime,
       "sleAutoUpgradeProfileControlModel": sleAutoUpgradeProfileControlModel,
       "sleAutoUpgradeProfileNotification": sleAutoUpgradeProfileNotification,
       "sleAutoUpgradeProfileCreated": sleAutoUpgradeProfileCreated,
       "sleAutoUpgradeProfileDeleted": sleAutoUpgradeProfileDeleted,
       "sleAutoUpgradeProfileChanged": sleAutoUpgradeProfileChanged,
       "sleAutoUpgradeMgmt": sleAutoUpgradeMgmt,
       "sleAutoUpgradeOltTable": sleAutoUpgradeOltTable,
       "sleAutoUpgradeOltEntry": sleAutoUpgradeOltEntry,
       "sleAutoUpgradeOltSlotIndex": sleAutoUpgradeOltSlotIndex,
       "sleAutoUpgradeOltFwType": sleAutoUpgradeOltFwType,
       "sleAutoUpgradeOltProfileName": sleAutoUpgradeOltProfileName,
       "sleAutoUpgradeOltSlotType": sleAutoUpgradeOltSlotType,
       "sleAutoUpgradeOntTable": sleAutoUpgradeOntTable,
       "sleAutoUpgradeOntEntry": sleAutoUpgradeOntEntry,
       "sleAutoUpgradeOntOltIndex": sleAutoUpgradeOntOltIndex,
       "sleAutoUpgradeOntIndex": sleAutoUpgradeOntIndex,
       "sleAutoUpgradeOntFwType": sleAutoUpgradeOntFwType,
       "sleAutoUpgradeOntProfileName": sleAutoUpgradeOntProfileName,
       "sleAutoUpgradeMgmtControl": sleAutoUpgradeMgmtControl,
       "sleAutoUpgradeMgmtControlRequest": sleAutoUpgradeMgmtControlRequest,
       "sleAutoUpgradeMgmtControlStatus": sleAutoUpgradeMgmtControlStatus,
       "sleAutoUpgradeMgmtControlTimer": sleAutoUpgradeMgmtControlTimer,
       "sleAutoUpgradeMgmtControlTimeStamp": sleAutoUpgradeMgmtControlTimeStamp,
       "sleAutoUpgradeMgmtControlReqResult": sleAutoUpgradeMgmtControlReqResult,
       "sleAutoUpgradeMgmtControlOltIndex": sleAutoUpgradeMgmtControlOltIndex,
       "sleAutoUpgradeMgmtControlOntIndex": sleAutoUpgradeMgmtControlOntIndex,
       "sleAutoUpgradeMgmtControlFwType": sleAutoUpgradeMgmtControlFwType,
       "sleAutoUpgradeMgmtControlProfileName": sleAutoUpgradeMgmtControlProfileName,
       "sleAutoUpgradeMgmtControlSlotType": sleAutoUpgradeMgmtControlSlotType,
       "sleAutoUpgradeMgmtNotification": sleAutoUpgradeMgmtNotification,
       "sleAutoUpgradeSetOltProfile": sleAutoUpgradeSetOltProfile,
       "sleAutoUpgradeUnSetOltProfile": sleAutoUpgradeUnSetOltProfile,
       "sleAutoUpgradeSetOntProfile": sleAutoUpgradeSetOntProfile,
       "sleAutoUpgradeUnSetOntProfile": sleAutoUpgradeUnSetOntProfile,
       "sleAutoUpgradeLog": sleAutoUpgradeLog,
       "sleAutoUpgradeLogInfo": sleAutoUpgradeLogInfo,
       "sleAutoUpgradeLogControl": sleAutoUpgradeLogControl,
       "sleAutoUpgradeLogControlRequest": sleAutoUpgradeLogControlRequest,
       "sleAutoUpgradeLogControlStatus": sleAutoUpgradeLogControlStatus,
       "sleAutoUpgradeLogControlTimer": sleAutoUpgradeLogControlTimer,
       "sleAutoUpgradeLogControlTimeStamp": sleAutoUpgradeLogControlTimeStamp,
       "sleAutoUpgradeLogControlReqResult": sleAutoUpgradeLogControlReqResult,
       "sleAutoUpgradeLogControlSlotIndex": sleAutoUpgradeLogControlSlotIndex,
       "sleAutoUpgradeLogControlOntIndex": sleAutoUpgradeLogControlOntIndex,
       "sleAutoUpgradeLogControlExportMethod": sleAutoUpgradeLogControlExportMethod,
       "sleAutoUpgradeLogControlServer": sleAutoUpgradeLogControlServer,
       "sleAutoUpgradeLogControlUser": sleAutoUpgradeLogControlUser,
       "sleAutoUpgradeLogControlPasswd": sleAutoUpgradeLogControlPasswd,
       "sleAutoUpgradeLogNotification": sleAutoUpgradeLogNotification,
       "sleAutoUpgradeDeleteOltLog": sleAutoUpgradeDeleteOltLog,
       "sleAutoUpgradeDeleteAllOltLog": sleAutoUpgradeDeleteAllOltLog,
       "sleAutoUpgradeDeleteOntLog": sleAutoUpgradeDeleteOntLog,
       "sleAutoUpgradeDeleteAllOntLog": sleAutoUpgradeDeleteAllOntLog,
       "sleAutoUpgradeExportOltLog": sleAutoUpgradeExportOltLog,
       "sleAutoUpgradeExportOntLog": sleAutoUpgradeExportOntLog,
       "sleWatchdog": sleWatchdog,
       "sleWatchdogInfo": sleWatchdogInfo,
       "sleWatchdogAdminStatus": sleWatchdogAdminStatus,
       "sleWatchdogTimeout": sleWatchdogTimeout,
       "sleWatchdogMode": sleWatchdogMode,
       "sleWatchdogControl": sleWatchdogControl,
       "sleWatchdogControlRequest": sleWatchdogControlRequest,
       "sleWatchdogControlStatus": sleWatchdogControlStatus,
       "sleWatchdogControlTimer": sleWatchdogControlTimer,
       "sleWatchdogControlTimeStamp": sleWatchdogControlTimeStamp,
       "sleWatchdogControlReqResult": sleWatchdogControlReqResult,
       "sleWatchdogControlAdminStatus": sleWatchdogControlAdminStatus,
       "sleWatchdogControlTimeout": sleWatchdogControlTimeout,
       "sleWatchdogControlMode": sleWatchdogControlMode,
       "sleWatchdogNotification": sleWatchdogNotification,
       "sleWatchdogAdminStatusChanged": sleWatchdogAdminStatusChanged,
       "sleWatchdogTimeoutChanged": sleWatchdogTimeoutChanged,
       "sleWatchdogModeChanged": sleWatchdogModeChanged,
       "sleFtpclient": sleFtpclient,
       "sleFtpclientTable": sleFtpclientTable,
       "sleFtpclientEntry": sleFtpclientEntry,
       "sleFtpclientIndex": sleFtpclientIndex,
       "sleFtpclientFileName": sleFtpclientFileName,
       "sleFtpclientFileSize": sleFtpclientFileSize,
       "sleFtpclientControl": sleFtpclientControl,
       "sleFtpclientControlRequest": sleFtpclientControlRequest,
       "sleFtpclientControlStatus": sleFtpclientControlStatus,
       "sleFtpclientControlTimer": sleFtpclientControlTimer,
       "sleFtpclientControlTimeStamp": sleFtpclientControlTimeStamp,
       "sleFtpclientControlReqResult": sleFtpclientControlReqResult,
       "sleFtpclientControlServerIp": sleFtpclientControlServerIp,
       "sleFtpclientControlUserId": sleFtpclientControlUserId,
       "sleFtpclientControlPassword": sleFtpclientControlPassword,
       "sleFtpclientControlDirectoryPath": sleFtpclientControlDirectoryPath,
       "sleFtpclientNotification": sleFtpclientNotification,
       "sleFtpclientDirectoryInfoUpdated": sleFtpclientDirectoryInfoUpdated,
       "sleSystemMaintenanceGroup": sleSystemMaintenanceGroup,
       "sleSystemMaintenanceNotificationGroup": sleSystemMaintenanceNotificationGroup}
)
