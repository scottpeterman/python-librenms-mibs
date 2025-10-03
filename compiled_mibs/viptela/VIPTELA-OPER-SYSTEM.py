# SNMP MIB module (VIPTELA-OPER-SYSTEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-OPER-SYSTEM
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:06 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_oper_system = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11)
)
if mibBuilder.loadTexts:
    viptela_oper_system.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Permission1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Permission(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_SystemStatus_ObjectIdentity = ObjectIdentity
systemStatus = _SystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1)
)
_SystemStatusPersonality_Type = String
_SystemStatusPersonality_Object = MibScalar
systemStatusPersonality = _SystemStatusPersonality_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 1),
    _SystemStatusPersonality_Type()
)
systemStatusPersonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusPersonality.setStatus("current")
_SystemStatusVersion_Type = String
_SystemStatusVersion_Object = MibScalar
systemStatusVersion = _SystemStatusVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 2),
    _SystemStatusVersion_Type()
)
systemStatusVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVersion.setStatus("current")
_SystemStatusLoghostStatus_Type = String
_SystemStatusLoghostStatus_Object = MibScalar
systemStatusLoghostStatus = _SystemStatusLoghostStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 3),
    _SystemStatusLoghostStatus_Type()
)
systemStatusLoghostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusLoghostStatus.setStatus("current")
_SystemStatusLoghostName_Type = String
_SystemStatusLoghostName_Object = MibScalar
systemStatusLoghostName = _SystemStatusLoghostName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 4),
    _SystemStatusLoghostName_Type()
)
systemStatusLoghostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusLoghostName.setStatus("current")
_SystemStatusDiskStatus_Type = String
_SystemStatusDiskStatus_Object = MibScalar
systemStatusDiskStatus = _SystemStatusDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 5),
    _SystemStatusDiskStatus_Type()
)
systemStatusDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskStatus.setStatus("current")
_SystemStatusRebootReason_Type = String
_SystemStatusRebootReason_Object = MibScalar
systemStatusRebootReason = _SystemStatusRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 6),
    _SystemStatusRebootReason_Type()
)
systemStatusRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusRebootReason.setStatus("current")
_SystemStatusCoreFilesStatus_Type = String
_SystemStatusCoreFilesStatus_Object = MibScalar
systemStatusCoreFilesStatus = _SystemStatusCoreFilesStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 7),
    _SystemStatusCoreFilesStatus_Type()
)
systemStatusCoreFilesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusCoreFilesStatus.setStatus("current")
_SystemStatusUptime_Type = String
_SystemStatusUptime_Object = MibScalar
systemStatusUptime = _SystemStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 8),
    _SystemStatusUptime_Type()
)
systemStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusUptime.setStatus("current")
_SystemStatusMin1Avg_Type = String
_SystemStatusMin1Avg_Object = MibScalar
systemStatusMin1Avg = _SystemStatusMin1Avg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 9),
    _SystemStatusMin1Avg_Type()
)
systemStatusMin1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMin1Avg.setStatus("current")
_SystemStatusMin5Avg_Type = String
_SystemStatusMin5Avg_Object = MibScalar
systemStatusMin5Avg = _SystemStatusMin5Avg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 10),
    _SystemStatusMin5Avg_Type()
)
systemStatusMin5Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMin5Avg.setStatus("current")
_SystemStatusMin15Avg_Type = String
_SystemStatusMin15Avg_Object = MibScalar
systemStatusMin15Avg = _SystemStatusMin15Avg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 11),
    _SystemStatusMin15Avg_Type()
)
systemStatusMin15Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMin15Avg.setStatus("current")
_SystemStatusTotalp_Type = Unsigned32
_SystemStatusTotalp_Object = MibScalar
systemStatusTotalp = _SystemStatusTotalp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 12),
    _SystemStatusTotalp_Type()
)
systemStatusTotalp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusTotalp.setStatus("current")
_SystemStatusRunningp_Type = Unsigned32
_SystemStatusRunningp_Object = MibScalar
systemStatusRunningp = _SystemStatusRunningp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 13),
    _SystemStatusRunningp_Type()
)
systemStatusRunningp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusRunningp.setStatus("current")
_SystemStatusCpuUser_Type = String
_SystemStatusCpuUser_Object = MibScalar
systemStatusCpuUser = _SystemStatusCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 14),
    _SystemStatusCpuUser_Type()
)
systemStatusCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusCpuUser.setStatus("current")
_SystemStatusCpuSystem_Type = String
_SystemStatusCpuSystem_Object = MibScalar
systemStatusCpuSystem = _SystemStatusCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 15),
    _SystemStatusCpuSystem_Type()
)
systemStatusCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusCpuSystem.setStatus("current")
_SystemStatusCpuIdle_Type = String
_SystemStatusCpuIdle_Object = MibScalar
systemStatusCpuIdle = _SystemStatusCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 16),
    _SystemStatusCpuIdle_Type()
)
systemStatusCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusCpuIdle.setStatus("current")
_SystemStatusMemTotal_Type = ConfdString
_SystemStatusMemTotal_Object = MibScalar
systemStatusMemTotal = _SystemStatusMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 17),
    _SystemStatusMemTotal_Type()
)
systemStatusMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemTotal.setStatus("current")
_SystemStatusMemUsed_Type = ConfdString
_SystemStatusMemUsed_Object = MibScalar
systemStatusMemUsed = _SystemStatusMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 18),
    _SystemStatusMemUsed_Type()
)
systemStatusMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemUsed.setStatus("current")
_SystemStatusMemFree_Type = ConfdString
_SystemStatusMemFree_Object = MibScalar
systemStatusMemFree = _SystemStatusMemFree_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 19),
    _SystemStatusMemFree_Type()
)
systemStatusMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemFree.setStatus("current")
_SystemStatusMemBuffers_Type = ConfdString
_SystemStatusMemBuffers_Object = MibScalar
systemStatusMemBuffers = _SystemStatusMemBuffers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 20),
    _SystemStatusMemBuffers_Type()
)
systemStatusMemBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemBuffers.setStatus("current")
_SystemStatusMemCached_Type = ConfdString
_SystemStatusMemCached_Object = MibScalar
systemStatusMemCached = _SystemStatusMemCached_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 21),
    _SystemStatusMemCached_Type()
)
systemStatusMemCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemCached.setStatus("current")
_SystemStatusDiskFs_Type = String
_SystemStatusDiskFs_Object = MibScalar
systemStatusDiskFs = _SystemStatusDiskFs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 22),
    _SystemStatusDiskFs_Type()
)
systemStatusDiskFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskFs.setStatus("current")
_SystemStatusDiskSize_Type = String
_SystemStatusDiskSize_Object = MibScalar
systemStatusDiskSize = _SystemStatusDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 23),
    _SystemStatusDiskSize_Type()
)
systemStatusDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskSize.setStatus("current")
_SystemStatusDiskUsed_Type = String
_SystemStatusDiskUsed_Object = MibScalar
systemStatusDiskUsed = _SystemStatusDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 24),
    _SystemStatusDiskUsed_Type()
)
systemStatusDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskUsed.setStatus("current")
_SystemStatusDiskAvail_Type = String
_SystemStatusDiskAvail_Object = MibScalar
systemStatusDiskAvail = _SystemStatusDiskAvail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 25),
    _SystemStatusDiskAvail_Type()
)
systemStatusDiskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskAvail.setStatus("current")
_SystemStatusDiskUse_Type = ConfdString
_SystemStatusDiskUse_Object = MibScalar
systemStatusDiskUse = _SystemStatusDiskUse_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 26),
    _SystemStatusDiskUse_Type()
)
systemStatusDiskUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskUse.setStatus("current")
_SystemStatusDiskTotalBytes_Type = ConfdString
_SystemStatusDiskTotalBytes_Object = MibScalar
systemStatusDiskTotalBytes = _SystemStatusDiskTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 27),
    _SystemStatusDiskTotalBytes_Type()
)
systemStatusDiskTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskTotalBytes.setStatus("current")
_SystemStatusDiskUsedBytes_Type = ConfdString
_SystemStatusDiskUsedBytes_Object = MibScalar
systemStatusDiskUsedBytes = _SystemStatusDiskUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 28),
    _SystemStatusDiskUsedBytes_Type()
)
systemStatusDiskUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskUsedBytes.setStatus("current")
_SystemStatusDiskAvailBytes_Type = ConfdString
_SystemStatusDiskAvailBytes_Object = MibScalar
systemStatusDiskAvailBytes = _SystemStatusDiskAvailBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 29),
    _SystemStatusDiskAvailBytes_Type()
)
systemStatusDiskAvailBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskAvailBytes.setStatus("current")
_SystemStatusDiskMount_Type = String
_SystemStatusDiskMount_Object = MibScalar
systemStatusDiskMount = _SystemStatusDiskMount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 30),
    _SystemStatusDiskMount_Type()
)
systemStatusDiskMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskMount.setStatus("current")
_SystemStatusServices_Type = String
_SystemStatusServices_Object = MibScalar
systemStatusServices = _SystemStatusServices_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 31),
    _SystemStatusServices_Type()
)
systemStatusServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusServices.setStatus("current")


class _SystemStatusBoardType_Type(Integer32):
    """Custom type systemStatusBoardType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("vedge-1000", 0),
          ("vedge-2000", 1),
          ("sim", 2),
          ("none", 3),
          ("unknown", 4),
          ("vedge-100", 5),
          ("vedge-100-B", 6),
          ("vedge-5000", 7),
          ("vedge-CSR", 8),
          ("vedge-ISR", 9),
          ("vedge-ASR", 10),
          ("vedge-101-B", 11),
          ("vedge-1001", 12),
          ("vedge-101-m", 13),
          ("vedge-ISR1100-4G", 14),
          ("vedge-ISR1100-4GLTE", 15),
          ("vedge-ISR1100-6G", 16),
          ("vedge-encs", 17),
          ("vedge-ISR1100X-4G", 18),
          ("vedge-ISR1100X-6G", 19))
    )


_SystemStatusBoardType_Type.__name__ = "Integer32"
_SystemStatusBoardType_Object = MibScalar
systemStatusBoardType = _SystemStatusBoardType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 32),
    _SystemStatusBoardType_Type()
)
systemStatusBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusBoardType.setStatus("current")
_SystemStatusConfigDateDateTimeString_Type = String
_SystemStatusConfigDateDateTimeString_Object = MibScalar
systemStatusConfigDateDateTimeString = _SystemStatusConfigDateDateTimeString_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 33),
    _SystemStatusConfigDateDateTimeString_Type()
)
systemStatusConfigDateDateTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusConfigDateDateTimeString.setStatus("current")
_SystemStatusCurrentDateDateTimeString_Type = String
_SystemStatusCurrentDateDateTimeString_Object = MibScalar
systemStatusCurrentDateDateTimeString = _SystemStatusCurrentDateDateTimeString_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 34),
    _SystemStatusCurrentDateDateTimeString_Type()
)
systemStatusCurrentDateDateTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusCurrentDateDateTimeString.setStatus("current")
_SystemStatusStandaloneVbond_Type = TruthValue
_SystemStatusStandaloneVbond_Object = MibScalar
systemStatusStandaloneVbond = _SystemStatusStandaloneVbond_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 35),
    _SystemStatusStandaloneVbond_Type()
)
systemStatusStandaloneVbond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusStandaloneVbond.setStatus("current")
_SystemStatusVmanaged_Type = TruthValue
_SystemStatusVmanaged_Object = MibScalar
systemStatusVmanaged = _SystemStatusVmanaged_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 36),
    _SystemStatusVmanaged_Type()
)
systemStatusVmanaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVmanaged.setStatus("current")
_SystemStatusPseudoConfirmCommit_Type = Unsigned32
_SystemStatusPseudoConfirmCommit_Object = MibScalar
systemStatusPseudoConfirmCommit = _SystemStatusPseudoConfirmCommit_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 37),
    _SystemStatusPseudoConfirmCommit_Type()
)
systemStatusPseudoConfirmCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusPseudoConfirmCommit.setStatus("current")


class _SystemStatusConfigTemplateName_Type(String):
    """Custom type systemStatusConfigTemplateName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatusConfigTemplateName_Type.__name__ = "String"
_SystemStatusConfigTemplateName_Object = MibScalar
systemStatusConfigTemplateName = _SystemStatusConfigTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 38),
    _SystemStatusConfigTemplateName_Type()
)
systemStatusConfigTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusConfigTemplateName.setStatus("current")


class _SystemStatusPolicyTemplateName_Type(String):
    """Custom type systemStatusPolicyTemplateName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatusPolicyTemplateName_Type.__name__ = "String"
_SystemStatusPolicyTemplateName_Object = MibScalar
systemStatusPolicyTemplateName = _SystemStatusPolicyTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 39),
    _SystemStatusPolicyTemplateName_Type()
)
systemStatusPolicyTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusPolicyTemplateName.setStatus("current")


class _SystemStatusPolicyTemplateVersion_Type(String):
    """Custom type systemStatusPolicyTemplateVersion based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SystemStatusPolicyTemplateVersion_Type.__name__ = "String"
_SystemStatusPolicyTemplateVersion_Object = MibScalar
systemStatusPolicyTemplateVersion = _SystemStatusPolicyTemplateVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 40),
    _SystemStatusPolicyTemplateVersion_Type()
)
systemStatusPolicyTemplateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusPolicyTemplateVersion.setStatus("current")
_SystemStatusVmanageStorageDiskFs_Type = String
_SystemStatusVmanageStorageDiskFs_Object = MibScalar
systemStatusVmanageStorageDiskFs = _SystemStatusVmanageStorageDiskFs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 41),
    _SystemStatusVmanageStorageDiskFs_Type()
)
systemStatusVmanageStorageDiskFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVmanageStorageDiskFs.setStatus("current")
_SystemStatusVmanageStorageDiskSize_Type = String
_SystemStatusVmanageStorageDiskSize_Object = MibScalar
systemStatusVmanageStorageDiskSize = _SystemStatusVmanageStorageDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 42),
    _SystemStatusVmanageStorageDiskSize_Type()
)
systemStatusVmanageStorageDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVmanageStorageDiskSize.setStatus("current")
_SystemStatusVmanageStorageDiskUsed_Type = String
_SystemStatusVmanageStorageDiskUsed_Object = MibScalar
systemStatusVmanageStorageDiskUsed = _SystemStatusVmanageStorageDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 43),
    _SystemStatusVmanageStorageDiskUsed_Type()
)
systemStatusVmanageStorageDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVmanageStorageDiskUsed.setStatus("current")
_SystemStatusVmanageStorageDiskAvail_Type = String
_SystemStatusVmanageStorageDiskAvail_Object = MibScalar
systemStatusVmanageStorageDiskAvail = _SystemStatusVmanageStorageDiskAvail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 44),
    _SystemStatusVmanageStorageDiskAvail_Type()
)
systemStatusVmanageStorageDiskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVmanageStorageDiskAvail.setStatus("current")
_SystemStatusVmanageStorageDiskUse_Type = ConfdString
_SystemStatusVmanageStorageDiskUse_Object = MibScalar
systemStatusVmanageStorageDiskUse = _SystemStatusVmanageStorageDiskUse_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 45),
    _SystemStatusVmanageStorageDiskUse_Type()
)
systemStatusVmanageStorageDiskUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVmanageStorageDiskUse.setStatus("current")
_SystemStatusVmanageStorageDiskMount_Type = String
_SystemStatusVmanageStorageDiskMount_Object = MibScalar
systemStatusVmanageStorageDiskMount = _SystemStatusVmanageStorageDiskMount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 46),
    _SystemStatusVmanageStorageDiskMount_Type()
)
systemStatusVmanageStorageDiskMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVmanageStorageDiskMount.setStatus("current")


class _SystemStatusModel_Type(Integer32):
    """Custom type systemStatusModel based on Integer32"""
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
              48,
              49,
              54,
              55,
              56,
              57,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              84,
              85,
              86,
              100,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268)
        )
    )
    namedValues = NamedValues(
        *(("vsmart", 1),
          ("vmanage", 2),
          ("vbond", 3),
          ("vedge-1000", 4),
          ("vedge-2000", 5),
          ("vedge-100", 6),
          ("vedge-100-W2", 7),
          ("vedge-100-WM", 8),
          ("vedge-100-M2", 9),
          ("vedge-100-M", 10),
          ("vedge-100-B", 11),
          ("vedge-cloud", 12),
          ("vcontainer", 13),
          ("vedge-5000", 14),
          ("vedge-CSR-1000v", 15),
          ("vedge-ISR-4331", 16),
          ("vedge-ISR-4321", 17),
          ("vedge-ISR-4351", 18),
          ("vedge-ISR-4221", 19),
          ("vedge-ASR-1001-X", 20),
          ("vedge-ASR-1001-HX", 21),
          ("vedge-ASR-1002-X", 22),
          ("vedge-ASR-1002-HX", 23),
          ("vedge-C1111-8PLTEEA", 24),
          ("vedge-C1111-8PLTELA", 25),
          ("vedge-C1117-4PLTEEA", 26),
          ("vedge-C1117-4PLTELA", 27),
          ("vedge-C1116-4PLTEEA", 28),
          ("vedge-C1116-4PLTELA", 29),
          ("vedge-ISRv", 30),
          ("vedge-C1111-8P", 31),
          ("vedge-C1111-4PLTEEA", 32),
          ("vedge-C1111-4PLTELA", 33),
          ("vedge-C1117-4PMLTEEA", 34),
          ("vedge-C1111-4P", 35),
          ("vedge-C1116-4P", 36),
          ("vedge-C1117-4P", 37),
          ("vedge-C1117-4PM", 38),
          ("vedge-C1101-4P", 39),
          ("vedge-C1101-4PLTEP", 40),
          ("vedge-C1111X-8P", 41),
          ("vedge-C1111-8PLTEEAW", 42),
          ("vedge-C1111-8PW", 43),
          ("vedge-ISR-4431", 44),
          ("vedge-ISR-4451-X", 45),
          ("vedge-ISR-4221X", 46),
          ("vedge-ISR-4461", 47),
          ("vedge-C8300-1N1S-6G", 48),
          ("vedge-C8300-1N1S-4G2X", 49),
          ("vedge-CE-9515", 54),
          ("vedge-CE-9511", 55),
          ("vedge-IR-1101", 56),
          ("vedge-C1121X-8PLTEPW", 57),
          ("vedge-C1161X-8P", 60),
          ("vedge-C1161X-8PLTEP", 61),
          ("vedge-C1111-8PLTEAEAW", 62),
          ("vedge-C1121-8P", 63),
          ("vedge-C1121-8PLTEP", 64),
          ("vedge-C1121X-8PLTEPWA", 65),
          ("vedge-C1127X-8PMLTEP", 66),
          ("vedge-C1109-4PLTE2P", 68),
          ("vedge-C1101-4PLTEPW", 69),
          ("vedge-C1109-4PLTE2PW", 70),
          ("vedge-C1111-8PLTELAW", 71),
          ("vedge-C1121X-8P", 72),
          ("vedge-C1121X-8PLTEP", 73),
          ("vedge-C1126X-8PLTEP", 74),
          ("vedge-C1127X-8PLTEP", 75),
          ("vedge-C8500-12X4QC", 76),
          ("vedge-C8500-12X", 77),
          ("vedge-C1121-8PLTEPW", 78),
          ("vedge-C1113-8PMLTEEA", 79),
          ("vedge-ISR1100-4G", 80),
          ("vedge-ISR1100-4GLTE", 81),
          ("vedge-ISR1100-6G", 82),
          ("vedge-C8300-2N2S-6G", 84),
          ("vedge-C8300-2N2S-4G2X", 85),
          ("vedge-C8500L-8G4X", 86),
          ("vedge-sim", 100),
          ("vedge-NFVIS-ENCS5100", 200),
          ("vedge-NFVIS-ENCS5400", 201),
          ("vedge-NFVIS-UCSC-M5", 202),
          ("vedge-NFVIS-UCSC-E", 203),
          ("vedge-NFVIS-CSP2100", 204),
          ("vedge-NFVIS-CSP2100-X1", 205),
          ("vedge-NFVIS-CSP2100-X2", 206),
          ("vedge-NFVIS-CSP2100-CSP-5444", 207),
          ("vedge-C1161-8P", 212),
          ("vedge-C1161-8PLTEP", 213),
          ("vedge-C1126-8PLTEP", 214),
          ("vedge-C1127-8PLTEP", 215),
          ("vedge-C1127-8PMLTEP", 216),
          ("vedge-C1121-4P", 217),
          ("vedge-C1121-4PLTEP", 218),
          ("vedge-C1128-8PLTEP", 219),
          ("vedge-C1111-4PW", 220),
          ("vedge-C1112-8P", 221),
          ("vedge-C1112-8PLTEEA", 222),
          ("vedge-C1112-8PLTEEAW", 223),
          ("vedge-C1112-8PW", 224),
          ("vedge-C1113-8P", 225),
          ("vedge-C1113-8PLTEEA", 226),
          ("vedge-C1113-8PLTEEAW", 227),
          ("vedge-C1113-8PLTELAW", 228),
          ("vedge-C1113-8PLTELA", 229),
          ("vedge-C1113-8PM", 230),
          ("vedge-C1113-8PMW", 231),
          ("vedge-C1113-8PW", 232),
          ("vedge-C1116-4PLTEEAW", 233),
          ("vedge-C1116-4PW", 234),
          ("vedge-C1117-4PLTEEAW", 235),
          ("vedge-C1117-4PMLTEEAW", 236),
          ("vedge-C1117-4PMW", 237),
          ("vedge-C1117-4PW", 238),
          ("vedge-C1118-8P", 239),
          ("vedge-C1109-2PLTEGB", 240),
          ("vedge-C1109-2PLTEUS", 241),
          ("vedge-C1109-2PLTEVZ", 242),
          ("vedge-C1113-8PLTEW", 243),
          ("vedge-C1112-8PLTEEAWE", 244),
          ("vedge-C1112-8PWE", 245),
          ("vedge-C1113-8PLTELAWZ", 246),
          ("vedge-C1113-8PMWE", 247),
          ("vedge-C1116-4PLTEEAWE", 248),
          ("vedge-C1116-4PWE", 249),
          ("vedge-C1117-4PLTEEAWA", 250),
          ("vedge-C1117-4PMLTEEAWE", 251),
          ("vedge-C1117-4PMWE", 252),
          ("vedge-C8200-1N-4G", 253),
          ("vedge-ISR1100-4GLTE-XE", 254),
          ("vedge-ISR1100-4G-XE", 255),
          ("vedge-ISR1100-6G-XE", 256),
          ("vedge-NFVIS-C8200-UCPE", 257),
          ("vedge-C8300-1N1S-6T", 258),
          ("vedge-C8300-1N1S-4T2X", 259),
          ("vedge-C8300-2N2S-6T", 260),
          ("vedge-C8300-2N2S-4T2X", 261),
          ("vedge-C8200-1N-4T", 262),
          ("vedge-ESR-6300", 263),
          ("vedge-C8000V", 264),
          ("vedge-ISR1100X-4G", 265),
          ("vedge-ISR1100X-6G", 266),
          ("vedge-ISR1100X-4G-XE", 267),
          ("vedge-ISR1100X-6G-XE", 268))
    )


_SystemStatusModel_Type.__name__ = "Integer32"
_SystemStatusModel_Object = MibScalar
systemStatusModel = _SystemStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 47),
    _SystemStatusModel_Type()
)
systemStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusModel.setStatus("current")
_SystemStatusRebootType_Type = String
_SystemStatusRebootType_Object = MibScalar
systemStatusRebootType = _SystemStatusRebootType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 48),
    _SystemStatusRebootType_Type()
)
systemStatusRebootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusRebootType.setStatus("current")
_SystemStatusTotalCpuCount_Type = Unsigned32
_SystemStatusTotalCpuCount_Object = MibScalar
systemStatusTotalCpuCount = _SystemStatusTotalCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 49),
    _SystemStatusTotalCpuCount_Type()
)
systemStatusTotalCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusTotalCpuCount.setStatus("current")
_SystemStatusFpCpuCount_Type = Unsigned32
_SystemStatusFpCpuCount_Object = MibScalar
systemStatusFpCpuCount = _SystemStatusFpCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 50),
    _SystemStatusFpCpuCount_Type()
)
systemStatusFpCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusFpCpuCount.setStatus("current")
_SystemStatusLinuxCpuCount_Type = Unsigned32
_SystemStatusLinuxCpuCount_Object = MibScalar
systemStatusLinuxCpuCount = _SystemStatusLinuxCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 51),
    _SystemStatusLinuxCpuCount_Type()
)
systemStatusLinuxCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusLinuxCpuCount.setStatus("current")
_SystemStatusBootloaderVersion_Type = String
_SystemStatusBootloaderVersion_Object = MibScalar
systemStatusBootloaderVersion = _SystemStatusBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 52),
    _SystemStatusBootloaderVersion_Type()
)
systemStatusBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusBootloaderVersion.setStatus("current")
_SystemStatusBuildNumber_Type = String
_SystemStatusBuildNumber_Object = MibScalar
systemStatusBuildNumber = _SystemStatusBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 53),
    _SystemStatusBuildNumber_Type()
)
systemStatusBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusBuildNumber.setStatus("current")


class _SystemStatusState_Type(Integer32):
    """Custom type systemStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blkng-green", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_SystemStatusState_Type.__name__ = "Integer32"
_SystemStatusState_Object = MibScalar
systemStatusState = _SystemStatusState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 54),
    _SystemStatusState_Type()
)
systemStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusState.setStatus("current")
_SystemStatusSystemStateDescription_Type = String
_SystemStatusSystemStateDescription_Object = MibScalar
systemStatusSystemStateDescription = _SystemStatusSystemStateDescription_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 55),
    _SystemStatusSystemStateDescription_Type()
)
systemStatusSystemStateDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemStateDescription.setStatus("current")
_SystemStatusSystemModelSku_Type = String
_SystemStatusSystemModelSku_Object = MibScalar
systemStatusSystemModelSku = _SystemStatusSystemModelSku_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 56),
    _SystemStatusSystemModelSku_Type()
)
systemStatusSystemModelSku.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemModelSku.setStatus("current")
_SystemStatusTcpdCpuCount_Type = Unsigned32
_SystemStatusTcpdCpuCount_Object = MibScalar
systemStatusTcpdCpuCount = _SystemStatusTcpdCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 57),
    _SystemStatusTcpdCpuCount_Type()
)
systemStatusTcpdCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusTcpdCpuCount.setStatus("current")


class _SystemStatusSystemFipsMode_Type(Integer32):
    """Custom type systemStatusSystemFipsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_SystemStatusSystemFipsMode_Type.__name__ = "Integer32"
_SystemStatusSystemFipsMode_Object = MibScalar
systemStatusSystemFipsMode = _SystemStatusSystemFipsMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 58),
    _SystemStatusSystemFipsMode_Type()
)
systemStatusSystemFipsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemFipsMode.setStatus("current")
_SystemStatusSystemTestbedMode_Type = Unsigned32
_SystemStatusSystemTestbedMode_Object = MibScalar
systemStatusSystemTestbedMode = _SystemStatusSystemTestbedMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 59),
    _SystemStatusSystemTestbedMode_Type()
)
systemStatusSystemTestbedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemTestbedMode.setStatus("current")
_SystemStatusSystemCtrlCompatibility_Type = String
_SystemStatusSystemCtrlCompatibility_Object = MibScalar
systemStatusSystemCtrlCompatibility = _SystemStatusSystemCtrlCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 60),
    _SystemStatusSystemCtrlCompatibility_Type()
)
systemStatusSystemCtrlCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemCtrlCompatibility.setStatus("current")
_SystemStatusSystemTimezone_Type = String
_SystemStatusSystemTimezone_Object = MibScalar
systemStatusSystemTimezone = _SystemStatusSystemTimezone_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 61),
    _SystemStatusSystemTimezone_Type()
)
systemStatusSystemTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemTimezone.setStatus("current")
_SystemStatusSystemEngineeringSigned_Type = Unsigned32
_SystemStatusSystemEngineeringSigned_Object = MibScalar
systemStatusSystemEngineeringSigned = _SystemStatusSystemEngineeringSigned_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 62),
    _SystemStatusSystemEngineeringSigned_Type()
)
systemStatusSystemEngineeringSigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemEngineeringSigned.setStatus("current")
_SystemStatusSystemLiLicenseEnabled_Type = Unsigned32
_SystemStatusSystemLiLicenseEnabled_Object = MibScalar
systemStatusSystemLiLicenseEnabled = _SystemStatusSystemLiLicenseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 63),
    _SystemStatusSystemLiLicenseEnabled_Type()
)
systemStatusSystemLiLicenseEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemLiLicenseEnabled.setStatus("current")
_SystemStatusSystemChassisSerialNumber_Type = String
_SystemStatusSystemChassisSerialNumber_Object = MibScalar
systemStatusSystemChassisSerialNumber = _SystemStatusSystemChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 64),
    _SystemStatusSystemChassisSerialNumber_Type()
)
systemStatusSystemChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemChassisSerialNumber.setStatus("current")
_SystemStatusProcs_Type = Unsigned32
_SystemStatusProcs_Object = MibScalar
systemStatusProcs = _SystemStatusProcs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 100),
    _SystemStatusProcs_Type()
)
systemStatusProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusProcs.setStatus("current")
_SystemStatusDiskBsize_Type = ConfdString
_SystemStatusDiskBsize_Object = MibScalar
systemStatusDiskBsize = _SystemStatusDiskBsize_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 101),
    _SystemStatusDiskBsize_Type()
)
systemStatusDiskBsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskBsize.setStatus("current")
_SystemStatusDiskBlocks_Type = ConfdString
_SystemStatusDiskBlocks_Object = MibScalar
systemStatusDiskBlocks = _SystemStatusDiskBlocks_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 102),
    _SystemStatusDiskBlocks_Type()
)
systemStatusDiskBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskBlocks.setStatus("current")
_SystemStatusDiskBused_Type = ConfdString
_SystemStatusDiskBused_Object = MibScalar
systemStatusDiskBused = _SystemStatusDiskBused_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 103),
    _SystemStatusDiskBused_Type()
)
systemStatusDiskBused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskBused.setStatus("current")
_SystemStatusDiskBavail_Type = ConfdString
_SystemStatusDiskBavail_Object = MibScalar
systemStatusDiskBavail = _SystemStatusDiskBavail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 1, 104),
    _SystemStatusDiskBavail_Type()
)
systemStatusDiskBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskBavail.setStatus("current")
_SystemStatistics_ObjectIdentity = ObjectIdentity
systemStatistics = _SystemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2)
)
_SystemStatisticsRxPkts_Type = Counter64
_SystemStatisticsRxPkts_Object = MibScalar
systemStatisticsRxPkts = _SystemStatisticsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 1),
    _SystemStatisticsRxPkts_Type()
)
systemStatisticsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxPkts.setStatus("current")
_SystemStatisticsRxDrops_Type = Counter64
_SystemStatisticsRxDrops_Object = MibScalar
systemStatisticsRxDrops = _SystemStatisticsRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 2),
    _SystemStatisticsRxDrops_Type()
)
systemStatisticsRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxDrops.setStatus("current")
_SystemStatisticsIpFwd_Type = Counter64
_SystemStatisticsIpFwd_Object = MibScalar
systemStatisticsIpFwd = _SystemStatisticsIpFwd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 3),
    _SystemStatisticsIpFwd_Type()
)
systemStatisticsIpFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwd.setStatus("current")
_SystemStatisticsIpFwdMirrorPkts_Type = Counter64
_SystemStatisticsIpFwdMirrorPkts_Object = MibScalar
systemStatisticsIpFwdMirrorPkts = _SystemStatisticsIpFwdMirrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 4),
    _SystemStatisticsIpFwdMirrorPkts_Type()
)
systemStatisticsIpFwdMirrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdMirrorPkts.setStatus("current")
_SystemStatisticsIpFwdArp_Type = Counter64
_SystemStatisticsIpFwdArp_Object = MibScalar
systemStatisticsIpFwdArp = _SystemStatisticsIpFwdArp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 5),
    _SystemStatisticsIpFwdArp_Type()
)
systemStatisticsIpFwdArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdArp.setStatus("current")
_SystemStatisticsIpFwdToEgress_Type = Counter64
_SystemStatisticsIpFwdToEgress_Object = MibScalar
systemStatisticsIpFwdToEgress = _SystemStatisticsIpFwdToEgress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 6),
    _SystemStatisticsIpFwdToEgress_Type()
)
systemStatisticsIpFwdToEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdToEgress.setStatus("current")
_SystemStatisticsIpFwdInvalidOil_Type = Counter64
_SystemStatisticsIpFwdInvalidOil_Object = MibScalar
systemStatisticsIpFwdInvalidOil = _SystemStatisticsIpFwdInvalidOil_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 7),
    _SystemStatisticsIpFwdInvalidOil_Type()
)
systemStatisticsIpFwdInvalidOil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdInvalidOil.setStatus("current")
_SystemStatisticsIpV6McastDrops_Type = Counter64
_SystemStatisticsIpV6McastDrops_Object = MibScalar
systemStatisticsIpV6McastDrops = _SystemStatisticsIpV6McastDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 8),
    _SystemStatisticsIpV6McastDrops_Type()
)
systemStatisticsIpV6McastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpV6McastDrops.setStatus("current")
_SystemStatisticsIpFwdMcastInvalidIif_Type = Counter64
_SystemStatisticsIpFwdMcastInvalidIif_Object = MibScalar
systemStatisticsIpFwdMcastInvalidIif = _SystemStatisticsIpFwdMcastInvalidIif_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 9),
    _SystemStatisticsIpFwdMcastInvalidIif_Type()
)
systemStatisticsIpFwdMcastInvalidIif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdMcastInvalidIif.setStatus("current")
_SystemStatisticsIpFwdMcastLifeExceededDrops_Type = Counter64
_SystemStatisticsIpFwdMcastLifeExceededDrops_Object = MibScalar
systemStatisticsIpFwdMcastLifeExceededDrops = _SystemStatisticsIpFwdMcastLifeExceededDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 10),
    _SystemStatisticsIpFwdMcastLifeExceededDrops_Type()
)
systemStatisticsIpFwdMcastLifeExceededDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdMcastLifeExceededDrops.setStatus("current")
_SystemStatisticsRxMcastThresholdExceeded_Type = Counter64
_SystemStatisticsRxMcastThresholdExceeded_Object = MibScalar
systemStatisticsRxMcastThresholdExceeded = _SystemStatisticsRxMcastThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 11),
    _SystemStatisticsRxMcastThresholdExceeded_Type()
)
systemStatisticsRxMcastThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxMcastThresholdExceeded.setStatus("current")
_SystemStatisticsIpFwdInvalidTunOil_Type = Counter64
_SystemStatisticsIpFwdInvalidTunOil_Object = MibScalar
systemStatisticsIpFwdInvalidTunOil = _SystemStatisticsIpFwdInvalidTunOil_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 12),
    _SystemStatisticsIpFwdInvalidTunOil_Type()
)
systemStatisticsIpFwdInvalidTunOil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdInvalidTunOil.setStatus("current")
_SystemStatisticsRxMcastPolicyFwdDrops_Type = Counter64
_SystemStatisticsRxMcastPolicyFwdDrops_Object = MibScalar
systemStatisticsRxMcastPolicyFwdDrops = _SystemStatisticsRxMcastPolicyFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 13),
    _SystemStatisticsRxMcastPolicyFwdDrops_Type()
)
systemStatisticsRxMcastPolicyFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxMcastPolicyFwdDrops.setStatus("current")
_SystemStatisticsRxMcastMirrorFwdDrops_Type = Counter64
_SystemStatisticsRxMcastMirrorFwdDrops_Object = MibScalar
systemStatisticsRxMcastMirrorFwdDrops = _SystemStatisticsRxMcastMirrorFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 14),
    _SystemStatisticsRxMcastMirrorFwdDrops_Type()
)
systemStatisticsRxMcastMirrorFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxMcastMirrorFwdDrops.setStatus("current")
_SystemStatisticsIpFwdNullMcastGroup_Type = Counter64
_SystemStatisticsIpFwdNullMcastGroup_Object = MibScalar
systemStatisticsIpFwdNullMcastGroup = _SystemStatisticsIpFwdNullMcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 15),
    _SystemStatisticsIpFwdNullMcastGroup_Type()
)
systemStatisticsIpFwdNullMcastGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdNullMcastGroup.setStatus("current")
_SystemStatisticsIpFwdNullNhop_Type = Counter64
_SystemStatisticsIpFwdNullNhop_Object = MibScalar
systemStatisticsIpFwdNullNhop = _SystemStatisticsIpFwdNullNhop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 16),
    _SystemStatisticsIpFwdNullNhop_Type()
)
systemStatisticsIpFwdNullNhop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdNullNhop.setStatus("current")
_SystemStatisticsIpFwdUnknownNhType_Type = Counter64
_SystemStatisticsIpFwdUnknownNhType_Object = MibScalar
systemStatisticsIpFwdUnknownNhType = _SystemStatisticsIpFwdUnknownNhType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 17),
    _SystemStatisticsIpFwdUnknownNhType_Type()
)
systemStatisticsIpFwdUnknownNhType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdUnknownNhType.setStatus("current")
_SystemStatisticsIpFwdNatOnTunnel_Type = Counter64
_SystemStatisticsIpFwdNatOnTunnel_Object = MibScalar
systemStatisticsIpFwdNatOnTunnel = _SystemStatisticsIpFwdNatOnTunnel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 18),
    _SystemStatisticsIpFwdNatOnTunnel_Type()
)
systemStatisticsIpFwdNatOnTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdNatOnTunnel.setStatus("current")
_SystemStatisticsIpFwdToCpu_Type = Counter64
_SystemStatisticsIpFwdToCpu_Object = MibScalar
systemStatisticsIpFwdToCpu = _SystemStatisticsIpFwdToCpu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 19),
    _SystemStatisticsIpFwdToCpu_Type()
)
systemStatisticsIpFwdToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdToCpu.setStatus("current")
_SystemStatisticsIpFwdToCpuNatXlates_Type = Counter64
_SystemStatisticsIpFwdToCpuNatXlates_Object = MibScalar
systemStatisticsIpFwdToCpuNatXlates = _SystemStatisticsIpFwdToCpuNatXlates_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 20),
    _SystemStatisticsIpFwdToCpuNatXlates_Type()
)
systemStatisticsIpFwdToCpuNatXlates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdToCpuNatXlates.setStatus("current")
_SystemStatisticsIpFwdFromCpuNatXlates_Type = Counter64
_SystemStatisticsIpFwdFromCpuNatXlates_Object = MibScalar
systemStatisticsIpFwdFromCpuNatXlates = _SystemStatisticsIpFwdFromCpuNatXlates_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 21),
    _SystemStatisticsIpFwdFromCpuNatXlates_Type()
)
systemStatisticsIpFwdFromCpuNatXlates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdFromCpuNatXlates.setStatus("current")
_SystemStatisticsIpFwdToCpuNatDrops_Type = Counter64
_SystemStatisticsIpFwdToCpuNatDrops_Object = MibScalar
systemStatisticsIpFwdToCpuNatDrops = _SystemStatisticsIpFwdToCpuNatDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 22),
    _SystemStatisticsIpFwdToCpuNatDrops_Type()
)
systemStatisticsIpFwdToCpuNatDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdToCpuNatDrops.setStatus("current")
_SystemStatisticsIpFwdFromCpuNonLocal_Type = Counter64
_SystemStatisticsIpFwdFromCpuNonLocal_Object = MibScalar
systemStatisticsIpFwdFromCpuNonLocal = _SystemStatisticsIpFwdFromCpuNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 23),
    _SystemStatisticsIpFwdFromCpuNonLocal_Type()
)
systemStatisticsIpFwdFromCpuNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdFromCpuNonLocal.setStatus("current")
_SystemStatisticsIpFwdRxIpsec_Type = Counter64
_SystemStatisticsIpFwdRxIpsec_Object = MibScalar
systemStatisticsIpFwdRxIpsec = _SystemStatisticsIpFwdRxIpsec_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 24),
    _SystemStatisticsIpFwdRxIpsec_Type()
)
systemStatisticsIpFwdRxIpsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdRxIpsec.setStatus("current")
_SystemStatisticsIpFwdMcastPkts_Type = Counter64
_SystemStatisticsIpFwdMcastPkts_Object = MibScalar
systemStatisticsIpFwdMcastPkts = _SystemStatisticsIpFwdMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 25),
    _SystemStatisticsIpFwdMcastPkts_Type()
)
systemStatisticsIpFwdMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdMcastPkts.setStatus("current")
_SystemStatisticsIpFwdRxGre_Type = Counter64
_SystemStatisticsIpFwdRxGre_Object = MibScalar
systemStatisticsIpFwdRxGre = _SystemStatisticsIpFwdRxGre_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 26),
    _SystemStatisticsIpFwdRxGre_Type()
)
systemStatisticsIpFwdRxGre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpFwdRxGre.setStatus("current")
_SystemStatisticsNatXlateOutbound_Type = Counter64
_SystemStatisticsNatXlateOutbound_Object = MibScalar
systemStatisticsNatXlateOutbound = _SystemStatisticsNatXlateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 27),
    _SystemStatisticsNatXlateOutbound_Type()
)
systemStatisticsNatXlateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsNatXlateOutbound.setStatus("current")
_SystemStatisticsNatXlateOutboundDrops_Type = Counter64
_SystemStatisticsNatXlateOutboundDrops_Object = MibScalar
systemStatisticsNatXlateOutboundDrops = _SystemStatisticsNatXlateOutboundDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 28),
    _SystemStatisticsNatXlateOutboundDrops_Type()
)
systemStatisticsNatXlateOutboundDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsNatXlateOutboundDrops.setStatus("current")
_SystemStatisticsNatXlateInbound_Type = Counter64
_SystemStatisticsNatXlateInbound_Object = MibScalar
systemStatisticsNatXlateInbound = _SystemStatisticsNatXlateInbound_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 29),
    _SystemStatisticsNatXlateInbound_Type()
)
systemStatisticsNatXlateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsNatXlateInbound.setStatus("current")
_SystemStatisticsNatXlateInboundFail_Type = Counter64
_SystemStatisticsNatXlateInboundFail_Object = MibScalar
systemStatisticsNatXlateInboundFail = _SystemStatisticsNatXlateInboundFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 30),
    _SystemStatisticsNatXlateInboundFail_Type()
)
systemStatisticsNatXlateInboundFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsNatXlateInboundFail.setStatus("current")
_SystemStatisticsCflowdPkts_Type = Counter64
_SystemStatisticsCflowdPkts_Object = MibScalar
systemStatisticsCflowdPkts = _SystemStatisticsCflowdPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 31),
    _SystemStatisticsCflowdPkts_Type()
)
systemStatisticsCflowdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsCflowdPkts.setStatus("current")
_SystemStatisticsNoNatNexthop_Type = Counter64
_SystemStatisticsNoNatNexthop_Object = MibScalar
systemStatisticsNoNatNexthop = _SystemStatisticsNoNatNexthop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 32),
    _SystemStatisticsNoNatNexthop_Type()
)
systemStatisticsNoNatNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsNoNatNexthop.setStatus("current")
_SystemStatisticsRxBcast_Type = Counter64
_SystemStatisticsRxBcast_Object = MibScalar
systemStatisticsRxBcast = _SystemStatisticsRxBcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 33),
    _SystemStatisticsRxBcast_Type()
)
systemStatisticsRxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxBcast.setStatus("current")
_SystemStatisticsRxMcast_Type = Counter64
_SystemStatisticsRxMcast_Object = MibScalar
systemStatisticsRxMcast = _SystemStatisticsRxMcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 34),
    _SystemStatisticsRxMcast_Type()
)
systemStatisticsRxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxMcast.setStatus("current")
_SystemStatisticsRxMcastLinkLocal_Type = Counter64
_SystemStatisticsRxMcastLinkLocal_Object = MibScalar
systemStatisticsRxMcastLinkLocal = _SystemStatisticsRxMcastLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 35),
    _SystemStatisticsRxMcastLinkLocal_Type()
)
systemStatisticsRxMcastLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxMcastLinkLocal.setStatus("current")
_SystemStatisticsRxMcastFilterToCpu_Type = Counter64
_SystemStatisticsRxMcastFilterToCpu_Object = MibScalar
systemStatisticsRxMcastFilterToCpu = _SystemStatisticsRxMcastFilterToCpu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 36),
    _SystemStatisticsRxMcastFilterToCpu_Type()
)
systemStatisticsRxMcastFilterToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxMcastFilterToCpu.setStatus("current")
_SystemStatisticsRxMcastFilterToCpuAndFwd_Type = Counter64
_SystemStatisticsRxMcastFilterToCpuAndFwd_Object = MibScalar
systemStatisticsRxMcastFilterToCpuAndFwd = _SystemStatisticsRxMcastFilterToCpuAndFwd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 37),
    _SystemStatisticsRxMcastFilterToCpuAndFwd_Type()
)
systemStatisticsRxMcastFilterToCpuAndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxMcastFilterToCpuAndFwd.setStatus("current")
_SystemStatisticsRxGreDecap_Type = Counter64
_SystemStatisticsRxGreDecap_Object = MibScalar
systemStatisticsRxGreDecap = _SystemStatisticsRxGreDecap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 38),
    _SystemStatisticsRxGreDecap_Type()
)
systemStatisticsRxGreDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxGreDecap.setStatus("current")
_SystemStatisticsRxGreDrops_Type = Counter64
_SystemStatisticsRxGreDrops_Object = MibScalar
systemStatisticsRxGreDrops = _SystemStatisticsRxGreDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 39),
    _SystemStatisticsRxGreDrops_Type()
)
systemStatisticsRxGreDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxGreDrops.setStatus("current")
_SystemStatisticsRxGrePolicerDrops_Type = Counter64
_SystemStatisticsRxGrePolicerDrops_Object = MibScalar
systemStatisticsRxGrePolicerDrops = _SystemStatisticsRxGrePolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 40),
    _SystemStatisticsRxGrePolicerDrops_Type()
)
systemStatisticsRxGrePolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxGrePolicerDrops.setStatus("current")
_SystemStatisticsRxImplicitAclDrops_Type = Counter64
_SystemStatisticsRxImplicitAclDrops_Object = MibScalar
systemStatisticsRxImplicitAclDrops = _SystemStatisticsRxImplicitAclDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 41),
    _SystemStatisticsRxImplicitAclDrops_Type()
)
systemStatisticsRxImplicitAclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxImplicitAclDrops.setStatus("current")
_SystemStatisticsRxIpsecDecap_Type = Counter64
_SystemStatisticsRxIpsecDecap_Object = MibScalar
systemStatisticsRxIpsecDecap = _SystemStatisticsRxIpsecDecap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 42),
    _SystemStatisticsRxIpsecDecap_Type()
)
systemStatisticsRxIpsecDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIpsecDecap.setStatus("current")
_SystemStatisticsRxIp6IpsecDrops_Type = Counter64
_SystemStatisticsRxIp6IpsecDrops_Object = MibScalar
systemStatisticsRxIp6IpsecDrops = _SystemStatisticsRxIp6IpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 43),
    _SystemStatisticsRxIp6IpsecDrops_Type()
)
systemStatisticsRxIp6IpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIp6IpsecDrops.setStatus("current")
_SystemStatisticsRxSaIpsecDrops_Type = Counter64
_SystemStatisticsRxSaIpsecDrops_Object = MibScalar
systemStatisticsRxSaIpsecDrops = _SystemStatisticsRxSaIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 44),
    _SystemStatisticsRxSaIpsecDrops_Type()
)
systemStatisticsRxSaIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxSaIpsecDrops.setStatus("current")
_SystemStatisticsRxInvalidIpsecPktSize_Type = Counter64
_SystemStatisticsRxInvalidIpsecPktSize_Object = MibScalar
systemStatisticsRxInvalidIpsecPktSize = _SystemStatisticsRxInvalidIpsecPktSize_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 45),
    _SystemStatisticsRxInvalidIpsecPktSize_Type()
)
systemStatisticsRxInvalidIpsecPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxInvalidIpsecPktSize.setStatus("current")
_SystemStatisticsRxSpiIpsecDrops_Type = Counter64
_SystemStatisticsRxSpiIpsecDrops_Object = MibScalar
systemStatisticsRxSpiIpsecDrops = _SystemStatisticsRxSpiIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 46),
    _SystemStatisticsRxSpiIpsecDrops_Type()
)
systemStatisticsRxSpiIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxSpiIpsecDrops.setStatus("current")
_SystemStatisticsRxReplayDrops_Type = Counter64
_SystemStatisticsRxReplayDrops_Object = MibScalar
systemStatisticsRxReplayDrops = _SystemStatisticsRxReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 47),
    _SystemStatisticsRxReplayDrops_Type()
)
systemStatisticsRxReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDrops.setStatus("current")
_SystemStatisticsRxReplayIntegrityDrops_Type = Counter64
_SystemStatisticsRxReplayIntegrityDrops_Object = MibScalar
systemStatisticsRxReplayIntegrityDrops = _SystemStatisticsRxReplayIntegrityDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 48),
    _SystemStatisticsRxReplayIntegrityDrops_Type()
)
systemStatisticsRxReplayIntegrityDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDrops.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDrops_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDrops_Object = MibScalar
systemStatisticsRxUnexpectedReplayDrops = _SystemStatisticsRxUnexpectedReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 49),
    _SystemStatisticsRxUnexpectedReplayDrops_Type()
)
systemStatisticsRxUnexpectedReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDrops.setStatus("current")
_SystemStatisticsRxNextHdrIpsecDrops_Type = Counter64
_SystemStatisticsRxNextHdrIpsecDrops_Object = MibScalar
systemStatisticsRxNextHdrIpsecDrops = _SystemStatisticsRxNextHdrIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 50),
    _SystemStatisticsRxNextHdrIpsecDrops_Type()
)
systemStatisticsRxNextHdrIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxNextHdrIpsecDrops.setStatus("current")
_SystemStatisticsRxMacCompareIpsecDrops_Type = Counter64
_SystemStatisticsRxMacCompareIpsecDrops_Object = MibScalar
systemStatisticsRxMacCompareIpsecDrops = _SystemStatisticsRxMacCompareIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 51),
    _SystemStatisticsRxMacCompareIpsecDrops_Type()
)
systemStatisticsRxMacCompareIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxMacCompareIpsecDrops.setStatus("current")
_SystemStatisticsRxErrPadIpsecDrops_Type = Counter64
_SystemStatisticsRxErrPadIpsecDrops_Object = MibScalar
systemStatisticsRxErrPadIpsecDrops = _SystemStatisticsRxErrPadIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 52),
    _SystemStatisticsRxErrPadIpsecDrops_Type()
)
systemStatisticsRxErrPadIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxErrPadIpsecDrops.setStatus("current")
_SystemStatisticsRxIpsecPolicerDrops_Type = Counter64
_SystemStatisticsRxIpsecPolicerDrops_Object = MibScalar
systemStatisticsRxIpsecPolicerDrops = _SystemStatisticsRxIpsecPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 53),
    _SystemStatisticsRxIpsecPolicerDrops_Type()
)
systemStatisticsRxIpsecPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIpsecPolicerDrops.setStatus("current")
_SystemStatisticsRxPreIpsecPkts_Type = Counter64
_SystemStatisticsRxPreIpsecPkts_Object = MibScalar
systemStatisticsRxPreIpsecPkts = _SystemStatisticsRxPreIpsecPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 54),
    _SystemStatisticsRxPreIpsecPkts_Type()
)
systemStatisticsRxPreIpsecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxPreIpsecPkts.setStatus("current")
_SystemStatisticsRxPreIpsecDrops_Type = Counter64
_SystemStatisticsRxPreIpsecDrops_Object = MibScalar
systemStatisticsRxPreIpsecDrops = _SystemStatisticsRxPreIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 55),
    _SystemStatisticsRxPreIpsecDrops_Type()
)
systemStatisticsRxPreIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxPreIpsecDrops.setStatus("current")
_SystemStatisticsRxPreIpsecPolicerDrops_Type = Counter64
_SystemStatisticsRxPreIpsecPolicerDrops_Object = MibScalar
systemStatisticsRxPreIpsecPolicerDrops = _SystemStatisticsRxPreIpsecPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 56),
    _SystemStatisticsRxPreIpsecPolicerDrops_Type()
)
systemStatisticsRxPreIpsecPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxPreIpsecPolicerDrops.setStatus("current")
_SystemStatisticsRxPreIpsecDecap_Type = Counter64
_SystemStatisticsRxPreIpsecDecap_Object = MibScalar
systemStatisticsRxPreIpsecDecap = _SystemStatisticsRxPreIpsecDecap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 57),
    _SystemStatisticsRxPreIpsecDecap_Type()
)
systemStatisticsRxPreIpsecDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxPreIpsecDecap.setStatus("current")
_SystemStatisticsOpensslAesDecrypt_Type = Counter64
_SystemStatisticsOpensslAesDecrypt_Object = MibScalar
systemStatisticsOpensslAesDecrypt = _SystemStatisticsOpensslAesDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 58),
    _SystemStatisticsOpensslAesDecrypt_Type()
)
systemStatisticsOpensslAesDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsOpensslAesDecrypt.setStatus("current")
_SystemStatisticsRxIpsecBadInner_Type = Counter64
_SystemStatisticsRxIpsecBadInner_Object = MibScalar
systemStatisticsRxIpsecBadInner = _SystemStatisticsRxIpsecBadInner_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 59),
    _SystemStatisticsRxIpsecBadInner_Type()
)
systemStatisticsRxIpsecBadInner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIpsecBadInner.setStatus("current")
_SystemStatisticsRxBadLabel_Type = Counter64
_SystemStatisticsRxBadLabel_Object = MibScalar
systemStatisticsRxBadLabel = _SystemStatisticsRxBadLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 60),
    _SystemStatisticsRxBadLabel_Type()
)
systemStatisticsRxBadLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxBadLabel.setStatus("current")
_SystemStatisticsServiceLabelFwd_Type = Counter64
_SystemStatisticsServiceLabelFwd_Object = MibScalar
systemStatisticsServiceLabelFwd = _SystemStatisticsServiceLabelFwd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 61),
    _SystemStatisticsServiceLabelFwd_Type()
)
systemStatisticsServiceLabelFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsServiceLabelFwd.setStatus("current")
_SystemStatisticsRxHostLocalPkt_Type = Counter64
_SystemStatisticsRxHostLocalPkt_Object = MibScalar
systemStatisticsRxHostLocalPkt = _SystemStatisticsRxHostLocalPkt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 62),
    _SystemStatisticsRxHostLocalPkt_Type()
)
systemStatisticsRxHostLocalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxHostLocalPkt.setStatus("current")
_SystemStatisticsRxHostMirrorDrops_Type = Counter64
_SystemStatisticsRxHostMirrorDrops_Object = MibScalar
systemStatisticsRxHostMirrorDrops = _SystemStatisticsRxHostMirrorDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 63),
    _SystemStatisticsRxHostMirrorDrops_Type()
)
systemStatisticsRxHostMirrorDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxHostMirrorDrops.setStatus("current")
_SystemStatisticsRxTunneledPkts_Type = Counter64
_SystemStatisticsRxTunneledPkts_Object = MibScalar
systemStatisticsRxTunneledPkts = _SystemStatisticsRxTunneledPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 64),
    _SystemStatisticsRxTunneledPkts_Type()
)
systemStatisticsRxTunneledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxTunneledPkts.setStatus("current")
_SystemStatisticsRxCpNonLocal_Type = Counter64
_SystemStatisticsRxCpNonLocal_Object = MibScalar
systemStatisticsRxCpNonLocal = _SystemStatisticsRxCpNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 65),
    _SystemStatisticsRxCpNonLocal_Type()
)
systemStatisticsRxCpNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxCpNonLocal.setStatus("current")
_SystemStatisticsTxIfNotPreferred_Type = Counter64
_SystemStatisticsTxIfNotPreferred_Object = MibScalar
systemStatisticsTxIfNotPreferred = _SystemStatisticsTxIfNotPreferred_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 66),
    _SystemStatisticsTxIfNotPreferred_Type()
)
systemStatisticsTxIfNotPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIfNotPreferred.setStatus("current")
_SystemStatisticsTxVsmartDrop_Type = Counter64
_SystemStatisticsTxVsmartDrop_Object = MibScalar
systemStatisticsTxVsmartDrop = _SystemStatisticsTxVsmartDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 67),
    _SystemStatisticsTxVsmartDrop_Type()
)
systemStatisticsTxVsmartDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxVsmartDrop.setStatus("current")
_SystemStatisticsRxInvalidPort_Type = Counter64
_SystemStatisticsRxInvalidPort_Object = MibScalar
systemStatisticsRxInvalidPort = _SystemStatisticsRxInvalidPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 68),
    _SystemStatisticsRxInvalidPort_Type()
)
systemStatisticsRxInvalidPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxInvalidPort.setStatus("current")
_SystemStatisticsPortDisabledRx_Type = Counter64
_SystemStatisticsPortDisabledRx_Object = MibScalar
systemStatisticsPortDisabledRx = _SystemStatisticsPortDisabledRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 69),
    _SystemStatisticsPortDisabledRx_Type()
)
systemStatisticsPortDisabledRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsPortDisabledRx.setStatus("current")
_SystemStatisticsIpDisabledRx_Type = Counter64
_SystemStatisticsIpDisabledRx_Object = MibScalar
systemStatisticsIpDisabledRx = _SystemStatisticsIpDisabledRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 70),
    _SystemStatisticsIpDisabledRx_Type()
)
systemStatisticsIpDisabledRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpDisabledRx.setStatus("current")
_SystemStatisticsRxInvalidQtags_Type = Counter64
_SystemStatisticsRxInvalidQtags_Object = MibScalar
systemStatisticsRxInvalidQtags = _SystemStatisticsRxInvalidQtags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 71),
    _SystemStatisticsRxInvalidQtags_Type()
)
systemStatisticsRxInvalidQtags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxInvalidQtags.setStatus("current")
_SystemStatisticsRxNonIpDrops_Type = Counter64
_SystemStatisticsRxNonIpDrops_Object = MibScalar
systemStatisticsRxNonIpDrops = _SystemStatisticsRxNonIpDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 72),
    _SystemStatisticsRxNonIpDrops_Type()
)
systemStatisticsRxNonIpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxNonIpDrops.setStatus("current")
_SystemStatisticsRxIpErrs_Type = Counter64
_SystemStatisticsRxIpErrs_Object = MibScalar
systemStatisticsRxIpErrs = _SystemStatisticsRxIpErrs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 73),
    _SystemStatisticsRxIpErrs_Type()
)
systemStatisticsRxIpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIpErrs.setStatus("current")
_SystemStatisticsPkoWredDrops_Type = Counter64
_SystemStatisticsPkoWredDrops_Object = MibScalar
systemStatisticsPkoWredDrops = _SystemStatisticsPkoWredDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 74),
    _SystemStatisticsPkoWredDrops_Type()
)
systemStatisticsPkoWredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsPkoWredDrops.setStatus("current")
_SystemStatisticsTxQueueExceeded_Type = Counter64
_SystemStatisticsTxQueueExceeded_Object = MibScalar
systemStatisticsTxQueueExceeded = _SystemStatisticsTxQueueExceeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 75),
    _SystemStatisticsTxQueueExceeded_Type()
)
systemStatisticsTxQueueExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxQueueExceeded.setStatus("current")
_SystemStatisticsRxPolicerDrops_Type = Counter64
_SystemStatisticsRxPolicerDrops_Object = MibScalar
systemStatisticsRxPolicerDrops = _SystemStatisticsRxPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 76),
    _SystemStatisticsRxPolicerDrops_Type()
)
systemStatisticsRxPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxPolicerDrops.setStatus("current")
_SystemStatisticsRouteToHost_Type = Counter64
_SystemStatisticsRouteToHost_Object = MibScalar
systemStatisticsRouteToHost = _SystemStatisticsRouteToHost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 77),
    _SystemStatisticsRouteToHost_Type()
)
systemStatisticsRouteToHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRouteToHost.setStatus("current")
_SystemStatisticsTtlExpired_Type = Counter64
_SystemStatisticsTtlExpired_Object = MibScalar
systemStatisticsTtlExpired = _SystemStatisticsTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 78),
    _SystemStatisticsTtlExpired_Type()
)
systemStatisticsTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTtlExpired.setStatus("current")
_SystemStatisticsIcmpRedirect_Type = Counter64
_SystemStatisticsIcmpRedirect_Object = MibScalar
systemStatisticsIcmpRedirect = _SystemStatisticsIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 79),
    _SystemStatisticsIcmpRedirect_Type()
)
systemStatisticsIcmpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIcmpRedirect.setStatus("current")
_SystemStatisticsBfdRxNonIp_Type = Counter64
_SystemStatisticsBfdRxNonIp_Object = MibScalar
systemStatisticsBfdRxNonIp = _SystemStatisticsBfdRxNonIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 80),
    _SystemStatisticsBfdRxNonIp_Type()
)
systemStatisticsBfdRxNonIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdRxNonIp.setStatus("current")
_SystemStatisticsBfdTxRecordChanged_Type = Counter64
_SystemStatisticsBfdTxRecordChanged_Object = MibScalar
systemStatisticsBfdTxRecordChanged = _SystemStatisticsBfdTxRecordChanged_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 81),
    _SystemStatisticsBfdTxRecordChanged_Type()
)
systemStatisticsBfdTxRecordChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdTxRecordChanged.setStatus("current")
_SystemStatisticsBfdRxRecordInvalid_Type = Counter64
_SystemStatisticsBfdRxRecordInvalid_Object = MibScalar
systemStatisticsBfdRxRecordInvalid = _SystemStatisticsBfdRxRecordInvalid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 82),
    _SystemStatisticsBfdRxRecordInvalid_Type()
)
systemStatisticsBfdRxRecordInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdRxRecordInvalid.setStatus("current")
_SystemStatisticsBfdRxParseErr_Type = Counter64
_SystemStatisticsBfdRxParseErr_Object = MibScalar
systemStatisticsBfdRxParseErr = _SystemStatisticsBfdRxParseErr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 83),
    _SystemStatisticsBfdRxParseErr_Type()
)
systemStatisticsBfdRxParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdRxParseErr.setStatus("current")
_SystemStatisticsRxArpRateLimitDrops_Type = Counter64
_SystemStatisticsRxArpRateLimitDrops_Object = MibScalar
systemStatisticsRxArpRateLimitDrops = _SystemStatisticsRxArpRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 84),
    _SystemStatisticsRxArpRateLimitDrops_Type()
)
systemStatisticsRxArpRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxArpRateLimitDrops.setStatus("current")
_SystemStatisticsRxArpNonLocalDrops_Type = Counter64
_SystemStatisticsRxArpNonLocalDrops_Object = MibScalar
systemStatisticsRxArpNonLocalDrops = _SystemStatisticsRxArpNonLocalDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 85),
    _SystemStatisticsRxArpNonLocalDrops_Type()
)
systemStatisticsRxArpNonLocalDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxArpNonLocalDrops.setStatus("current")
_SystemStatisticsRxArpReqs_Type = Counter64
_SystemStatisticsRxArpReqs_Object = MibScalar
systemStatisticsRxArpReqs = _SystemStatisticsRxArpReqs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 86),
    _SystemStatisticsRxArpReqs_Type()
)
systemStatisticsRxArpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxArpReqs.setStatus("current")
_SystemStatisticsRxArpReplies_Type = Counter64
_SystemStatisticsRxArpReplies_Object = MibScalar
systemStatisticsRxArpReplies = _SystemStatisticsRxArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 87),
    _SystemStatisticsRxArpReplies_Type()
)
systemStatisticsRxArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxArpReplies.setStatus("current")
_SystemStatisticsArpAddFail_Type = Counter64
_SystemStatisticsArpAddFail_Object = MibScalar
systemStatisticsArpAddFail = _SystemStatisticsArpAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 88),
    _SystemStatisticsArpAddFail_Type()
)
systemStatisticsArpAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsArpAddFail.setStatus("current")
_SystemStatisticsUnknownNhType_Type = Counter64
_SystemStatisticsUnknownNhType_Object = MibScalar
systemStatisticsUnknownNhType = _SystemStatisticsUnknownNhType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 89),
    _SystemStatisticsUnknownNhType_Type()
)
systemStatisticsUnknownNhType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsUnknownNhType.setStatus("current")
_SystemStatisticsBufAllocFails_Type = Counter64
_SystemStatisticsBufAllocFails_Object = MibScalar
systemStatisticsBufAllocFails = _SystemStatisticsBufAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 90),
    _SystemStatisticsBufAllocFails_Type()
)
systemStatisticsBufAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBufAllocFails.setStatus("current")
_SystemStatisticsEcmpDiscards_Type = Counter64
_SystemStatisticsEcmpDiscards_Object = MibScalar
systemStatisticsEcmpDiscards = _SystemStatisticsEcmpDiscards_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 91),
    _SystemStatisticsEcmpDiscards_Type()
)
systemStatisticsEcmpDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsEcmpDiscards.setStatus("current")
_SystemStatisticsAppRoutePolicyDiscards_Type = Counter64
_SystemStatisticsAppRoutePolicyDiscards_Object = MibScalar
systemStatisticsAppRoutePolicyDiscards = _SystemStatisticsAppRoutePolicyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 92),
    _SystemStatisticsAppRoutePolicyDiscards_Type()
)
systemStatisticsAppRoutePolicyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsAppRoutePolicyDiscards.setStatus("current")
_SystemStatisticsCbfDiscards_Type = Counter64
_SystemStatisticsCbfDiscards_Object = MibScalar
systemStatisticsCbfDiscards = _SystemStatisticsCbfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 93),
    _SystemStatisticsCbfDiscards_Type()
)
systemStatisticsCbfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsCbfDiscards.setStatus("current")
_SystemStatisticsFilterDrops_Type = Counter64
_SystemStatisticsFilterDrops_Object = MibScalar
systemStatisticsFilterDrops = _SystemStatisticsFilterDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 94),
    _SystemStatisticsFilterDrops_Type()
)
systemStatisticsFilterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsFilterDrops.setStatus("current")
_SystemStatisticsInvalidBackPtr_Type = Counter64
_SystemStatisticsInvalidBackPtr_Object = MibScalar
systemStatisticsInvalidBackPtr = _SystemStatisticsInvalidBackPtr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 95),
    _SystemStatisticsInvalidBackPtr_Type()
)
systemStatisticsInvalidBackPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsInvalidBackPtr.setStatus("current")
_SystemStatisticsTunnelLoopDrops_Type = Counter64
_SystemStatisticsTunnelLoopDrops_Object = MibScalar
systemStatisticsTunnelLoopDrops = _SystemStatisticsTunnelLoopDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 96),
    _SystemStatisticsTunnelLoopDrops_Type()
)
systemStatisticsTunnelLoopDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTunnelLoopDrops.setStatus("current")
_SystemStatisticsToCpuPolicerDrops_Type = Counter64
_SystemStatisticsToCpuPolicerDrops_Object = MibScalar
systemStatisticsToCpuPolicerDrops = _SystemStatisticsToCpuPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 97),
    _SystemStatisticsToCpuPolicerDrops_Type()
)
systemStatisticsToCpuPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsToCpuPolicerDrops.setStatus("current")
_SystemStatisticsMirrorDrops_Type = Counter64
_SystemStatisticsMirrorDrops_Object = MibScalar
systemStatisticsMirrorDrops = _SystemStatisticsMirrorDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 98),
    _SystemStatisticsMirrorDrops_Type()
)
systemStatisticsMirrorDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsMirrorDrops.setStatus("current")
_SystemStatisticsSplitHorizonDrops_Type = Counter64
_SystemStatisticsSplitHorizonDrops_Object = MibScalar
systemStatisticsSplitHorizonDrops = _SystemStatisticsSplitHorizonDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 99),
    _SystemStatisticsSplitHorizonDrops_Type()
)
systemStatisticsSplitHorizonDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsSplitHorizonDrops.setStatus("current")
_SystemStatisticsRxNoTunIf_Type = Counter64
_SystemStatisticsRxNoTunIf_Object = MibScalar
systemStatisticsRxNoTunIf = _SystemStatisticsRxNoTunIf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 100),
    _SystemStatisticsRxNoTunIf_Type()
)
systemStatisticsRxNoTunIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxNoTunIf.setStatus("current")
_SystemStatisticsTxPkts_Type = Counter64
_SystemStatisticsTxPkts_Object = MibScalar
systemStatisticsTxPkts = _SystemStatisticsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 101),
    _SystemStatisticsTxPkts_Type()
)
systemStatisticsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxPkts.setStatus("current")
_SystemStatisticsTxErrors_Type = Counter64
_SystemStatisticsTxErrors_Object = MibScalar
systemStatisticsTxErrors = _SystemStatisticsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 102),
    _SystemStatisticsTxErrors_Type()
)
systemStatisticsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxErrors.setStatus("current")
_SystemStatisticsTxBcast_Type = Counter64
_SystemStatisticsTxBcast_Object = MibScalar
systemStatisticsTxBcast = _SystemStatisticsTxBcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 103),
    _SystemStatisticsTxBcast_Type()
)
systemStatisticsTxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxBcast.setStatus("current")
_SystemStatisticsTxMcast_Type = Counter64
_SystemStatisticsTxMcast_Object = MibScalar
systemStatisticsTxMcast = _SystemStatisticsTxMcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 104),
    _SystemStatisticsTxMcast_Type()
)
systemStatisticsTxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxMcast.setStatus("current")
_SystemStatisticsPortDisabledTx_Type = Counter64
_SystemStatisticsPortDisabledTx_Object = MibScalar
systemStatisticsPortDisabledTx = _SystemStatisticsPortDisabledTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 105),
    _SystemStatisticsPortDisabledTx_Type()
)
systemStatisticsPortDisabledTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsPortDisabledTx.setStatus("current")
_SystemStatisticsIpDisabledTx_Type = Counter64
_SystemStatisticsIpDisabledTx_Object = MibScalar
systemStatisticsIpDisabledTx = _SystemStatisticsIpDisabledTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 106),
    _SystemStatisticsIpDisabledTx_Type()
)
systemStatisticsIpDisabledTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpDisabledTx.setStatus("current")
_SystemStatisticsTxFragmentNeeded_Type = Counter64
_SystemStatisticsTxFragmentNeeded_Object = MibScalar
systemStatisticsTxFragmentNeeded = _SystemStatisticsTxFragmentNeeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 107),
    _SystemStatisticsTxFragmentNeeded_Type()
)
systemStatisticsTxFragmentNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxFragmentNeeded.setStatus("current")
_SystemStatisticsTxMcastFragmentNeeded_Type = Counter64
_SystemStatisticsTxMcastFragmentNeeded_Object = MibScalar
systemStatisticsTxMcastFragmentNeeded = _SystemStatisticsTxMcastFragmentNeeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 108),
    _SystemStatisticsTxMcastFragmentNeeded_Type()
)
systemStatisticsTxMcastFragmentNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxMcastFragmentNeeded.setStatus("current")
_SystemStatisticsFragmentDfDrops_Type = Counter64
_SystemStatisticsFragmentDfDrops_Object = MibScalar
systemStatisticsFragmentDfDrops = _SystemStatisticsFragmentDfDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 109),
    _SystemStatisticsFragmentDfDrops_Type()
)
systemStatisticsFragmentDfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsFragmentDfDrops.setStatus("current")
_SystemStatisticsTxFragments_Type = Counter64
_SystemStatisticsTxFragments_Object = MibScalar
systemStatisticsTxFragments = _SystemStatisticsTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 110),
    _SystemStatisticsTxFragments_Type()
)
systemStatisticsTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxFragments.setStatus("current")
_SystemStatisticsTxFragmentDrops_Type = Counter64
_SystemStatisticsTxFragmentDrops_Object = MibScalar
systemStatisticsTxFragmentDrops = _SystemStatisticsTxFragmentDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 111),
    _SystemStatisticsTxFragmentDrops_Type()
)
systemStatisticsTxFragmentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxFragmentDrops.setStatus("current")
_SystemStatisticsTxFragmentFail_Type = Counter64
_SystemStatisticsTxFragmentFail_Object = MibScalar
systemStatisticsTxFragmentFail = _SystemStatisticsTxFragmentFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 112),
    _SystemStatisticsTxFragmentFail_Type()
)
systemStatisticsTxFragmentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxFragmentFail.setStatus("current")
_SystemStatisticsTxFragmentAllocFail_Type = Counter64
_SystemStatisticsTxFragmentAllocFail_Object = MibScalar
systemStatisticsTxFragmentAllocFail = _SystemStatisticsTxFragmentAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 113),
    _SystemStatisticsTxFragmentAllocFail_Type()
)
systemStatisticsTxFragmentAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxFragmentAllocFail.setStatus("current")
_SystemStatisticsTunnelPmtuLowered_Type = Counter64
_SystemStatisticsTunnelPmtuLowered_Object = MibScalar
systemStatisticsTunnelPmtuLowered = _SystemStatisticsTunnelPmtuLowered_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 114),
    _SystemStatisticsTunnelPmtuLowered_Type()
)
systemStatisticsTunnelPmtuLowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTunnelPmtuLowered.setStatus("current")
_SystemStatisticsTxGrePkts_Type = Counter64
_SystemStatisticsTxGrePkts_Object = MibScalar
systemStatisticsTxGrePkts = _SystemStatisticsTxGrePkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 115),
    _SystemStatisticsTxGrePkts_Type()
)
systemStatisticsTxGrePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxGrePkts.setStatus("current")
_SystemStatisticsTxGreDrops_Type = Counter64
_SystemStatisticsTxGreDrops_Object = MibScalar
systemStatisticsTxGreDrops = _SystemStatisticsTxGreDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 116),
    _SystemStatisticsTxGreDrops_Type()
)
systemStatisticsTxGreDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxGreDrops.setStatus("current")
_SystemStatisticsTxGrePolicerDrops_Type = Counter64
_SystemStatisticsTxGrePolicerDrops_Object = MibScalar
systemStatisticsTxGrePolicerDrops = _SystemStatisticsTxGrePolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 117),
    _SystemStatisticsTxGrePolicerDrops_Type()
)
systemStatisticsTxGrePolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxGrePolicerDrops.setStatus("current")
_SystemStatisticsTxGreEncap_Type = Counter64
_SystemStatisticsTxGreEncap_Object = MibScalar
systemStatisticsTxGreEncap = _SystemStatisticsTxGreEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 118),
    _SystemStatisticsTxGreEncap_Type()
)
systemStatisticsTxGreEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxGreEncap.setStatus("current")
_SystemStatisticsTxIpsecPkts_Type = Counter64
_SystemStatisticsTxIpsecPkts_Object = MibScalar
systemStatisticsTxIpsecPkts = _SystemStatisticsTxIpsecPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 119),
    _SystemStatisticsTxIpsecPkts_Type()
)
systemStatisticsTxIpsecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIpsecPkts.setStatus("current")
_SystemStatisticsTxIpsecMcastPkts_Type = Counter64
_SystemStatisticsTxIpsecMcastPkts_Object = MibScalar
systemStatisticsTxIpsecMcastPkts = _SystemStatisticsTxIpsecMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 120),
    _SystemStatisticsTxIpsecMcastPkts_Type()
)
systemStatisticsTxIpsecMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIpsecMcastPkts.setStatus("current")
_SystemStatisticsTxIp6IpsecDrops_Type = Counter64
_SystemStatisticsTxIp6IpsecDrops_Object = MibScalar
systemStatisticsTxIp6IpsecDrops = _SystemStatisticsTxIp6IpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 121),
    _SystemStatisticsTxIp6IpsecDrops_Type()
)
systemStatisticsTxIp6IpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIp6IpsecDrops.setStatus("current")
_SystemStatisticsTxNoOutSaIpsecDrops_Type = Counter64
_SystemStatisticsTxNoOutSaIpsecDrops_Object = MibScalar
systemStatisticsTxNoOutSaIpsecDrops = _SystemStatisticsTxNoOutSaIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 122),
    _SystemStatisticsTxNoOutSaIpsecDrops_Type()
)
systemStatisticsTxNoOutSaIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxNoOutSaIpsecDrops.setStatus("current")
_SystemStatisticsTxNoTunnIpsecDrops_Type = Counter64
_SystemStatisticsTxNoTunnIpsecDrops_Object = MibScalar
systemStatisticsTxNoTunnIpsecDrops = _SystemStatisticsTxNoTunnIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 123),
    _SystemStatisticsTxNoTunnIpsecDrops_Type()
)
systemStatisticsTxNoTunnIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxNoTunnIpsecDrops.setStatus("current")
_SystemStatisticsTxIpsecPolicerDrops_Type = Counter64
_SystemStatisticsTxIpsecPolicerDrops_Object = MibScalar
systemStatisticsTxIpsecPolicerDrops = _SystemStatisticsTxIpsecPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 124),
    _SystemStatisticsTxIpsecPolicerDrops_Type()
)
systemStatisticsTxIpsecPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIpsecPolicerDrops.setStatus("current")
_SystemStatisticsTxIpsecEncap_Type = Counter64
_SystemStatisticsTxIpsecEncap_Object = MibScalar
systemStatisticsTxIpsecEncap = _SystemStatisticsTxIpsecEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 125),
    _SystemStatisticsTxIpsecEncap_Type()
)
systemStatisticsTxIpsecEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIpsecEncap.setStatus("current")
_SystemStatisticsTxIpsecMcastEncap_Type = Counter64
_SystemStatisticsTxIpsecMcastEncap_Object = MibScalar
systemStatisticsTxIpsecMcastEncap = _SystemStatisticsTxIpsecMcastEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 126),
    _SystemStatisticsTxIpsecMcastEncap_Type()
)
systemStatisticsTxIpsecMcastEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIpsecMcastEncap.setStatus("current")
_SystemStatisticsTxPreIpsecPkts_Type = Counter64
_SystemStatisticsTxPreIpsecPkts_Object = MibScalar
systemStatisticsTxPreIpsecPkts = _SystemStatisticsTxPreIpsecPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 127),
    _SystemStatisticsTxPreIpsecPkts_Type()
)
systemStatisticsTxPreIpsecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxPreIpsecPkts.setStatus("current")
_SystemStatisticsTxNoOutSaPreIpsecDrops_Type = Counter64
_SystemStatisticsTxNoOutSaPreIpsecDrops_Object = MibScalar
systemStatisticsTxNoOutSaPreIpsecDrops = _SystemStatisticsTxNoOutSaPreIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 128),
    _SystemStatisticsTxNoOutSaPreIpsecDrops_Type()
)
systemStatisticsTxNoOutSaPreIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxNoOutSaPreIpsecDrops.setStatus("current")
_SystemStatisticsTxNoTunnPreIpsecDrops_Type = Counter64
_SystemStatisticsTxNoTunnPreIpsecDrops_Object = MibScalar
systemStatisticsTxNoTunnPreIpsecDrops = _SystemStatisticsTxNoTunnPreIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 129),
    _SystemStatisticsTxNoTunnPreIpsecDrops_Type()
)
systemStatisticsTxNoTunnPreIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxNoTunnPreIpsecDrops.setStatus("current")
_SystemStatisticsOpensslAesEncrypt_Type = Counter64
_SystemStatisticsOpensslAesEncrypt_Object = MibScalar
systemStatisticsOpensslAesEncrypt = _SystemStatisticsOpensslAesEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 130),
    _SystemStatisticsOpensslAesEncrypt_Type()
)
systemStatisticsOpensslAesEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsOpensslAesEncrypt.setStatus("current")
_SystemStatisticsTxPreIpsecPolicerDrops_Type = Counter64
_SystemStatisticsTxPreIpsecPolicerDrops_Object = MibScalar
systemStatisticsTxPreIpsecPolicerDrops = _SystemStatisticsTxPreIpsecPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 131),
    _SystemStatisticsTxPreIpsecPolicerDrops_Type()
)
systemStatisticsTxPreIpsecPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxPreIpsecPolicerDrops.setStatus("current")
_SystemStatisticsTxPreIpsecEncap_Type = Counter64
_SystemStatisticsTxPreIpsecEncap_Object = MibScalar
systemStatisticsTxPreIpsecEncap = _SystemStatisticsTxPreIpsecEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 132),
    _SystemStatisticsTxPreIpsecEncap_Type()
)
systemStatisticsTxPreIpsecEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxPreIpsecEncap.setStatus("current")
_SystemStatisticsTxArpReplies_Type = Counter64
_SystemStatisticsTxArpReplies_Object = MibScalar
systemStatisticsTxArpReplies = _SystemStatisticsTxArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 133),
    _SystemStatisticsTxArpReplies_Type()
)
systemStatisticsTxArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxArpReplies.setStatus("current")
_SystemStatisticsTxArpReqs_Type = Counter64
_SystemStatisticsTxArpReqs_Object = MibScalar
systemStatisticsTxArpReqs = _SystemStatisticsTxArpReqs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 134),
    _SystemStatisticsTxArpReqs_Type()
)
systemStatisticsTxArpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxArpReqs.setStatus("current")
_SystemStatisticsTxArpReqFail_Type = Counter64
_SystemStatisticsTxArpReqFail_Object = MibScalar
systemStatisticsTxArpReqFail = _SystemStatisticsTxArpReqFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 135),
    _SystemStatisticsTxArpReqFail_Type()
)
systemStatisticsTxArpReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxArpReqFail.setStatus("current")
_SystemStatisticsTxNoArpDrop_Type = Counter64
_SystemStatisticsTxNoArpDrop_Object = MibScalar
systemStatisticsTxNoArpDrop = _SystemStatisticsTxNoArpDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 136),
    _SystemStatisticsTxNoArpDrop_Type()
)
systemStatisticsTxNoArpDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxNoArpDrop.setStatus("current")
_SystemStatisticsTxArpRateLimitDrops_Type = Counter64
_SystemStatisticsTxArpRateLimitDrops_Object = MibScalar
systemStatisticsTxArpRateLimitDrops = _SystemStatisticsTxArpRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 137),
    _SystemStatisticsTxArpRateLimitDrops_Type()
)
systemStatisticsTxArpRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxArpRateLimitDrops.setStatus("current")
_SystemStatisticsTxIcmpPolicerDrops_Type = Counter64
_SystemStatisticsTxIcmpPolicerDrops_Object = MibScalar
systemStatisticsTxIcmpPolicerDrops = _SystemStatisticsTxIcmpPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 138),
    _SystemStatisticsTxIcmpPolicerDrops_Type()
)
systemStatisticsTxIcmpPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpPolicerDrops.setStatus("current")
_SystemStatisticsTxIcmpMirroredDrops_Type = Counter64
_SystemStatisticsTxIcmpMirroredDrops_Object = MibScalar
systemStatisticsTxIcmpMirroredDrops = _SystemStatisticsTxIcmpMirroredDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 139),
    _SystemStatisticsTxIcmpMirroredDrops_Type()
)
systemStatisticsTxIcmpMirroredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpMirroredDrops.setStatus("current")
_SystemStatisticsBfdTxFail_Type = Counter64
_SystemStatisticsBfdTxFail_Object = MibScalar
systemStatisticsBfdTxFail = _SystemStatisticsBfdTxFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 140),
    _SystemStatisticsBfdTxFail_Type()
)
systemStatisticsBfdTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdTxFail.setStatus("current")
_SystemStatisticsBfdAllocFail_Type = Counter64
_SystemStatisticsBfdAllocFail_Object = MibScalar
systemStatisticsBfdAllocFail = _SystemStatisticsBfdAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 141),
    _SystemStatisticsBfdAllocFail_Type()
)
systemStatisticsBfdAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdAllocFail.setStatus("current")
_SystemStatisticsBfdTimerAddFail_Type = Counter64
_SystemStatisticsBfdTimerAddFail_Object = MibScalar
systemStatisticsBfdTimerAddFail = _SystemStatisticsBfdTimerAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 142),
    _SystemStatisticsBfdTimerAddFail_Type()
)
systemStatisticsBfdTimerAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdTimerAddFail.setStatus("current")
_SystemStatisticsBfdTxPkts_Type = Counter64
_SystemStatisticsBfdTxPkts_Object = MibScalar
systemStatisticsBfdTxPkts = _SystemStatisticsBfdTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 143),
    _SystemStatisticsBfdTxPkts_Type()
)
systemStatisticsBfdTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdTxPkts.setStatus("current")
_SystemStatisticsBfdRxPkts_Type = Counter64
_SystemStatisticsBfdRxPkts_Object = MibScalar
systemStatisticsBfdRxPkts = _SystemStatisticsBfdRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 144),
    _SystemStatisticsBfdRxPkts_Type()
)
systemStatisticsBfdRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdRxPkts.setStatus("current")
_SystemStatisticsBfdRecDown_Type = Counter64
_SystemStatisticsBfdRecDown_Object = MibScalar
systemStatisticsBfdRecDown = _SystemStatisticsBfdRecDown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 145),
    _SystemStatisticsBfdRecDown_Type()
)
systemStatisticsBfdRecDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdRecDown.setStatus("current")
_SystemStatisticsBfdRecInvalid_Type = Counter64
_SystemStatisticsBfdRecInvalid_Object = MibScalar
systemStatisticsBfdRecInvalid = _SystemStatisticsBfdRecInvalid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 146),
    _SystemStatisticsBfdRecInvalid_Type()
)
systemStatisticsBfdRecInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdRecInvalid.setStatus("current")
_SystemStatisticsBfdLkupFail_Type = Counter64
_SystemStatisticsBfdLkupFail_Object = MibScalar
systemStatisticsBfdLkupFail = _SystemStatisticsBfdLkupFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 147),
    _SystemStatisticsBfdLkupFail_Type()
)
systemStatisticsBfdLkupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdLkupFail.setStatus("current")
_SystemStatisticsRxIcmpEchoRequests_Type = Counter64
_SystemStatisticsRxIcmpEchoRequests_Object = MibScalar
systemStatisticsRxIcmpEchoRequests = _SystemStatisticsRxIcmpEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 148),
    _SystemStatisticsRxIcmpEchoRequests_Type()
)
systemStatisticsRxIcmpEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpEchoRequests.setStatus("current")
_SystemStatisticsRxIcmpEchoReplies_Type = Counter64
_SystemStatisticsRxIcmpEchoReplies_Object = MibScalar
systemStatisticsRxIcmpEchoReplies = _SystemStatisticsRxIcmpEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 149),
    _SystemStatisticsRxIcmpEchoReplies_Type()
)
systemStatisticsRxIcmpEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpEchoReplies.setStatus("current")
_SystemStatisticsRxIcmpNetworkUnreach_Type = Counter64
_SystemStatisticsRxIcmpNetworkUnreach_Object = MibScalar
systemStatisticsRxIcmpNetworkUnreach = _SystemStatisticsRxIcmpNetworkUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 150),
    _SystemStatisticsRxIcmpNetworkUnreach_Type()
)
systemStatisticsRxIcmpNetworkUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpNetworkUnreach.setStatus("current")
_SystemStatisticsRxIcmpHostUnreach_Type = Counter64
_SystemStatisticsRxIcmpHostUnreach_Object = MibScalar
systemStatisticsRxIcmpHostUnreach = _SystemStatisticsRxIcmpHostUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 151),
    _SystemStatisticsRxIcmpHostUnreach_Type()
)
systemStatisticsRxIcmpHostUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpHostUnreach.setStatus("current")
_SystemStatisticsRxIcmpPortUnreach_Type = Counter64
_SystemStatisticsRxIcmpPortUnreach_Object = MibScalar
systemStatisticsRxIcmpPortUnreach = _SystemStatisticsRxIcmpPortUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 152),
    _SystemStatisticsRxIcmpPortUnreach_Type()
)
systemStatisticsRxIcmpPortUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpPortUnreach.setStatus("current")
_SystemStatisticsRxIcmpProtocolUnreach_Type = Counter64
_SystemStatisticsRxIcmpProtocolUnreach_Object = MibScalar
systemStatisticsRxIcmpProtocolUnreach = _SystemStatisticsRxIcmpProtocolUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 153),
    _SystemStatisticsRxIcmpProtocolUnreach_Type()
)
systemStatisticsRxIcmpProtocolUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpProtocolUnreach.setStatus("current")
_SystemStatisticsRxIcmpFragmentRequired_Type = Counter64
_SystemStatisticsRxIcmpFragmentRequired_Object = MibScalar
systemStatisticsRxIcmpFragmentRequired = _SystemStatisticsRxIcmpFragmentRequired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 154),
    _SystemStatisticsRxIcmpFragmentRequired_Type()
)
systemStatisticsRxIcmpFragmentRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpFragmentRequired.setStatus("current")
_SystemStatisticsRxIcmpDstUnreachOther_Type = Counter64
_SystemStatisticsRxIcmpDstUnreachOther_Object = MibScalar
systemStatisticsRxIcmpDstUnreachOther = _SystemStatisticsRxIcmpDstUnreachOther_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 155),
    _SystemStatisticsRxIcmpDstUnreachOther_Type()
)
systemStatisticsRxIcmpDstUnreachOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpDstUnreachOther.setStatus("current")
_SystemStatisticsRxIcmpTtlExpired_Type = Counter64
_SystemStatisticsRxIcmpTtlExpired_Object = MibScalar
systemStatisticsRxIcmpTtlExpired = _SystemStatisticsRxIcmpTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 156),
    _SystemStatisticsRxIcmpTtlExpired_Type()
)
systemStatisticsRxIcmpTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpTtlExpired.setStatus("current")
_SystemStatisticsRxIcmpRedirect_Type = Counter64
_SystemStatisticsRxIcmpRedirect_Object = MibScalar
systemStatisticsRxIcmpRedirect = _SystemStatisticsRxIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 157),
    _SystemStatisticsRxIcmpRedirect_Type()
)
systemStatisticsRxIcmpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpRedirect.setStatus("current")
_SystemStatisticsRxIcmpSrcQuench_Type = Counter64
_SystemStatisticsRxIcmpSrcQuench_Object = MibScalar
systemStatisticsRxIcmpSrcQuench = _SystemStatisticsRxIcmpSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 158),
    _SystemStatisticsRxIcmpSrcQuench_Type()
)
systemStatisticsRxIcmpSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpSrcQuench.setStatus("current")
_SystemStatisticsRxIcmpBadIpHdr_Type = Counter64
_SystemStatisticsRxIcmpBadIpHdr_Object = MibScalar
systemStatisticsRxIcmpBadIpHdr = _SystemStatisticsRxIcmpBadIpHdr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 159),
    _SystemStatisticsRxIcmpBadIpHdr_Type()
)
systemStatisticsRxIcmpBadIpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpBadIpHdr.setStatus("current")
_SystemStatisticsRxIcmpOtherTypes_Type = Counter64
_SystemStatisticsRxIcmpOtherTypes_Object = MibScalar
systemStatisticsRxIcmpOtherTypes = _SystemStatisticsRxIcmpOtherTypes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 160),
    _SystemStatisticsRxIcmpOtherTypes_Type()
)
systemStatisticsRxIcmpOtherTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxIcmpOtherTypes.setStatus("current")
_SystemStatisticsTxIcmpEchoRequests_Type = Counter64
_SystemStatisticsTxIcmpEchoRequests_Object = MibScalar
systemStatisticsTxIcmpEchoRequests = _SystemStatisticsTxIcmpEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 161),
    _SystemStatisticsTxIcmpEchoRequests_Type()
)
systemStatisticsTxIcmpEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpEchoRequests.setStatus("current")
_SystemStatisticsTxIcmpEchoReplies_Type = Counter64
_SystemStatisticsTxIcmpEchoReplies_Object = MibScalar
systemStatisticsTxIcmpEchoReplies = _SystemStatisticsTxIcmpEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 162),
    _SystemStatisticsTxIcmpEchoReplies_Type()
)
systemStatisticsTxIcmpEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpEchoReplies.setStatus("current")
_SystemStatisticsTxIcmpNetworkUnreach_Type = Counter64
_SystemStatisticsTxIcmpNetworkUnreach_Object = MibScalar
systemStatisticsTxIcmpNetworkUnreach = _SystemStatisticsTxIcmpNetworkUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 163),
    _SystemStatisticsTxIcmpNetworkUnreach_Type()
)
systemStatisticsTxIcmpNetworkUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpNetworkUnreach.setStatus("current")
_SystemStatisticsTxIcmpHostUnreach_Type = Counter64
_SystemStatisticsTxIcmpHostUnreach_Object = MibScalar
systemStatisticsTxIcmpHostUnreach = _SystemStatisticsTxIcmpHostUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 164),
    _SystemStatisticsTxIcmpHostUnreach_Type()
)
systemStatisticsTxIcmpHostUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpHostUnreach.setStatus("current")
_SystemStatisticsTxIcmpPortUnreach_Type = Counter64
_SystemStatisticsTxIcmpPortUnreach_Object = MibScalar
systemStatisticsTxIcmpPortUnreach = _SystemStatisticsTxIcmpPortUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 165),
    _SystemStatisticsTxIcmpPortUnreach_Type()
)
systemStatisticsTxIcmpPortUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpPortUnreach.setStatus("current")
_SystemStatisticsTxIcmpProtocolUnreach_Type = Counter64
_SystemStatisticsTxIcmpProtocolUnreach_Object = MibScalar
systemStatisticsTxIcmpProtocolUnreach = _SystemStatisticsTxIcmpProtocolUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 166),
    _SystemStatisticsTxIcmpProtocolUnreach_Type()
)
systemStatisticsTxIcmpProtocolUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpProtocolUnreach.setStatus("current")
_SystemStatisticsTxIcmpFragmentRequired_Type = Counter64
_SystemStatisticsTxIcmpFragmentRequired_Object = MibScalar
systemStatisticsTxIcmpFragmentRequired = _SystemStatisticsTxIcmpFragmentRequired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 167),
    _SystemStatisticsTxIcmpFragmentRequired_Type()
)
systemStatisticsTxIcmpFragmentRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpFragmentRequired.setStatus("current")
_SystemStatisticsTxIcmpDstUnreachOther_Type = Counter64
_SystemStatisticsTxIcmpDstUnreachOther_Object = MibScalar
systemStatisticsTxIcmpDstUnreachOther = _SystemStatisticsTxIcmpDstUnreachOther_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 168),
    _SystemStatisticsTxIcmpDstUnreachOther_Type()
)
systemStatisticsTxIcmpDstUnreachOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpDstUnreachOther.setStatus("current")
_SystemStatisticsTxIcmpTtlExpired_Type = Counter64
_SystemStatisticsTxIcmpTtlExpired_Object = MibScalar
systemStatisticsTxIcmpTtlExpired = _SystemStatisticsTxIcmpTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 169),
    _SystemStatisticsTxIcmpTtlExpired_Type()
)
systemStatisticsTxIcmpTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpTtlExpired.setStatus("current")
_SystemStatisticsTxIcmpRedirect_Type = Counter64
_SystemStatisticsTxIcmpRedirect_Object = MibScalar
systemStatisticsTxIcmpRedirect = _SystemStatisticsTxIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 170),
    _SystemStatisticsTxIcmpRedirect_Type()
)
systemStatisticsTxIcmpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpRedirect.setStatus("current")
_SystemStatisticsTxIcmpSrcQuench_Type = Counter64
_SystemStatisticsTxIcmpSrcQuench_Object = MibScalar
systemStatisticsTxIcmpSrcQuench = _SystemStatisticsTxIcmpSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 171),
    _SystemStatisticsTxIcmpSrcQuench_Type()
)
systemStatisticsTxIcmpSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpSrcQuench.setStatus("current")
_SystemStatisticsTxIcmpBadIpHdr_Type = Counter64
_SystemStatisticsTxIcmpBadIpHdr_Object = MibScalar
systemStatisticsTxIcmpBadIpHdr = _SystemStatisticsTxIcmpBadIpHdr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 172),
    _SystemStatisticsTxIcmpBadIpHdr_Type()
)
systemStatisticsTxIcmpBadIpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpBadIpHdr.setStatus("current")
_SystemStatisticsTxIcmpOtherTypes_Type = Counter64
_SystemStatisticsTxIcmpOtherTypes_Object = MibScalar
systemStatisticsTxIcmpOtherTypes = _SystemStatisticsTxIcmpOtherTypes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 173),
    _SystemStatisticsTxIcmpOtherTypes_Type()
)
systemStatisticsTxIcmpOtherTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxIcmpOtherTypes.setStatus("current")
_SystemStatisticsGreKaTxPkts_Type = Counter64
_SystemStatisticsGreKaTxPkts_Object = MibScalar
systemStatisticsGreKaTxPkts = _SystemStatisticsGreKaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 174),
    _SystemStatisticsGreKaTxPkts_Type()
)
systemStatisticsGreKaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaTxPkts.setStatus("current")
_SystemStatisticsGreKaRxPkts_Type = Counter64
_SystemStatisticsGreKaRxPkts_Object = MibScalar
systemStatisticsGreKaRxPkts = _SystemStatisticsGreKaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 175),
    _SystemStatisticsGreKaRxPkts_Type()
)
systemStatisticsGreKaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaRxPkts.setStatus("current")
_SystemStatisticsGreKaTxIpv4OptionsDrop_Type = Counter64
_SystemStatisticsGreKaTxIpv4OptionsDrop_Object = MibScalar
systemStatisticsGreKaTxIpv4OptionsDrop = _SystemStatisticsGreKaTxIpv4OptionsDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 176),
    _SystemStatisticsGreKaTxIpv4OptionsDrop_Type()
)
systemStatisticsGreKaTxIpv4OptionsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaTxIpv4OptionsDrop.setStatus("current")
_SystemStatisticsGreKaTxNonIp_Type = Counter64
_SystemStatisticsGreKaTxNonIp_Object = MibScalar
systemStatisticsGreKaTxNonIp = _SystemStatisticsGreKaTxNonIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 177),
    _SystemStatisticsGreKaTxNonIp_Type()
)
systemStatisticsGreKaTxNonIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaTxNonIp.setStatus("current")
_SystemStatisticsGreKaTxParseErr_Type = Counter64
_SystemStatisticsGreKaTxParseErr_Object = MibScalar
systemStatisticsGreKaTxParseErr = _SystemStatisticsGreKaTxParseErr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 178),
    _SystemStatisticsGreKaTxParseErr_Type()
)
systemStatisticsGreKaTxParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaTxParseErr.setStatus("current")
_SystemStatisticsGreKaTxRecordChanged_Type = Counter64
_SystemStatisticsGreKaTxRecordChanged_Object = MibScalar
systemStatisticsGreKaTxRecordChanged = _SystemStatisticsGreKaTxRecordChanged_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 179),
    _SystemStatisticsGreKaTxRecordChanged_Type()
)
systemStatisticsGreKaTxRecordChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaTxRecordChanged.setStatus("current")
_SystemStatisticsGreKaTxFail_Type = Counter64
_SystemStatisticsGreKaTxFail_Object = MibScalar
systemStatisticsGreKaTxFail = _SystemStatisticsGreKaTxFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 180),
    _SystemStatisticsGreKaTxFail_Type()
)
systemStatisticsGreKaTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaTxFail.setStatus("current")
_SystemStatisticsGreKaAllocFail_Type = Counter64
_SystemStatisticsGreKaAllocFail_Object = MibScalar
systemStatisticsGreKaAllocFail = _SystemStatisticsGreKaAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 181),
    _SystemStatisticsGreKaAllocFail_Type()
)
systemStatisticsGreKaAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaAllocFail.setStatus("current")
_SystemStatisticsGreKaTimerAddFail_Type = Counter64
_SystemStatisticsGreKaTimerAddFail_Object = MibScalar
systemStatisticsGreKaTimerAddFail = _SystemStatisticsGreKaTimerAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 182),
    _SystemStatisticsGreKaTimerAddFail_Type()
)
systemStatisticsGreKaTimerAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaTimerAddFail.setStatus("current")
_SystemStatisticsGreKaRxNonIp_Type = Counter64
_SystemStatisticsGreKaRxNonIp_Object = MibScalar
systemStatisticsGreKaRxNonIp = _SystemStatisticsGreKaRxNonIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 183),
    _SystemStatisticsGreKaRxNonIp_Type()
)
systemStatisticsGreKaRxNonIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaRxNonIp.setStatus("current")
_SystemStatisticsGreKaRxRecInvalid_Type = Counter64
_SystemStatisticsGreKaRxRecInvalid_Object = MibScalar
systemStatisticsGreKaRxRecInvalid = _SystemStatisticsGreKaRxRecInvalid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 184),
    _SystemStatisticsGreKaRxRecInvalid_Type()
)
systemStatisticsGreKaRxRecInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsGreKaRxRecInvalid.setStatus("current")
_SystemStatisticsDot1xRxPkts_Type = Counter64
_SystemStatisticsDot1xRxPkts_Object = MibScalar
systemStatisticsDot1xRxPkts = _SystemStatisticsDot1xRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 185),
    _SystemStatisticsDot1xRxPkts_Type()
)
systemStatisticsDot1xRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDot1xRxPkts.setStatus("current")
_SystemStatisticsDot1xTxPkts_Type = Counter64
_SystemStatisticsDot1xTxPkts_Object = MibScalar
systemStatisticsDot1xTxPkts = _SystemStatisticsDot1xTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 186),
    _SystemStatisticsDot1xTxPkts_Type()
)
systemStatisticsDot1xTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDot1xTxPkts.setStatus("current")
_SystemStatisticsDot1xRxDrops_Type = Counter64
_SystemStatisticsDot1xRxDrops_Object = MibScalar
systemStatisticsDot1xRxDrops = _SystemStatisticsDot1xRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 187),
    _SystemStatisticsDot1xRxDrops_Type()
)
systemStatisticsDot1xRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDot1xRxDrops.setStatus("current")
_SystemStatisticsDot1xTxDrops_Type = Counter64
_SystemStatisticsDot1xTxDrops_Object = MibScalar
systemStatisticsDot1xTxDrops = _SystemStatisticsDot1xTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 188),
    _SystemStatisticsDot1xTxDrops_Type()
)
systemStatisticsDot1xTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDot1xTxDrops.setStatus("current")
_SystemStatisticsDot1xVlanIfNotFoundDrops_Type = Counter64
_SystemStatisticsDot1xVlanIfNotFoundDrops_Object = MibScalar
systemStatisticsDot1xVlanIfNotFoundDrops = _SystemStatisticsDot1xVlanIfNotFoundDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 189),
    _SystemStatisticsDot1xVlanIfNotFoundDrops_Type()
)
systemStatisticsDot1xVlanIfNotFoundDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDot1xVlanIfNotFoundDrops.setStatus("current")
_SystemStatisticsDot1xMacLearnDrops_Type = Counter64
_SystemStatisticsDot1xMacLearnDrops_Object = MibScalar
systemStatisticsDot1xMacLearnDrops = _SystemStatisticsDot1xMacLearnDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 190),
    _SystemStatisticsDot1xMacLearnDrops_Type()
)
systemStatisticsDot1xMacLearnDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDot1xMacLearnDrops.setStatus("current")
_SystemStatisticsRxPolicerRemark_Type = Counter64
_SystemStatisticsRxPolicerRemark_Object = MibScalar
systemStatisticsRxPolicerRemark = _SystemStatisticsRxPolicerRemark_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 191),
    _SystemStatisticsRxPolicerRemark_Type()
)
systemStatisticsRxPolicerRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxPolicerRemark.setStatus("current")
_SystemStatisticsBfdTxOctets_Type = Counter64
_SystemStatisticsBfdTxOctets_Object = MibScalar
systemStatisticsBfdTxOctets = _SystemStatisticsBfdTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 192),
    _SystemStatisticsBfdTxOctets_Type()
)
systemStatisticsBfdTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdTxOctets.setStatus("current")
_SystemStatisticsBfdRxOctets_Type = Counter64
_SystemStatisticsBfdRxOctets_Object = MibScalar
systemStatisticsBfdRxOctets = _SystemStatisticsBfdRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 193),
    _SystemStatisticsBfdRxOctets_Type()
)
systemStatisticsBfdRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdRxOctets.setStatus("current")
_SystemStatisticsBfdPmtuTxPkts_Type = Counter64
_SystemStatisticsBfdPmtuTxPkts_Object = MibScalar
systemStatisticsBfdPmtuTxPkts = _SystemStatisticsBfdPmtuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 194),
    _SystemStatisticsBfdPmtuTxPkts_Type()
)
systemStatisticsBfdPmtuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdPmtuTxPkts.setStatus("current")
_SystemStatisticsBfdPmtuRxPkts_Type = Counter64
_SystemStatisticsBfdPmtuRxPkts_Object = MibScalar
systemStatisticsBfdPmtuRxPkts = _SystemStatisticsBfdPmtuRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 195),
    _SystemStatisticsBfdPmtuRxPkts_Type()
)
systemStatisticsBfdPmtuRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdPmtuRxPkts.setStatus("current")
_SystemStatisticsBfdPmtuTxOctets_Type = Counter64
_SystemStatisticsBfdPmtuTxOctets_Object = MibScalar
systemStatisticsBfdPmtuTxOctets = _SystemStatisticsBfdPmtuTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 196),
    _SystemStatisticsBfdPmtuTxOctets_Type()
)
systemStatisticsBfdPmtuTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdPmtuTxOctets.setStatus("current")
_SystemStatisticsBfdPmtuRxOctets_Type = Counter64
_SystemStatisticsBfdPmtuRxOctets_Object = MibScalar
systemStatisticsBfdPmtuRxOctets = _SystemStatisticsBfdPmtuRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 197),
    _SystemStatisticsBfdPmtuRxOctets_Type()
)
systemStatisticsBfdPmtuRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsBfdPmtuRxOctets.setStatus("current")
_SystemStatisticsDnsReqSnoop_Type = Counter64
_SystemStatisticsDnsReqSnoop_Object = MibScalar
systemStatisticsDnsReqSnoop = _SystemStatisticsDnsReqSnoop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 198),
    _SystemStatisticsDnsReqSnoop_Type()
)
systemStatisticsDnsReqSnoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDnsReqSnoop.setStatus("current")
_SystemStatisticsDnsResSnoop_Type = Counter64
_SystemStatisticsDnsResSnoop_Object = MibScalar
systemStatisticsDnsResSnoop = _SystemStatisticsDnsResSnoop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 199),
    _SystemStatisticsDnsResSnoop_Type()
)
systemStatisticsDnsResSnoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDnsResSnoop.setStatus("current")
_SystemStatisticsCtrlLoopFwd_Type = Counter64
_SystemStatisticsCtrlLoopFwd_Object = MibScalar
systemStatisticsCtrlLoopFwd = _SystemStatisticsCtrlLoopFwd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 200),
    _SystemStatisticsCtrlLoopFwd_Type()
)
systemStatisticsCtrlLoopFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsCtrlLoopFwd.setStatus("current")
_SystemStatisticsCtrlLoopFwdDrops_Type = Counter64
_SystemStatisticsCtrlLoopFwdDrops_Object = MibScalar
systemStatisticsCtrlLoopFwdDrops = _SystemStatisticsCtrlLoopFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 201),
    _SystemStatisticsCtrlLoopFwdDrops_Type()
)
systemStatisticsCtrlLoopFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsCtrlLoopFwdDrops.setStatus("current")
_SystemStatisticsRedirectDnsReq_Type = Counter64
_SystemStatisticsRedirectDnsReq_Object = MibScalar
systemStatisticsRedirectDnsReq = _SystemStatisticsRedirectDnsReq_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 202),
    _SystemStatisticsRedirectDnsReq_Type()
)
systemStatisticsRedirectDnsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRedirectDnsReq.setStatus("current")
_SystemStatisticsQatAesDecrypt_Type = Counter64
_SystemStatisticsQatAesDecrypt_Object = MibScalar
systemStatisticsQatAesDecrypt = _SystemStatisticsQatAesDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 204),
    _SystemStatisticsQatAesDecrypt_Type()
)
systemStatisticsQatAesDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsQatAesDecrypt.setStatus("current")
_SystemStatisticsQatAesEncrypt_Type = Counter64
_SystemStatisticsQatAesEncrypt_Object = MibScalar
systemStatisticsQatAesEncrypt = _SystemStatisticsQatAesEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 205),
    _SystemStatisticsQatAesEncrypt_Type()
)
systemStatisticsQatAesEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsQatAesEncrypt.setStatus("current")
_SystemStatisticsQatGcmDecrypt_Type = Counter64
_SystemStatisticsQatGcmDecrypt_Object = MibScalar
systemStatisticsQatGcmDecrypt = _SystemStatisticsQatGcmDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 206),
    _SystemStatisticsQatGcmDecrypt_Type()
)
systemStatisticsQatGcmDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsQatGcmDecrypt.setStatus("current")
_SystemStatisticsQatGcmEncrypt_Type = Counter64
_SystemStatisticsQatGcmEncrypt_Object = MibScalar
systemStatisticsQatGcmEncrypt = _SystemStatisticsQatGcmEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 207),
    _SystemStatisticsQatGcmEncrypt_Type()
)
systemStatisticsQatGcmEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsQatGcmEncrypt.setStatus("current")
_SystemStatisticsOpensslGcmDecrypt_Type = Counter64
_SystemStatisticsOpensslGcmDecrypt_Object = MibScalar
systemStatisticsOpensslGcmDecrypt = _SystemStatisticsOpensslGcmDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 208),
    _SystemStatisticsOpensslGcmDecrypt_Type()
)
systemStatisticsOpensslGcmDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsOpensslGcmDecrypt.setStatus("current")
_SystemStatisticsOpensslGcmEncrypt_Type = Counter64
_SystemStatisticsOpensslGcmEncrypt_Object = MibScalar
systemStatisticsOpensslGcmEncrypt = _SystemStatisticsOpensslGcmEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 209),
    _SystemStatisticsOpensslGcmEncrypt_Type()
)
systemStatisticsOpensslGcmEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsOpensslGcmEncrypt.setStatus("current")
_SystemStatisticsRxReplayDropsTc0_Type = Counter64
_SystemStatisticsRxReplayDropsTc0_Object = MibScalar
systemStatisticsRxReplayDropsTc0 = _SystemStatisticsRxReplayDropsTc0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 210),
    _SystemStatisticsRxReplayDropsTc0_Type()
)
systemStatisticsRxReplayDropsTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDropsTc0.setStatus("current")
_SystemStatisticsRxReplayDropsTc1_Type = Counter64
_SystemStatisticsRxReplayDropsTc1_Object = MibScalar
systemStatisticsRxReplayDropsTc1 = _SystemStatisticsRxReplayDropsTc1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 211),
    _SystemStatisticsRxReplayDropsTc1_Type()
)
systemStatisticsRxReplayDropsTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDropsTc1.setStatus("current")
_SystemStatisticsRxReplayDropsTc2_Type = Counter64
_SystemStatisticsRxReplayDropsTc2_Object = MibScalar
systemStatisticsRxReplayDropsTc2 = _SystemStatisticsRxReplayDropsTc2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 212),
    _SystemStatisticsRxReplayDropsTc2_Type()
)
systemStatisticsRxReplayDropsTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDropsTc2.setStatus("current")
_SystemStatisticsRxReplayDropsTc3_Type = Counter64
_SystemStatisticsRxReplayDropsTc3_Object = MibScalar
systemStatisticsRxReplayDropsTc3 = _SystemStatisticsRxReplayDropsTc3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 213),
    _SystemStatisticsRxReplayDropsTc3_Type()
)
systemStatisticsRxReplayDropsTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDropsTc3.setStatus("current")
_SystemStatisticsRxReplayDropsTc4_Type = Counter64
_SystemStatisticsRxReplayDropsTc4_Object = MibScalar
systemStatisticsRxReplayDropsTc4 = _SystemStatisticsRxReplayDropsTc4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 214),
    _SystemStatisticsRxReplayDropsTc4_Type()
)
systemStatisticsRxReplayDropsTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDropsTc4.setStatus("current")
_SystemStatisticsRxReplayDropsTc5_Type = Counter64
_SystemStatisticsRxReplayDropsTc5_Object = MibScalar
systemStatisticsRxReplayDropsTc5 = _SystemStatisticsRxReplayDropsTc5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 215),
    _SystemStatisticsRxReplayDropsTc5_Type()
)
systemStatisticsRxReplayDropsTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDropsTc5.setStatus("current")
_SystemStatisticsRxReplayDropsTc6_Type = Counter64
_SystemStatisticsRxReplayDropsTc6_Object = MibScalar
systemStatisticsRxReplayDropsTc6 = _SystemStatisticsRxReplayDropsTc6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 216),
    _SystemStatisticsRxReplayDropsTc6_Type()
)
systemStatisticsRxReplayDropsTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDropsTc6.setStatus("current")
_SystemStatisticsRxReplayDropsTc7_Type = Counter64
_SystemStatisticsRxReplayDropsTc7_Object = MibScalar
systemStatisticsRxReplayDropsTc7 = _SystemStatisticsRxReplayDropsTc7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 217),
    _SystemStatisticsRxReplayDropsTc7_Type()
)
systemStatisticsRxReplayDropsTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayDropsTc7.setStatus("current")
_SystemStatisticsRxWindowDropsTc0_Type = Counter64
_SystemStatisticsRxWindowDropsTc0_Object = MibScalar
systemStatisticsRxWindowDropsTc0 = _SystemStatisticsRxWindowDropsTc0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 218),
    _SystemStatisticsRxWindowDropsTc0_Type()
)
systemStatisticsRxWindowDropsTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxWindowDropsTc0.setStatus("current")
_SystemStatisticsRxWindowDropsTc1_Type = Counter64
_SystemStatisticsRxWindowDropsTc1_Object = MibScalar
systemStatisticsRxWindowDropsTc1 = _SystemStatisticsRxWindowDropsTc1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 219),
    _SystemStatisticsRxWindowDropsTc1_Type()
)
systemStatisticsRxWindowDropsTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxWindowDropsTc1.setStatus("current")
_SystemStatisticsRxWindowDropsTc2_Type = Counter64
_SystemStatisticsRxWindowDropsTc2_Object = MibScalar
systemStatisticsRxWindowDropsTc2 = _SystemStatisticsRxWindowDropsTc2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 220),
    _SystemStatisticsRxWindowDropsTc2_Type()
)
systemStatisticsRxWindowDropsTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxWindowDropsTc2.setStatus("current")
_SystemStatisticsRxWindowDropsTc3_Type = Counter64
_SystemStatisticsRxWindowDropsTc3_Object = MibScalar
systemStatisticsRxWindowDropsTc3 = _SystemStatisticsRxWindowDropsTc3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 221),
    _SystemStatisticsRxWindowDropsTc3_Type()
)
systemStatisticsRxWindowDropsTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxWindowDropsTc3.setStatus("current")
_SystemStatisticsRxWindowDropsTc4_Type = Counter64
_SystemStatisticsRxWindowDropsTc4_Object = MibScalar
systemStatisticsRxWindowDropsTc4 = _SystemStatisticsRxWindowDropsTc4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 222),
    _SystemStatisticsRxWindowDropsTc4_Type()
)
systemStatisticsRxWindowDropsTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxWindowDropsTc4.setStatus("current")
_SystemStatisticsRxWindowDropsTc5_Type = Counter64
_SystemStatisticsRxWindowDropsTc5_Object = MibScalar
systemStatisticsRxWindowDropsTc5 = _SystemStatisticsRxWindowDropsTc5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 223),
    _SystemStatisticsRxWindowDropsTc5_Type()
)
systemStatisticsRxWindowDropsTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxWindowDropsTc5.setStatus("current")
_SystemStatisticsRxWindowDropsTc6_Type = Counter64
_SystemStatisticsRxWindowDropsTc6_Object = MibScalar
systemStatisticsRxWindowDropsTc6 = _SystemStatisticsRxWindowDropsTc6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 224),
    _SystemStatisticsRxWindowDropsTc6_Type()
)
systemStatisticsRxWindowDropsTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxWindowDropsTc6.setStatus("current")
_SystemStatisticsRxWindowDropsTc7_Type = Counter64
_SystemStatisticsRxWindowDropsTc7_Object = MibScalar
systemStatisticsRxWindowDropsTc7 = _SystemStatisticsRxWindowDropsTc7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 225),
    _SystemStatisticsRxWindowDropsTc7_Type()
)
systemStatisticsRxWindowDropsTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxWindowDropsTc7.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDropsTc0_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDropsTc0_Object = MibScalar
systemStatisticsRxUnexpectedReplayDropsTc0 = _SystemStatisticsRxUnexpectedReplayDropsTc0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 226),
    _SystemStatisticsRxUnexpectedReplayDropsTc0_Type()
)
systemStatisticsRxUnexpectedReplayDropsTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDropsTc0.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDropsTc1_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDropsTc1_Object = MibScalar
systemStatisticsRxUnexpectedReplayDropsTc1 = _SystemStatisticsRxUnexpectedReplayDropsTc1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 227),
    _SystemStatisticsRxUnexpectedReplayDropsTc1_Type()
)
systemStatisticsRxUnexpectedReplayDropsTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDropsTc1.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDropsTc2_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDropsTc2_Object = MibScalar
systemStatisticsRxUnexpectedReplayDropsTc2 = _SystemStatisticsRxUnexpectedReplayDropsTc2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 228),
    _SystemStatisticsRxUnexpectedReplayDropsTc2_Type()
)
systemStatisticsRxUnexpectedReplayDropsTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDropsTc2.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDropsTc3_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDropsTc3_Object = MibScalar
systemStatisticsRxUnexpectedReplayDropsTc3 = _SystemStatisticsRxUnexpectedReplayDropsTc3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 229),
    _SystemStatisticsRxUnexpectedReplayDropsTc3_Type()
)
systemStatisticsRxUnexpectedReplayDropsTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDropsTc3.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDropsTc4_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDropsTc4_Object = MibScalar
systemStatisticsRxUnexpectedReplayDropsTc4 = _SystemStatisticsRxUnexpectedReplayDropsTc4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 230),
    _SystemStatisticsRxUnexpectedReplayDropsTc4_Type()
)
systemStatisticsRxUnexpectedReplayDropsTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDropsTc4.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDropsTc5_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDropsTc5_Object = MibScalar
systemStatisticsRxUnexpectedReplayDropsTc5 = _SystemStatisticsRxUnexpectedReplayDropsTc5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 231),
    _SystemStatisticsRxUnexpectedReplayDropsTc5_Type()
)
systemStatisticsRxUnexpectedReplayDropsTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDropsTc5.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDropsTc6_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDropsTc6_Object = MibScalar
systemStatisticsRxUnexpectedReplayDropsTc6 = _SystemStatisticsRxUnexpectedReplayDropsTc6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 232),
    _SystemStatisticsRxUnexpectedReplayDropsTc6_Type()
)
systemStatisticsRxUnexpectedReplayDropsTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDropsTc6.setStatus("current")
_SystemStatisticsRxUnexpectedReplayDropsTc7_Type = Counter64
_SystemStatisticsRxUnexpectedReplayDropsTc7_Object = MibScalar
systemStatisticsRxUnexpectedReplayDropsTc7 = _SystemStatisticsRxUnexpectedReplayDropsTc7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 233),
    _SystemStatisticsRxUnexpectedReplayDropsTc7_Type()
)
systemStatisticsRxUnexpectedReplayDropsTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxUnexpectedReplayDropsTc7.setStatus("current")
_SystemStatisticsRxReplayIntegrityDropsTc0_Type = Counter64
_SystemStatisticsRxReplayIntegrityDropsTc0_Object = MibScalar
systemStatisticsRxReplayIntegrityDropsTc0 = _SystemStatisticsRxReplayIntegrityDropsTc0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 234),
    _SystemStatisticsRxReplayIntegrityDropsTc0_Type()
)
systemStatisticsRxReplayIntegrityDropsTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDropsTc0.setStatus("current")
_SystemStatisticsRxReplayIntegrityDropsTc1_Type = Counter64
_SystemStatisticsRxReplayIntegrityDropsTc1_Object = MibScalar
systemStatisticsRxReplayIntegrityDropsTc1 = _SystemStatisticsRxReplayIntegrityDropsTc1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 235),
    _SystemStatisticsRxReplayIntegrityDropsTc1_Type()
)
systemStatisticsRxReplayIntegrityDropsTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDropsTc1.setStatus("current")
_SystemStatisticsRxReplayIntegrityDropsTc2_Type = Counter64
_SystemStatisticsRxReplayIntegrityDropsTc2_Object = MibScalar
systemStatisticsRxReplayIntegrityDropsTc2 = _SystemStatisticsRxReplayIntegrityDropsTc2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 236),
    _SystemStatisticsRxReplayIntegrityDropsTc2_Type()
)
systemStatisticsRxReplayIntegrityDropsTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDropsTc2.setStatus("current")
_SystemStatisticsRxReplayIntegrityDropsTc3_Type = Counter64
_SystemStatisticsRxReplayIntegrityDropsTc3_Object = MibScalar
systemStatisticsRxReplayIntegrityDropsTc3 = _SystemStatisticsRxReplayIntegrityDropsTc3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 237),
    _SystemStatisticsRxReplayIntegrityDropsTc3_Type()
)
systemStatisticsRxReplayIntegrityDropsTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDropsTc3.setStatus("current")
_SystemStatisticsRxReplayIntegrityDropsTc4_Type = Counter64
_SystemStatisticsRxReplayIntegrityDropsTc4_Object = MibScalar
systemStatisticsRxReplayIntegrityDropsTc4 = _SystemStatisticsRxReplayIntegrityDropsTc4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 238),
    _SystemStatisticsRxReplayIntegrityDropsTc4_Type()
)
systemStatisticsRxReplayIntegrityDropsTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDropsTc4.setStatus("current")
_SystemStatisticsRxReplayIntegrityDropsTc5_Type = Counter64
_SystemStatisticsRxReplayIntegrityDropsTc5_Object = MibScalar
systemStatisticsRxReplayIntegrityDropsTc5 = _SystemStatisticsRxReplayIntegrityDropsTc5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 239),
    _SystemStatisticsRxReplayIntegrityDropsTc5_Type()
)
systemStatisticsRxReplayIntegrityDropsTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDropsTc5.setStatus("current")
_SystemStatisticsRxReplayIntegrityDropsTc6_Type = Counter64
_SystemStatisticsRxReplayIntegrityDropsTc6_Object = MibScalar
systemStatisticsRxReplayIntegrityDropsTc6 = _SystemStatisticsRxReplayIntegrityDropsTc6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 240),
    _SystemStatisticsRxReplayIntegrityDropsTc6_Type()
)
systemStatisticsRxReplayIntegrityDropsTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDropsTc6.setStatus("current")
_SystemStatisticsRxReplayIntegrityDropsTc7_Type = Counter64
_SystemStatisticsRxReplayIntegrityDropsTc7_Object = MibScalar
systemStatisticsRxReplayIntegrityDropsTc7 = _SystemStatisticsRxReplayIntegrityDropsTc7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 241),
    _SystemStatisticsRxReplayIntegrityDropsTc7_Type()
)
systemStatisticsRxReplayIntegrityDropsTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxReplayIntegrityDropsTc7.setStatus("current")
_SystemStatisticsIcmpRedirectTxDrops_Type = Counter64
_SystemStatisticsIcmpRedirectTxDrops_Object = MibScalar
systemStatisticsIcmpRedirectTxDrops = _SystemStatisticsIcmpRedirectTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 242),
    _SystemStatisticsIcmpRedirectTxDrops_Type()
)
systemStatisticsIcmpRedirectTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIcmpRedirectTxDrops.setStatus("current")
_SystemStatisticsIcmpRedirectRxDrops_Type = Counter64
_SystemStatisticsIcmpRedirectRxDrops_Object = MibScalar
systemStatisticsIcmpRedirectRxDrops = _SystemStatisticsIcmpRedirectRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 243),
    _SystemStatisticsIcmpRedirectRxDrops_Type()
)
systemStatisticsIcmpRedirectRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIcmpRedirectRxDrops.setStatus("current")
_SystemStatisticsRxL2MtuExceeded_Type = Counter64
_SystemStatisticsRxL2MtuExceeded_Object = MibScalar
systemStatisticsRxL2MtuExceeded = _SystemStatisticsRxL2MtuExceeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 244),
    _SystemStatisticsRxL2MtuExceeded_Type()
)
systemStatisticsRxL2MtuExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxL2MtuExceeded.setStatus("deprecated")
_SystemStatisticsTcpOptTimeoutStateErr_Type = Counter64
_SystemStatisticsTcpOptTimeoutStateErr_Object = MibScalar
systemStatisticsTcpOptTimeoutStateErr = _SystemStatisticsTcpOptTimeoutStateErr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 245),
    _SystemStatisticsTcpOptTimeoutStateErr_Type()
)
systemStatisticsTcpOptTimeoutStateErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptTimeoutStateErr.setStatus("current")
_SystemStatisticsTcpOptThirdSynPt_Type = Counter64
_SystemStatisticsTcpOptThirdSynPt_Object = MibScalar
systemStatisticsTcpOptThirdSynPt = _SystemStatisticsTcpOptThirdSynPt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 246),
    _SystemStatisticsTcpOptThirdSynPt_Type()
)
systemStatisticsTcpOptThirdSynPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptThirdSynPt.setStatus("current")
_SystemStatisticsTcpOptInitLimitPt_Type = Counter64
_SystemStatisticsTcpOptInitLimitPt_Object = MibScalar
systemStatisticsTcpOptInitLimitPt = _SystemStatisticsTcpOptInitLimitPt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 247),
    _SystemStatisticsTcpOptInitLimitPt_Type()
)
systemStatisticsTcpOptInitLimitPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptInitLimitPt.setStatus("current")
_SystemStatisticsTcpOptToCpu_Type = Counter64
_SystemStatisticsTcpOptToCpu_Object = MibScalar
systemStatisticsTcpOptToCpu = _SystemStatisticsTcpOptToCpu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 248),
    _SystemStatisticsTcpOptToCpu_Type()
)
systemStatisticsTcpOptToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptToCpu.setStatus("current")
_SystemStatisticsTcpOptFromCpu_Type = Counter64
_SystemStatisticsTcpOptFromCpu_Object = MibScalar
systemStatisticsTcpOptFromCpu = _SystemStatisticsTcpOptFromCpu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 249),
    _SystemStatisticsTcpOptFromCpu_Type()
)
systemStatisticsTcpOptFromCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptFromCpu.setStatus("current")
_SystemStatisticsTcpOptCtrlInvalidSeq_Type = Counter64
_SystemStatisticsTcpOptCtrlInvalidSeq_Object = MibScalar
systemStatisticsTcpOptCtrlInvalidSeq = _SystemStatisticsTcpOptCtrlInvalidSeq_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 250),
    _SystemStatisticsTcpOptCtrlInvalidSeq_Type()
)
systemStatisticsTcpOptCtrlInvalidSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptCtrlInvalidSeq.setStatus("current")
_SystemStatisticsTcpOptMboxTotal_Type = Counter64
_SystemStatisticsTcpOptMboxTotal_Object = MibScalar
systemStatisticsTcpOptMboxTotal = _SystemStatisticsTcpOptMboxTotal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 251),
    _SystemStatisticsTcpOptMboxTotal_Type()
)
systemStatisticsTcpOptMboxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptMboxTotal.setStatus("current")
_SystemStatisticsTcpOptNewFlow_Type = Counter64
_SystemStatisticsTcpOptNewFlow_Object = MibScalar
systemStatisticsTcpOptNewFlow = _SystemStatisticsTcpOptNewFlow_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 252),
    _SystemStatisticsTcpOptNewFlow_Type()
)
systemStatisticsTcpOptNewFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptNewFlow.setStatus("current")
_SystemStatisticsTcpOptDelFlow_Type = Counter64
_SystemStatisticsTcpOptDelFlow_Object = MibScalar
systemStatisticsTcpOptDelFlow = _SystemStatisticsTcpOptDelFlow_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 253),
    _SystemStatisticsTcpOptDelFlow_Type()
)
systemStatisticsTcpOptDelFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTcpOptDelFlow.setStatus("current")
_SystemStatisticsIpDirectBcastTxDrops_Type = Counter64
_SystemStatisticsIpDirectBcastTxDrops_Object = MibScalar
systemStatisticsIpDirectBcastTxDrops = _SystemStatisticsIpDirectBcastTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 254),
    _SystemStatisticsIpDirectBcastTxDrops_Type()
)
systemStatisticsIpDirectBcastTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpDirectBcastTxDrops.setStatus("current")
_SystemStatisticsIpDirectBcastTxL2Bcast_Type = Counter64
_SystemStatisticsIpDirectBcastTxL2Bcast_Object = MibScalar
systemStatisticsIpDirectBcastTxL2Bcast = _SystemStatisticsIpDirectBcastTxL2Bcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 255),
    _SystemStatisticsIpDirectBcastTxL2Bcast_Type()
)
systemStatisticsIpDirectBcastTxL2Bcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpDirectBcastTxL2Bcast.setStatus("current")
_SystemStatisticsRxInvalidIpHdr_Type = Counter64
_SystemStatisticsRxInvalidIpHdr_Object = MibScalar
systemStatisticsRxInvalidIpHdr = _SystemStatisticsRxInvalidIpHdr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 256),
    _SystemStatisticsRxInvalidIpHdr_Type()
)
systemStatisticsRxInvalidIpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsRxInvalidIpHdr.setStatus("current")
_SystemStatisticsNatDstNatMapInvalid_Type = Counter64
_SystemStatisticsNatDstNatMapInvalid_Object = MibScalar
systemStatisticsNatDstNatMapInvalid = _SystemStatisticsNatDstNatMapInvalid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 257),
    _SystemStatisticsNatDstNatMapInvalid_Type()
)
systemStatisticsNatDstNatMapInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsNatDstNatMapInvalid.setStatus("current")
_SystemStatisticsDevicePolicyDrops_Type = Counter64
_SystemStatisticsDevicePolicyDrops_Object = MibScalar
systemStatisticsDevicePolicyDrops = _SystemStatisticsDevicePolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 258),
    _SystemStatisticsDevicePolicyDrops_Type()
)
systemStatisticsDevicePolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDevicePolicyDrops.setStatus("current")
_SystemStatisticsInvalidLoopHdrDrops_Type = Counter64
_SystemStatisticsInvalidLoopHdrDrops_Object = MibScalar
systemStatisticsInvalidLoopHdrDrops = _SystemStatisticsInvalidLoopHdrDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 259),
    _SystemStatisticsInvalidLoopHdrDrops_Type()
)
systemStatisticsInvalidLoopHdrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsInvalidLoopHdrDrops.setStatus("current")
_SystemStatisticsZbfFragCacheDrops_Type = Counter64
_SystemStatisticsZbfFragCacheDrops_Object = MibScalar
systemStatisticsZbfFragCacheDrops = _SystemStatisticsZbfFragCacheDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 260),
    _SystemStatisticsZbfFragCacheDrops_Type()
)
systemStatisticsZbfFragCacheDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsZbfFragCacheDrops.setStatus("current")
_SystemStatisticsNatFragCacheDrops_Type = Counter64
_SystemStatisticsNatFragCacheDrops_Object = MibScalar
systemStatisticsNatFragCacheDrops = _SystemStatisticsNatFragCacheDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 261),
    _SystemStatisticsNatFragCacheDrops_Type()
)
systemStatisticsNatFragCacheDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsNatFragCacheDrops.setStatus("current")
_SystemStatisticsTxTrackerIfNotPreferred_Type = Counter64
_SystemStatisticsTxTrackerIfNotPreferred_Object = MibScalar
systemStatisticsTxTrackerIfNotPreferred = _SystemStatisticsTxTrackerIfNotPreferred_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 262),
    _SystemStatisticsTxTrackerIfNotPreferred_Type()
)
systemStatisticsTxTrackerIfNotPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsTxTrackerIfNotPreferred.setStatus("current")
_SystemStatisticsIpfragAllfragsSeen_Type = Counter64
_SystemStatisticsIpfragAllfragsSeen_Object = MibScalar
systemStatisticsIpfragAllfragsSeen = _SystemStatisticsIpfragAllfragsSeen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 263),
    _SystemStatisticsIpfragAllfragsSeen_Type()
)
systemStatisticsIpfragAllfragsSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpfragAllfragsSeen.setStatus("current")
_SystemStatisticsIpfragManyFrags_Type = Counter64
_SystemStatisticsIpfragManyFrags_Object = MibScalar
systemStatisticsIpfragManyFrags = _SystemStatisticsIpfragManyFrags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 264),
    _SystemStatisticsIpfragManyFrags_Type()
)
systemStatisticsIpfragManyFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsIpfragManyFrags.setStatus("current")
_SystemStatisticsVRRPMismatchedDMACDrops_Type = Counter64
_SystemStatisticsVRRPMismatchedDMACDrops_Object = MibScalar
systemStatisticsVRRPMismatchedDMACDrops = _SystemStatisticsVRRPMismatchedDMACDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 2, 265),
    _SystemStatisticsVRRPMismatchedDMACDrops_Type()
)
systemStatisticsVRRPMismatchedDMACDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsVRRPMismatchedDMACDrops.setStatus("current")
_SystemStatisticsDiff_ObjectIdentity = ObjectIdentity
systemStatisticsDiff = _SystemStatisticsDiff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3)
)
_SystemStatisticsDiffRxPkts_Type = Counter64
_SystemStatisticsDiffRxPkts_Object = MibScalar
systemStatisticsDiffRxPkts = _SystemStatisticsDiffRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 1),
    _SystemStatisticsDiffRxPkts_Type()
)
systemStatisticsDiffRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxPkts.setStatus("current")
_SystemStatisticsDiffRxDrops_Type = Counter64
_SystemStatisticsDiffRxDrops_Object = MibScalar
systemStatisticsDiffRxDrops = _SystemStatisticsDiffRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 2),
    _SystemStatisticsDiffRxDrops_Type()
)
systemStatisticsDiffRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxDrops.setStatus("current")
_SystemStatisticsDiffIpFwd_Type = Counter64
_SystemStatisticsDiffIpFwd_Object = MibScalar
systemStatisticsDiffIpFwd = _SystemStatisticsDiffIpFwd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 3),
    _SystemStatisticsDiffIpFwd_Type()
)
systemStatisticsDiffIpFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwd.setStatus("current")
_SystemStatisticsDiffIpFwdMirrorPkts_Type = Counter64
_SystemStatisticsDiffIpFwdMirrorPkts_Object = MibScalar
systemStatisticsDiffIpFwdMirrorPkts = _SystemStatisticsDiffIpFwdMirrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 4),
    _SystemStatisticsDiffIpFwdMirrorPkts_Type()
)
systemStatisticsDiffIpFwdMirrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdMirrorPkts.setStatus("current")
_SystemStatisticsDiffIpFwdArp_Type = Counter64
_SystemStatisticsDiffIpFwdArp_Object = MibScalar
systemStatisticsDiffIpFwdArp = _SystemStatisticsDiffIpFwdArp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 5),
    _SystemStatisticsDiffIpFwdArp_Type()
)
systemStatisticsDiffIpFwdArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdArp.setStatus("current")
_SystemStatisticsDiffIpFwdToEgress_Type = Counter64
_SystemStatisticsDiffIpFwdToEgress_Object = MibScalar
systemStatisticsDiffIpFwdToEgress = _SystemStatisticsDiffIpFwdToEgress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 6),
    _SystemStatisticsDiffIpFwdToEgress_Type()
)
systemStatisticsDiffIpFwdToEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdToEgress.setStatus("current")
_SystemStatisticsDiffIpFwdInvalidOil_Type = Counter64
_SystemStatisticsDiffIpFwdInvalidOil_Object = MibScalar
systemStatisticsDiffIpFwdInvalidOil = _SystemStatisticsDiffIpFwdInvalidOil_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 7),
    _SystemStatisticsDiffIpFwdInvalidOil_Type()
)
systemStatisticsDiffIpFwdInvalidOil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdInvalidOil.setStatus("current")
_SystemStatisticsDiffIpV6McastDrops_Type = Counter64
_SystemStatisticsDiffIpV6McastDrops_Object = MibScalar
systemStatisticsDiffIpV6McastDrops = _SystemStatisticsDiffIpV6McastDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 8),
    _SystemStatisticsDiffIpV6McastDrops_Type()
)
systemStatisticsDiffIpV6McastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpV6McastDrops.setStatus("current")
_SystemStatisticsDiffIpFwdMcastInvalidIif_Type = Counter64
_SystemStatisticsDiffIpFwdMcastInvalidIif_Object = MibScalar
systemStatisticsDiffIpFwdMcastInvalidIif = _SystemStatisticsDiffIpFwdMcastInvalidIif_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 9),
    _SystemStatisticsDiffIpFwdMcastInvalidIif_Type()
)
systemStatisticsDiffIpFwdMcastInvalidIif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdMcastInvalidIif.setStatus("current")
_SystemStatisticsDiffIpFwdMcastLifeExceededDrops_Type = Counter64
_SystemStatisticsDiffIpFwdMcastLifeExceededDrops_Object = MibScalar
systemStatisticsDiffIpFwdMcastLifeExceededDrops = _SystemStatisticsDiffIpFwdMcastLifeExceededDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 10),
    _SystemStatisticsDiffIpFwdMcastLifeExceededDrops_Type()
)
systemStatisticsDiffIpFwdMcastLifeExceededDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdMcastLifeExceededDrops.setStatus("current")
_SystemStatisticsDiffRxMcastThresholdExceeded_Type = Counter64
_SystemStatisticsDiffRxMcastThresholdExceeded_Object = MibScalar
systemStatisticsDiffRxMcastThresholdExceeded = _SystemStatisticsDiffRxMcastThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 11),
    _SystemStatisticsDiffRxMcastThresholdExceeded_Type()
)
systemStatisticsDiffRxMcastThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxMcastThresholdExceeded.setStatus("current")
_SystemStatisticsDiffIpFwdInvalidTunOil_Type = Counter64
_SystemStatisticsDiffIpFwdInvalidTunOil_Object = MibScalar
systemStatisticsDiffIpFwdInvalidTunOil = _SystemStatisticsDiffIpFwdInvalidTunOil_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 12),
    _SystemStatisticsDiffIpFwdInvalidTunOil_Type()
)
systemStatisticsDiffIpFwdInvalidTunOil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdInvalidTunOil.setStatus("current")
_SystemStatisticsDiffRxMcastPolicyFwdDrops_Type = Counter64
_SystemStatisticsDiffRxMcastPolicyFwdDrops_Object = MibScalar
systemStatisticsDiffRxMcastPolicyFwdDrops = _SystemStatisticsDiffRxMcastPolicyFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 13),
    _SystemStatisticsDiffRxMcastPolicyFwdDrops_Type()
)
systemStatisticsDiffRxMcastPolicyFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxMcastPolicyFwdDrops.setStatus("current")
_SystemStatisticsDiffRxMcastMirrorFwdDrops_Type = Counter64
_SystemStatisticsDiffRxMcastMirrorFwdDrops_Object = MibScalar
systemStatisticsDiffRxMcastMirrorFwdDrops = _SystemStatisticsDiffRxMcastMirrorFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 14),
    _SystemStatisticsDiffRxMcastMirrorFwdDrops_Type()
)
systemStatisticsDiffRxMcastMirrorFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxMcastMirrorFwdDrops.setStatus("current")
_SystemStatisticsDiffIpFwdNullMcastGroup_Type = Counter64
_SystemStatisticsDiffIpFwdNullMcastGroup_Object = MibScalar
systemStatisticsDiffIpFwdNullMcastGroup = _SystemStatisticsDiffIpFwdNullMcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 15),
    _SystemStatisticsDiffIpFwdNullMcastGroup_Type()
)
systemStatisticsDiffIpFwdNullMcastGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdNullMcastGroup.setStatus("current")
_SystemStatisticsDiffIpFwdNullNhop_Type = Counter64
_SystemStatisticsDiffIpFwdNullNhop_Object = MibScalar
systemStatisticsDiffIpFwdNullNhop = _SystemStatisticsDiffIpFwdNullNhop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 16),
    _SystemStatisticsDiffIpFwdNullNhop_Type()
)
systemStatisticsDiffIpFwdNullNhop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdNullNhop.setStatus("current")
_SystemStatisticsDiffIpFwdUnknownNhType_Type = Counter64
_SystemStatisticsDiffIpFwdUnknownNhType_Object = MibScalar
systemStatisticsDiffIpFwdUnknownNhType = _SystemStatisticsDiffIpFwdUnknownNhType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 17),
    _SystemStatisticsDiffIpFwdUnknownNhType_Type()
)
systemStatisticsDiffIpFwdUnknownNhType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdUnknownNhType.setStatus("current")
_SystemStatisticsDiffIpFwdNatOnTunnel_Type = Counter64
_SystemStatisticsDiffIpFwdNatOnTunnel_Object = MibScalar
systemStatisticsDiffIpFwdNatOnTunnel = _SystemStatisticsDiffIpFwdNatOnTunnel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 18),
    _SystemStatisticsDiffIpFwdNatOnTunnel_Type()
)
systemStatisticsDiffIpFwdNatOnTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdNatOnTunnel.setStatus("current")
_SystemStatisticsDiffIpFwdToCpu_Type = Counter64
_SystemStatisticsDiffIpFwdToCpu_Object = MibScalar
systemStatisticsDiffIpFwdToCpu = _SystemStatisticsDiffIpFwdToCpu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 19),
    _SystemStatisticsDiffIpFwdToCpu_Type()
)
systemStatisticsDiffIpFwdToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdToCpu.setStatus("current")
_SystemStatisticsDiffIpFwdToCpuNatXlates_Type = Counter64
_SystemStatisticsDiffIpFwdToCpuNatXlates_Object = MibScalar
systemStatisticsDiffIpFwdToCpuNatXlates = _SystemStatisticsDiffIpFwdToCpuNatXlates_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 20),
    _SystemStatisticsDiffIpFwdToCpuNatXlates_Type()
)
systemStatisticsDiffIpFwdToCpuNatXlates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdToCpuNatXlates.setStatus("current")
_SystemStatisticsDiffIpFwdFromCpuNatXlates_Type = Counter64
_SystemStatisticsDiffIpFwdFromCpuNatXlates_Object = MibScalar
systemStatisticsDiffIpFwdFromCpuNatXlates = _SystemStatisticsDiffIpFwdFromCpuNatXlates_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 21),
    _SystemStatisticsDiffIpFwdFromCpuNatXlates_Type()
)
systemStatisticsDiffIpFwdFromCpuNatXlates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdFromCpuNatXlates.setStatus("current")
_SystemStatisticsDiffIpFwdToCpuNatDrops_Type = Counter64
_SystemStatisticsDiffIpFwdToCpuNatDrops_Object = MibScalar
systemStatisticsDiffIpFwdToCpuNatDrops = _SystemStatisticsDiffIpFwdToCpuNatDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 22),
    _SystemStatisticsDiffIpFwdToCpuNatDrops_Type()
)
systemStatisticsDiffIpFwdToCpuNatDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdToCpuNatDrops.setStatus("current")
_SystemStatisticsDiffIpFwdFromCpuNonLocal_Type = Counter64
_SystemStatisticsDiffIpFwdFromCpuNonLocal_Object = MibScalar
systemStatisticsDiffIpFwdFromCpuNonLocal = _SystemStatisticsDiffIpFwdFromCpuNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 23),
    _SystemStatisticsDiffIpFwdFromCpuNonLocal_Type()
)
systemStatisticsDiffIpFwdFromCpuNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdFromCpuNonLocal.setStatus("current")
_SystemStatisticsDiffIpFwdRxIpsec_Type = Counter64
_SystemStatisticsDiffIpFwdRxIpsec_Object = MibScalar
systemStatisticsDiffIpFwdRxIpsec = _SystemStatisticsDiffIpFwdRxIpsec_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 24),
    _SystemStatisticsDiffIpFwdRxIpsec_Type()
)
systemStatisticsDiffIpFwdRxIpsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdRxIpsec.setStatus("current")
_SystemStatisticsDiffIpFwdMcastPkts_Type = Counter64
_SystemStatisticsDiffIpFwdMcastPkts_Object = MibScalar
systemStatisticsDiffIpFwdMcastPkts = _SystemStatisticsDiffIpFwdMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 25),
    _SystemStatisticsDiffIpFwdMcastPkts_Type()
)
systemStatisticsDiffIpFwdMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdMcastPkts.setStatus("current")
_SystemStatisticsDiffIpFwdRxGre_Type = Counter64
_SystemStatisticsDiffIpFwdRxGre_Object = MibScalar
systemStatisticsDiffIpFwdRxGre = _SystemStatisticsDiffIpFwdRxGre_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 26),
    _SystemStatisticsDiffIpFwdRxGre_Type()
)
systemStatisticsDiffIpFwdRxGre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpFwdRxGre.setStatus("current")
_SystemStatisticsDiffNatXlateOutbound_Type = Counter64
_SystemStatisticsDiffNatXlateOutbound_Object = MibScalar
systemStatisticsDiffNatXlateOutbound = _SystemStatisticsDiffNatXlateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 27),
    _SystemStatisticsDiffNatXlateOutbound_Type()
)
systemStatisticsDiffNatXlateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffNatXlateOutbound.setStatus("current")
_SystemStatisticsDiffNatXlateOutboundDrops_Type = Counter64
_SystemStatisticsDiffNatXlateOutboundDrops_Object = MibScalar
systemStatisticsDiffNatXlateOutboundDrops = _SystemStatisticsDiffNatXlateOutboundDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 28),
    _SystemStatisticsDiffNatXlateOutboundDrops_Type()
)
systemStatisticsDiffNatXlateOutboundDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffNatXlateOutboundDrops.setStatus("current")
_SystemStatisticsDiffNatXlateInbound_Type = Counter64
_SystemStatisticsDiffNatXlateInbound_Object = MibScalar
systemStatisticsDiffNatXlateInbound = _SystemStatisticsDiffNatXlateInbound_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 29),
    _SystemStatisticsDiffNatXlateInbound_Type()
)
systemStatisticsDiffNatXlateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffNatXlateInbound.setStatus("current")
_SystemStatisticsDiffNatXlateInboundFail_Type = Counter64
_SystemStatisticsDiffNatXlateInboundFail_Object = MibScalar
systemStatisticsDiffNatXlateInboundFail = _SystemStatisticsDiffNatXlateInboundFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 30),
    _SystemStatisticsDiffNatXlateInboundFail_Type()
)
systemStatisticsDiffNatXlateInboundFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffNatXlateInboundFail.setStatus("current")
_SystemStatisticsDiffCflowdPkts_Type = Counter64
_SystemStatisticsDiffCflowdPkts_Object = MibScalar
systemStatisticsDiffCflowdPkts = _SystemStatisticsDiffCflowdPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 31),
    _SystemStatisticsDiffCflowdPkts_Type()
)
systemStatisticsDiffCflowdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffCflowdPkts.setStatus("current")
_SystemStatisticsDiffRxBcast_Type = Counter64
_SystemStatisticsDiffRxBcast_Object = MibScalar
systemStatisticsDiffRxBcast = _SystemStatisticsDiffRxBcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 32),
    _SystemStatisticsDiffRxBcast_Type()
)
systemStatisticsDiffRxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxBcast.setStatus("current")
_SystemStatisticsDiffRxMcast_Type = Counter64
_SystemStatisticsDiffRxMcast_Object = MibScalar
systemStatisticsDiffRxMcast = _SystemStatisticsDiffRxMcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 33),
    _SystemStatisticsDiffRxMcast_Type()
)
systemStatisticsDiffRxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxMcast.setStatus("current")
_SystemStatisticsDiffRxMcastLinkLocal_Type = Counter64
_SystemStatisticsDiffRxMcastLinkLocal_Object = MibScalar
systemStatisticsDiffRxMcastLinkLocal = _SystemStatisticsDiffRxMcastLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 34),
    _SystemStatisticsDiffRxMcastLinkLocal_Type()
)
systemStatisticsDiffRxMcastLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxMcastLinkLocal.setStatus("current")
_SystemStatisticsDiffRxMcastFilterToCpu_Type = Counter64
_SystemStatisticsDiffRxMcastFilterToCpu_Object = MibScalar
systemStatisticsDiffRxMcastFilterToCpu = _SystemStatisticsDiffRxMcastFilterToCpu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 35),
    _SystemStatisticsDiffRxMcastFilterToCpu_Type()
)
systemStatisticsDiffRxMcastFilterToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxMcastFilterToCpu.setStatus("current")
_SystemStatisticsDiffRxMcastFilterToCpuAndFwd_Type = Counter64
_SystemStatisticsDiffRxMcastFilterToCpuAndFwd_Object = MibScalar
systemStatisticsDiffRxMcastFilterToCpuAndFwd = _SystemStatisticsDiffRxMcastFilterToCpuAndFwd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 36),
    _SystemStatisticsDiffRxMcastFilterToCpuAndFwd_Type()
)
systemStatisticsDiffRxMcastFilterToCpuAndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxMcastFilterToCpuAndFwd.setStatus("current")
_SystemStatisticsDiffRxGreDecap_Type = Counter64
_SystemStatisticsDiffRxGreDecap_Object = MibScalar
systemStatisticsDiffRxGreDecap = _SystemStatisticsDiffRxGreDecap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 37),
    _SystemStatisticsDiffRxGreDecap_Type()
)
systemStatisticsDiffRxGreDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxGreDecap.setStatus("current")
_SystemStatisticsDiffRxGreDrops_Type = Counter64
_SystemStatisticsDiffRxGreDrops_Object = MibScalar
systemStatisticsDiffRxGreDrops = _SystemStatisticsDiffRxGreDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 38),
    _SystemStatisticsDiffRxGreDrops_Type()
)
systemStatisticsDiffRxGreDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxGreDrops.setStatus("current")
_SystemStatisticsDiffRxGrePolicerDrops_Type = Counter64
_SystemStatisticsDiffRxGrePolicerDrops_Object = MibScalar
systemStatisticsDiffRxGrePolicerDrops = _SystemStatisticsDiffRxGrePolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 39),
    _SystemStatisticsDiffRxGrePolicerDrops_Type()
)
systemStatisticsDiffRxGrePolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxGrePolicerDrops.setStatus("current")
_SystemStatisticsDiffRxImplicitAclDrops_Type = Counter64
_SystemStatisticsDiffRxImplicitAclDrops_Object = MibScalar
systemStatisticsDiffRxImplicitAclDrops = _SystemStatisticsDiffRxImplicitAclDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 40),
    _SystemStatisticsDiffRxImplicitAclDrops_Type()
)
systemStatisticsDiffRxImplicitAclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxImplicitAclDrops.setStatus("current")
_SystemStatisticsDiffRxIpsecDecap_Type = Counter64
_SystemStatisticsDiffRxIpsecDecap_Object = MibScalar
systemStatisticsDiffRxIpsecDecap = _SystemStatisticsDiffRxIpsecDecap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 41),
    _SystemStatisticsDiffRxIpsecDecap_Type()
)
systemStatisticsDiffRxIpsecDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIpsecDecap.setStatus("current")
_SystemStatisticsDiffRxIp6IpsecDrops_Type = Counter64
_SystemStatisticsDiffRxIp6IpsecDrops_Object = MibScalar
systemStatisticsDiffRxIp6IpsecDrops = _SystemStatisticsDiffRxIp6IpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 42),
    _SystemStatisticsDiffRxIp6IpsecDrops_Type()
)
systemStatisticsDiffRxIp6IpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIp6IpsecDrops.setStatus("current")
_SystemStatisticsDiffRxSaIpsecDrops_Type = Counter64
_SystemStatisticsDiffRxSaIpsecDrops_Object = MibScalar
systemStatisticsDiffRxSaIpsecDrops = _SystemStatisticsDiffRxSaIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 43),
    _SystemStatisticsDiffRxSaIpsecDrops_Type()
)
systemStatisticsDiffRxSaIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxSaIpsecDrops.setStatus("current")
_SystemStatisticsDiffRxInvalidIpsecPktSize_Type = Counter64
_SystemStatisticsDiffRxInvalidIpsecPktSize_Object = MibScalar
systemStatisticsDiffRxInvalidIpsecPktSize = _SystemStatisticsDiffRxInvalidIpsecPktSize_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 44),
    _SystemStatisticsDiffRxInvalidIpsecPktSize_Type()
)
systemStatisticsDiffRxInvalidIpsecPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxInvalidIpsecPktSize.setStatus("current")
_SystemStatisticsDiffRxSpiIpsecDrops_Type = Counter64
_SystemStatisticsDiffRxSpiIpsecDrops_Object = MibScalar
systemStatisticsDiffRxSpiIpsecDrops = _SystemStatisticsDiffRxSpiIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 45),
    _SystemStatisticsDiffRxSpiIpsecDrops_Type()
)
systemStatisticsDiffRxSpiIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxSpiIpsecDrops.setStatus("current")
_SystemStatisticsDiffRxReplayDrops_Type = Counter64
_SystemStatisticsDiffRxReplayDrops_Object = MibScalar
systemStatisticsDiffRxReplayDrops = _SystemStatisticsDiffRxReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 46),
    _SystemStatisticsDiffRxReplayDrops_Type()
)
systemStatisticsDiffRxReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDrops.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDrops_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDrops_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDrops = _SystemStatisticsDiffRxReplayIntegrityDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 47),
    _SystemStatisticsDiffRxReplayIntegrityDrops_Type()
)
systemStatisticsDiffRxReplayIntegrityDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDrops.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDrops_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDrops_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDrops = _SystemStatisticsDiffRxUnexpectedReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 48),
    _SystemStatisticsDiffRxUnexpectedReplayDrops_Type()
)
systemStatisticsDiffRxUnexpectedReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDrops.setStatus("current")
_SystemStatisticsDiffRxNextHdrIpsecDrops_Type = Counter64
_SystemStatisticsDiffRxNextHdrIpsecDrops_Object = MibScalar
systemStatisticsDiffRxNextHdrIpsecDrops = _SystemStatisticsDiffRxNextHdrIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 49),
    _SystemStatisticsDiffRxNextHdrIpsecDrops_Type()
)
systemStatisticsDiffRxNextHdrIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxNextHdrIpsecDrops.setStatus("current")
_SystemStatisticsDiffRxMacCompareIpsecDrops_Type = Counter64
_SystemStatisticsDiffRxMacCompareIpsecDrops_Object = MibScalar
systemStatisticsDiffRxMacCompareIpsecDrops = _SystemStatisticsDiffRxMacCompareIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 50),
    _SystemStatisticsDiffRxMacCompareIpsecDrops_Type()
)
systemStatisticsDiffRxMacCompareIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxMacCompareIpsecDrops.setStatus("current")
_SystemStatisticsDiffRxErrPadIpsecDrops_Type = Counter64
_SystemStatisticsDiffRxErrPadIpsecDrops_Object = MibScalar
systemStatisticsDiffRxErrPadIpsecDrops = _SystemStatisticsDiffRxErrPadIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 51),
    _SystemStatisticsDiffRxErrPadIpsecDrops_Type()
)
systemStatisticsDiffRxErrPadIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxErrPadIpsecDrops.setStatus("current")
_SystemStatisticsDiffRxIpsecPolicerDrops_Type = Counter64
_SystemStatisticsDiffRxIpsecPolicerDrops_Object = MibScalar
systemStatisticsDiffRxIpsecPolicerDrops = _SystemStatisticsDiffRxIpsecPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 52),
    _SystemStatisticsDiffRxIpsecPolicerDrops_Type()
)
systemStatisticsDiffRxIpsecPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIpsecPolicerDrops.setStatus("current")
_SystemStatisticsDiffRxPreIpsecPkts_Type = Counter64
_SystemStatisticsDiffRxPreIpsecPkts_Object = MibScalar
systemStatisticsDiffRxPreIpsecPkts = _SystemStatisticsDiffRxPreIpsecPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 53),
    _SystemStatisticsDiffRxPreIpsecPkts_Type()
)
systemStatisticsDiffRxPreIpsecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxPreIpsecPkts.setStatus("current")
_SystemStatisticsDiffRxPreIpsecDrops_Type = Counter64
_SystemStatisticsDiffRxPreIpsecDrops_Object = MibScalar
systemStatisticsDiffRxPreIpsecDrops = _SystemStatisticsDiffRxPreIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 54),
    _SystemStatisticsDiffRxPreIpsecDrops_Type()
)
systemStatisticsDiffRxPreIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxPreIpsecDrops.setStatus("current")
_SystemStatisticsDiffRxPreIpsecPolicerDrops_Type = Counter64
_SystemStatisticsDiffRxPreIpsecPolicerDrops_Object = MibScalar
systemStatisticsDiffRxPreIpsecPolicerDrops = _SystemStatisticsDiffRxPreIpsecPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 55),
    _SystemStatisticsDiffRxPreIpsecPolicerDrops_Type()
)
systemStatisticsDiffRxPreIpsecPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxPreIpsecPolicerDrops.setStatus("current")
_SystemStatisticsDiffRxPreIpsecDecap_Type = Counter64
_SystemStatisticsDiffRxPreIpsecDecap_Object = MibScalar
systemStatisticsDiffRxPreIpsecDecap = _SystemStatisticsDiffRxPreIpsecDecap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 56),
    _SystemStatisticsDiffRxPreIpsecDecap_Type()
)
systemStatisticsDiffRxPreIpsecDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxPreIpsecDecap.setStatus("current")
_SystemStatisticsDiffOpensslAesDecrypt_Type = Counter64
_SystemStatisticsDiffOpensslAesDecrypt_Object = MibScalar
systemStatisticsDiffOpensslAesDecrypt = _SystemStatisticsDiffOpensslAesDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 57),
    _SystemStatisticsDiffOpensslAesDecrypt_Type()
)
systemStatisticsDiffOpensslAesDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffOpensslAesDecrypt.setStatus("current")
_SystemStatisticsDiffRxIpsecBadInner_Type = Counter64
_SystemStatisticsDiffRxIpsecBadInner_Object = MibScalar
systemStatisticsDiffRxIpsecBadInner = _SystemStatisticsDiffRxIpsecBadInner_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 58),
    _SystemStatisticsDiffRxIpsecBadInner_Type()
)
systemStatisticsDiffRxIpsecBadInner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIpsecBadInner.setStatus("current")
_SystemStatisticsDiffRxBadLabel_Type = Counter64
_SystemStatisticsDiffRxBadLabel_Object = MibScalar
systemStatisticsDiffRxBadLabel = _SystemStatisticsDiffRxBadLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 59),
    _SystemStatisticsDiffRxBadLabel_Type()
)
systemStatisticsDiffRxBadLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxBadLabel.setStatus("current")
_SystemStatisticsDiffServiceLabelFwd_Type = Counter64
_SystemStatisticsDiffServiceLabelFwd_Object = MibScalar
systemStatisticsDiffServiceLabelFwd = _SystemStatisticsDiffServiceLabelFwd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 60),
    _SystemStatisticsDiffServiceLabelFwd_Type()
)
systemStatisticsDiffServiceLabelFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffServiceLabelFwd.setStatus("current")
_SystemStatisticsDiffRxHostLocalPkt_Type = Counter64
_SystemStatisticsDiffRxHostLocalPkt_Object = MibScalar
systemStatisticsDiffRxHostLocalPkt = _SystemStatisticsDiffRxHostLocalPkt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 61),
    _SystemStatisticsDiffRxHostLocalPkt_Type()
)
systemStatisticsDiffRxHostLocalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxHostLocalPkt.setStatus("current")
_SystemStatisticsDiffRxHostMirrorDrops_Type = Counter64
_SystemStatisticsDiffRxHostMirrorDrops_Object = MibScalar
systemStatisticsDiffRxHostMirrorDrops = _SystemStatisticsDiffRxHostMirrorDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 62),
    _SystemStatisticsDiffRxHostMirrorDrops_Type()
)
systemStatisticsDiffRxHostMirrorDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxHostMirrorDrops.setStatus("current")
_SystemStatisticsDiffRxTunneledPkts_Type = Counter64
_SystemStatisticsDiffRxTunneledPkts_Object = MibScalar
systemStatisticsDiffRxTunneledPkts = _SystemStatisticsDiffRxTunneledPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 63),
    _SystemStatisticsDiffRxTunneledPkts_Type()
)
systemStatisticsDiffRxTunneledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxTunneledPkts.setStatus("current")
_SystemStatisticsDiffRxCpNonLocal_Type = Counter64
_SystemStatisticsDiffRxCpNonLocal_Object = MibScalar
systemStatisticsDiffRxCpNonLocal = _SystemStatisticsDiffRxCpNonLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 64),
    _SystemStatisticsDiffRxCpNonLocal_Type()
)
systemStatisticsDiffRxCpNonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxCpNonLocal.setStatus("current")
_SystemStatisticsDiffTxIfNotPreferred_Type = Counter64
_SystemStatisticsDiffTxIfNotPreferred_Object = MibScalar
systemStatisticsDiffTxIfNotPreferred = _SystemStatisticsDiffTxIfNotPreferred_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 65),
    _SystemStatisticsDiffTxIfNotPreferred_Type()
)
systemStatisticsDiffTxIfNotPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIfNotPreferred.setStatus("current")
_SystemStatisticsDiffTxVsmartDrop_Type = Counter64
_SystemStatisticsDiffTxVsmartDrop_Object = MibScalar
systemStatisticsDiffTxVsmartDrop = _SystemStatisticsDiffTxVsmartDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 66),
    _SystemStatisticsDiffTxVsmartDrop_Type()
)
systemStatisticsDiffTxVsmartDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxVsmartDrop.setStatus("current")
_SystemStatisticsDiffRxInvalidPort_Type = Counter64
_SystemStatisticsDiffRxInvalidPort_Object = MibScalar
systemStatisticsDiffRxInvalidPort = _SystemStatisticsDiffRxInvalidPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 67),
    _SystemStatisticsDiffRxInvalidPort_Type()
)
systemStatisticsDiffRxInvalidPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxInvalidPort.setStatus("current")
_SystemStatisticsDiffPortDisabledRx_Type = Counter64
_SystemStatisticsDiffPortDisabledRx_Object = MibScalar
systemStatisticsDiffPortDisabledRx = _SystemStatisticsDiffPortDisabledRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 68),
    _SystemStatisticsDiffPortDisabledRx_Type()
)
systemStatisticsDiffPortDisabledRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffPortDisabledRx.setStatus("current")
_SystemStatisticsDiffIpDisabledRx_Type = Counter64
_SystemStatisticsDiffIpDisabledRx_Object = MibScalar
systemStatisticsDiffIpDisabledRx = _SystemStatisticsDiffIpDisabledRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 69),
    _SystemStatisticsDiffIpDisabledRx_Type()
)
systemStatisticsDiffIpDisabledRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpDisabledRx.setStatus("current")
_SystemStatisticsDiffRxInvalidQtags_Type = Counter64
_SystemStatisticsDiffRxInvalidQtags_Object = MibScalar
systemStatisticsDiffRxInvalidQtags = _SystemStatisticsDiffRxInvalidQtags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 70),
    _SystemStatisticsDiffRxInvalidQtags_Type()
)
systemStatisticsDiffRxInvalidQtags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxInvalidQtags.setStatus("current")
_SystemStatisticsDiffRxNonIpDrops_Type = Counter64
_SystemStatisticsDiffRxNonIpDrops_Object = MibScalar
systemStatisticsDiffRxNonIpDrops = _SystemStatisticsDiffRxNonIpDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 71),
    _SystemStatisticsDiffRxNonIpDrops_Type()
)
systemStatisticsDiffRxNonIpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxNonIpDrops.setStatus("current")
_SystemStatisticsDiffRxIpErrs_Type = Counter64
_SystemStatisticsDiffRxIpErrs_Object = MibScalar
systemStatisticsDiffRxIpErrs = _SystemStatisticsDiffRxIpErrs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 72),
    _SystemStatisticsDiffRxIpErrs_Type()
)
systemStatisticsDiffRxIpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIpErrs.setStatus("current")
_SystemStatisticsDiffPkoWredDrops_Type = Counter64
_SystemStatisticsDiffPkoWredDrops_Object = MibScalar
systemStatisticsDiffPkoWredDrops = _SystemStatisticsDiffPkoWredDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 73),
    _SystemStatisticsDiffPkoWredDrops_Type()
)
systemStatisticsDiffPkoWredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffPkoWredDrops.setStatus("current")
_SystemStatisticsDiffTxQueueExceeded_Type = Counter64
_SystemStatisticsDiffTxQueueExceeded_Object = MibScalar
systemStatisticsDiffTxQueueExceeded = _SystemStatisticsDiffTxQueueExceeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 74),
    _SystemStatisticsDiffTxQueueExceeded_Type()
)
systemStatisticsDiffTxQueueExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxQueueExceeded.setStatus("current")
_SystemStatisticsDiffRxPolicerDrops_Type = Counter64
_SystemStatisticsDiffRxPolicerDrops_Object = MibScalar
systemStatisticsDiffRxPolicerDrops = _SystemStatisticsDiffRxPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 75),
    _SystemStatisticsDiffRxPolicerDrops_Type()
)
systemStatisticsDiffRxPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxPolicerDrops.setStatus("current")
_SystemStatisticsDiffRouteToHost_Type = Counter64
_SystemStatisticsDiffRouteToHost_Object = MibScalar
systemStatisticsDiffRouteToHost = _SystemStatisticsDiffRouteToHost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 76),
    _SystemStatisticsDiffRouteToHost_Type()
)
systemStatisticsDiffRouteToHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRouteToHost.setStatus("current")
_SystemStatisticsDiffTtlExpired_Type = Counter64
_SystemStatisticsDiffTtlExpired_Object = MibScalar
systemStatisticsDiffTtlExpired = _SystemStatisticsDiffTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 77),
    _SystemStatisticsDiffTtlExpired_Type()
)
systemStatisticsDiffTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTtlExpired.setStatus("current")
_SystemStatisticsDiffIcmpRedirect_Type = Counter64
_SystemStatisticsDiffIcmpRedirect_Object = MibScalar
systemStatisticsDiffIcmpRedirect = _SystemStatisticsDiffIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 78),
    _SystemStatisticsDiffIcmpRedirect_Type()
)
systemStatisticsDiffIcmpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIcmpRedirect.setStatus("current")
_SystemStatisticsDiffBfdRxNonIp_Type = Counter64
_SystemStatisticsDiffBfdRxNonIp_Object = MibScalar
systemStatisticsDiffBfdRxNonIp = _SystemStatisticsDiffBfdRxNonIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 79),
    _SystemStatisticsDiffBfdRxNonIp_Type()
)
systemStatisticsDiffBfdRxNonIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdRxNonIp.setStatus("current")
_SystemStatisticsDiffBfdTxRecordChanged_Type = Counter64
_SystemStatisticsDiffBfdTxRecordChanged_Object = MibScalar
systemStatisticsDiffBfdTxRecordChanged = _SystemStatisticsDiffBfdTxRecordChanged_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 80),
    _SystemStatisticsDiffBfdTxRecordChanged_Type()
)
systemStatisticsDiffBfdTxRecordChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdTxRecordChanged.setStatus("current")
_SystemStatisticsDiffBfdRxRecordInvalid_Type = Counter64
_SystemStatisticsDiffBfdRxRecordInvalid_Object = MibScalar
systemStatisticsDiffBfdRxRecordInvalid = _SystemStatisticsDiffBfdRxRecordInvalid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 81),
    _SystemStatisticsDiffBfdRxRecordInvalid_Type()
)
systemStatisticsDiffBfdRxRecordInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdRxRecordInvalid.setStatus("current")
_SystemStatisticsDiffBfdRxParseErr_Type = Counter64
_SystemStatisticsDiffBfdRxParseErr_Object = MibScalar
systemStatisticsDiffBfdRxParseErr = _SystemStatisticsDiffBfdRxParseErr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 82),
    _SystemStatisticsDiffBfdRxParseErr_Type()
)
systemStatisticsDiffBfdRxParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdRxParseErr.setStatus("current")
_SystemStatisticsDiffRxArpRateLimitDrops_Type = Counter64
_SystemStatisticsDiffRxArpRateLimitDrops_Object = MibScalar
systemStatisticsDiffRxArpRateLimitDrops = _SystemStatisticsDiffRxArpRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 83),
    _SystemStatisticsDiffRxArpRateLimitDrops_Type()
)
systemStatisticsDiffRxArpRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxArpRateLimitDrops.setStatus("current")
_SystemStatisticsDiffRxArpNonLocalDrops_Type = Counter64
_SystemStatisticsDiffRxArpNonLocalDrops_Object = MibScalar
systemStatisticsDiffRxArpNonLocalDrops = _SystemStatisticsDiffRxArpNonLocalDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 84),
    _SystemStatisticsDiffRxArpNonLocalDrops_Type()
)
systemStatisticsDiffRxArpNonLocalDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxArpNonLocalDrops.setStatus("current")
_SystemStatisticsDiffRxArpReqs_Type = Counter64
_SystemStatisticsDiffRxArpReqs_Object = MibScalar
systemStatisticsDiffRxArpReqs = _SystemStatisticsDiffRxArpReqs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 85),
    _SystemStatisticsDiffRxArpReqs_Type()
)
systemStatisticsDiffRxArpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxArpReqs.setStatus("current")
_SystemStatisticsDiffRxArpReplies_Type = Counter64
_SystemStatisticsDiffRxArpReplies_Object = MibScalar
systemStatisticsDiffRxArpReplies = _SystemStatisticsDiffRxArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 86),
    _SystemStatisticsDiffRxArpReplies_Type()
)
systemStatisticsDiffRxArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxArpReplies.setStatus("current")
_SystemStatisticsDiffArpAddFail_Type = Counter64
_SystemStatisticsDiffArpAddFail_Object = MibScalar
systemStatisticsDiffArpAddFail = _SystemStatisticsDiffArpAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 87),
    _SystemStatisticsDiffArpAddFail_Type()
)
systemStatisticsDiffArpAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffArpAddFail.setStatus("current")
_SystemStatisticsDiffUnknownNhType_Type = Counter64
_SystemStatisticsDiffUnknownNhType_Object = MibScalar
systemStatisticsDiffUnknownNhType = _SystemStatisticsDiffUnknownNhType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 88),
    _SystemStatisticsDiffUnknownNhType_Type()
)
systemStatisticsDiffUnknownNhType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffUnknownNhType.setStatus("current")
_SystemStatisticsDiffBufAllocFails_Type = Counter64
_SystemStatisticsDiffBufAllocFails_Object = MibScalar
systemStatisticsDiffBufAllocFails = _SystemStatisticsDiffBufAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 89),
    _SystemStatisticsDiffBufAllocFails_Type()
)
systemStatisticsDiffBufAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBufAllocFails.setStatus("current")
_SystemStatisticsDiffEcmpDiscards_Type = Counter64
_SystemStatisticsDiffEcmpDiscards_Object = MibScalar
systemStatisticsDiffEcmpDiscards = _SystemStatisticsDiffEcmpDiscards_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 90),
    _SystemStatisticsDiffEcmpDiscards_Type()
)
systemStatisticsDiffEcmpDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffEcmpDiscards.setStatus("current")
_SystemStatisticsDiffAppRoutePolicyDiscards_Type = Counter64
_SystemStatisticsDiffAppRoutePolicyDiscards_Object = MibScalar
systemStatisticsDiffAppRoutePolicyDiscards = _SystemStatisticsDiffAppRoutePolicyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 91),
    _SystemStatisticsDiffAppRoutePolicyDiscards_Type()
)
systemStatisticsDiffAppRoutePolicyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffAppRoutePolicyDiscards.setStatus("current")
_SystemStatisticsDiffCbfDiscards_Type = Counter64
_SystemStatisticsDiffCbfDiscards_Object = MibScalar
systemStatisticsDiffCbfDiscards = _SystemStatisticsDiffCbfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 92),
    _SystemStatisticsDiffCbfDiscards_Type()
)
systemStatisticsDiffCbfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffCbfDiscards.setStatus("current")
_SystemStatisticsDiffFilterDrops_Type = Counter64
_SystemStatisticsDiffFilterDrops_Object = MibScalar
systemStatisticsDiffFilterDrops = _SystemStatisticsDiffFilterDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 93),
    _SystemStatisticsDiffFilterDrops_Type()
)
systemStatisticsDiffFilterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffFilterDrops.setStatus("current")
_SystemStatisticsDiffInvalidBackPtr_Type = Counter64
_SystemStatisticsDiffInvalidBackPtr_Object = MibScalar
systemStatisticsDiffInvalidBackPtr = _SystemStatisticsDiffInvalidBackPtr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 94),
    _SystemStatisticsDiffInvalidBackPtr_Type()
)
systemStatisticsDiffInvalidBackPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffInvalidBackPtr.setStatus("current")
_SystemStatisticsDiffTunnelLoopDrops_Type = Counter64
_SystemStatisticsDiffTunnelLoopDrops_Object = MibScalar
systemStatisticsDiffTunnelLoopDrops = _SystemStatisticsDiffTunnelLoopDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 95),
    _SystemStatisticsDiffTunnelLoopDrops_Type()
)
systemStatisticsDiffTunnelLoopDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTunnelLoopDrops.setStatus("current")
_SystemStatisticsDiffToCpuPolicerDrops_Type = Counter64
_SystemStatisticsDiffToCpuPolicerDrops_Object = MibScalar
systemStatisticsDiffToCpuPolicerDrops = _SystemStatisticsDiffToCpuPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 96),
    _SystemStatisticsDiffToCpuPolicerDrops_Type()
)
systemStatisticsDiffToCpuPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffToCpuPolicerDrops.setStatus("current")
_SystemStatisticsDiffMirrorDrops_Type = Counter64
_SystemStatisticsDiffMirrorDrops_Object = MibScalar
systemStatisticsDiffMirrorDrops = _SystemStatisticsDiffMirrorDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 97),
    _SystemStatisticsDiffMirrorDrops_Type()
)
systemStatisticsDiffMirrorDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffMirrorDrops.setStatus("current")
_SystemStatisticsDiffSplitHorizonDrops_Type = Counter64
_SystemStatisticsDiffSplitHorizonDrops_Object = MibScalar
systemStatisticsDiffSplitHorizonDrops = _SystemStatisticsDiffSplitHorizonDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 98),
    _SystemStatisticsDiffSplitHorizonDrops_Type()
)
systemStatisticsDiffSplitHorizonDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffSplitHorizonDrops.setStatus("current")
_SystemStatisticsDiffRxNoTunIf_Type = Counter64
_SystemStatisticsDiffRxNoTunIf_Object = MibScalar
systemStatisticsDiffRxNoTunIf = _SystemStatisticsDiffRxNoTunIf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 99),
    _SystemStatisticsDiffRxNoTunIf_Type()
)
systemStatisticsDiffRxNoTunIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxNoTunIf.setStatus("current")
_SystemStatisticsDiffTxPkts_Type = Counter64
_SystemStatisticsDiffTxPkts_Object = MibScalar
systemStatisticsDiffTxPkts = _SystemStatisticsDiffTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 100),
    _SystemStatisticsDiffTxPkts_Type()
)
systemStatisticsDiffTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxPkts.setStatus("current")
_SystemStatisticsDiffTxErrors_Type = Counter64
_SystemStatisticsDiffTxErrors_Object = MibScalar
systemStatisticsDiffTxErrors = _SystemStatisticsDiffTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 101),
    _SystemStatisticsDiffTxErrors_Type()
)
systemStatisticsDiffTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxErrors.setStatus("current")
_SystemStatisticsDiffTxBcast_Type = Counter64
_SystemStatisticsDiffTxBcast_Object = MibScalar
systemStatisticsDiffTxBcast = _SystemStatisticsDiffTxBcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 102),
    _SystemStatisticsDiffTxBcast_Type()
)
systemStatisticsDiffTxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxBcast.setStatus("current")
_SystemStatisticsDiffTxMcast_Type = Counter64
_SystemStatisticsDiffTxMcast_Object = MibScalar
systemStatisticsDiffTxMcast = _SystemStatisticsDiffTxMcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 103),
    _SystemStatisticsDiffTxMcast_Type()
)
systemStatisticsDiffTxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxMcast.setStatus("current")
_SystemStatisticsDiffPortDisabledTx_Type = Counter64
_SystemStatisticsDiffPortDisabledTx_Object = MibScalar
systemStatisticsDiffPortDisabledTx = _SystemStatisticsDiffPortDisabledTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 104),
    _SystemStatisticsDiffPortDisabledTx_Type()
)
systemStatisticsDiffPortDisabledTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffPortDisabledTx.setStatus("current")
_SystemStatisticsDiffIpDisabledTx_Type = Counter64
_SystemStatisticsDiffIpDisabledTx_Object = MibScalar
systemStatisticsDiffIpDisabledTx = _SystemStatisticsDiffIpDisabledTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 105),
    _SystemStatisticsDiffIpDisabledTx_Type()
)
systemStatisticsDiffIpDisabledTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpDisabledTx.setStatus("current")
_SystemStatisticsDiffTxFragmentNeeded_Type = Counter64
_SystemStatisticsDiffTxFragmentNeeded_Object = MibScalar
systemStatisticsDiffTxFragmentNeeded = _SystemStatisticsDiffTxFragmentNeeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 106),
    _SystemStatisticsDiffTxFragmentNeeded_Type()
)
systemStatisticsDiffTxFragmentNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxFragmentNeeded.setStatus("current")
_SystemStatisticsDiffTxMcastFragmentNeeded_Type = Counter64
_SystemStatisticsDiffTxMcastFragmentNeeded_Object = MibScalar
systemStatisticsDiffTxMcastFragmentNeeded = _SystemStatisticsDiffTxMcastFragmentNeeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 107),
    _SystemStatisticsDiffTxMcastFragmentNeeded_Type()
)
systemStatisticsDiffTxMcastFragmentNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxMcastFragmentNeeded.setStatus("current")
_SystemStatisticsDiffFragmentDfDrops_Type = Counter64
_SystemStatisticsDiffFragmentDfDrops_Object = MibScalar
systemStatisticsDiffFragmentDfDrops = _SystemStatisticsDiffFragmentDfDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 108),
    _SystemStatisticsDiffFragmentDfDrops_Type()
)
systemStatisticsDiffFragmentDfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffFragmentDfDrops.setStatus("current")
_SystemStatisticsDiffTxFragments_Type = Counter64
_SystemStatisticsDiffTxFragments_Object = MibScalar
systemStatisticsDiffTxFragments = _SystemStatisticsDiffTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 109),
    _SystemStatisticsDiffTxFragments_Type()
)
systemStatisticsDiffTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxFragments.setStatus("current")
_SystemStatisticsDiffTxFragmentDrops_Type = Counter64
_SystemStatisticsDiffTxFragmentDrops_Object = MibScalar
systemStatisticsDiffTxFragmentDrops = _SystemStatisticsDiffTxFragmentDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 110),
    _SystemStatisticsDiffTxFragmentDrops_Type()
)
systemStatisticsDiffTxFragmentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxFragmentDrops.setStatus("current")
_SystemStatisticsDiffTxFragmentFail_Type = Counter64
_SystemStatisticsDiffTxFragmentFail_Object = MibScalar
systemStatisticsDiffTxFragmentFail = _SystemStatisticsDiffTxFragmentFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 111),
    _SystemStatisticsDiffTxFragmentFail_Type()
)
systemStatisticsDiffTxFragmentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxFragmentFail.setStatus("current")
_SystemStatisticsDiffTxFragmentAllocFail_Type = Counter64
_SystemStatisticsDiffTxFragmentAllocFail_Object = MibScalar
systemStatisticsDiffTxFragmentAllocFail = _SystemStatisticsDiffTxFragmentAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 112),
    _SystemStatisticsDiffTxFragmentAllocFail_Type()
)
systemStatisticsDiffTxFragmentAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxFragmentAllocFail.setStatus("current")
_SystemStatisticsDiffTunnelPmtuLowered_Type = Counter64
_SystemStatisticsDiffTunnelPmtuLowered_Object = MibScalar
systemStatisticsDiffTunnelPmtuLowered = _SystemStatisticsDiffTunnelPmtuLowered_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 113),
    _SystemStatisticsDiffTunnelPmtuLowered_Type()
)
systemStatisticsDiffTunnelPmtuLowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTunnelPmtuLowered.setStatus("current")
_SystemStatisticsDiffTxGrePkts_Type = Counter64
_SystemStatisticsDiffTxGrePkts_Object = MibScalar
systemStatisticsDiffTxGrePkts = _SystemStatisticsDiffTxGrePkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 114),
    _SystemStatisticsDiffTxGrePkts_Type()
)
systemStatisticsDiffTxGrePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxGrePkts.setStatus("current")
_SystemStatisticsDiffTxGreDrops_Type = Counter64
_SystemStatisticsDiffTxGreDrops_Object = MibScalar
systemStatisticsDiffTxGreDrops = _SystemStatisticsDiffTxGreDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 115),
    _SystemStatisticsDiffTxGreDrops_Type()
)
systemStatisticsDiffTxGreDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxGreDrops.setStatus("current")
_SystemStatisticsDiffTxGrePolicerDrops_Type = Counter64
_SystemStatisticsDiffTxGrePolicerDrops_Object = MibScalar
systemStatisticsDiffTxGrePolicerDrops = _SystemStatisticsDiffTxGrePolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 116),
    _SystemStatisticsDiffTxGrePolicerDrops_Type()
)
systemStatisticsDiffTxGrePolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxGrePolicerDrops.setStatus("current")
_SystemStatisticsDiffTxGreEncap_Type = Counter64
_SystemStatisticsDiffTxGreEncap_Object = MibScalar
systemStatisticsDiffTxGreEncap = _SystemStatisticsDiffTxGreEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 117),
    _SystemStatisticsDiffTxGreEncap_Type()
)
systemStatisticsDiffTxGreEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxGreEncap.setStatus("current")
_SystemStatisticsDiffTxIpsecPkts_Type = Counter64
_SystemStatisticsDiffTxIpsecPkts_Object = MibScalar
systemStatisticsDiffTxIpsecPkts = _SystemStatisticsDiffTxIpsecPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 118),
    _SystemStatisticsDiffTxIpsecPkts_Type()
)
systemStatisticsDiffTxIpsecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIpsecPkts.setStatus("current")
_SystemStatisticsDiffTxIpsecMcastPkts_Type = Counter64
_SystemStatisticsDiffTxIpsecMcastPkts_Object = MibScalar
systemStatisticsDiffTxIpsecMcastPkts = _SystemStatisticsDiffTxIpsecMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 119),
    _SystemStatisticsDiffTxIpsecMcastPkts_Type()
)
systemStatisticsDiffTxIpsecMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIpsecMcastPkts.setStatus("current")
_SystemStatisticsDiffTxIp6IpsecDrops_Type = Counter64
_SystemStatisticsDiffTxIp6IpsecDrops_Object = MibScalar
systemStatisticsDiffTxIp6IpsecDrops = _SystemStatisticsDiffTxIp6IpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 120),
    _SystemStatisticsDiffTxIp6IpsecDrops_Type()
)
systemStatisticsDiffTxIp6IpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIp6IpsecDrops.setStatus("current")
_SystemStatisticsDiffTxNoOutSaIpsecDrops_Type = Counter64
_SystemStatisticsDiffTxNoOutSaIpsecDrops_Object = MibScalar
systemStatisticsDiffTxNoOutSaIpsecDrops = _SystemStatisticsDiffTxNoOutSaIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 121),
    _SystemStatisticsDiffTxNoOutSaIpsecDrops_Type()
)
systemStatisticsDiffTxNoOutSaIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxNoOutSaIpsecDrops.setStatus("current")
_SystemStatisticsDiffTxNoTunnIpsecDrops_Type = Counter64
_SystemStatisticsDiffTxNoTunnIpsecDrops_Object = MibScalar
systemStatisticsDiffTxNoTunnIpsecDrops = _SystemStatisticsDiffTxNoTunnIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 122),
    _SystemStatisticsDiffTxNoTunnIpsecDrops_Type()
)
systemStatisticsDiffTxNoTunnIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxNoTunnIpsecDrops.setStatus("current")
_SystemStatisticsDiffTxIpsecPolicerDrops_Type = Counter64
_SystemStatisticsDiffTxIpsecPolicerDrops_Object = MibScalar
systemStatisticsDiffTxIpsecPolicerDrops = _SystemStatisticsDiffTxIpsecPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 123),
    _SystemStatisticsDiffTxIpsecPolicerDrops_Type()
)
systemStatisticsDiffTxIpsecPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIpsecPolicerDrops.setStatus("current")
_SystemStatisticsDiffTxIpsecEncap_Type = Counter64
_SystemStatisticsDiffTxIpsecEncap_Object = MibScalar
systemStatisticsDiffTxIpsecEncap = _SystemStatisticsDiffTxIpsecEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 124),
    _SystemStatisticsDiffTxIpsecEncap_Type()
)
systemStatisticsDiffTxIpsecEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIpsecEncap.setStatus("current")
_SystemStatisticsDiffTxIpsecMcastEncap_Type = Counter64
_SystemStatisticsDiffTxIpsecMcastEncap_Object = MibScalar
systemStatisticsDiffTxIpsecMcastEncap = _SystemStatisticsDiffTxIpsecMcastEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 125),
    _SystemStatisticsDiffTxIpsecMcastEncap_Type()
)
systemStatisticsDiffTxIpsecMcastEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIpsecMcastEncap.setStatus("current")
_SystemStatisticsDiffTxPreIpsecPkts_Type = Counter64
_SystemStatisticsDiffTxPreIpsecPkts_Object = MibScalar
systemStatisticsDiffTxPreIpsecPkts = _SystemStatisticsDiffTxPreIpsecPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 126),
    _SystemStatisticsDiffTxPreIpsecPkts_Type()
)
systemStatisticsDiffTxPreIpsecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxPreIpsecPkts.setStatus("current")
_SystemStatisticsDiffTxNoOutSaPreIpsecDrops_Type = Counter64
_SystemStatisticsDiffTxNoOutSaPreIpsecDrops_Object = MibScalar
systemStatisticsDiffTxNoOutSaPreIpsecDrops = _SystemStatisticsDiffTxNoOutSaPreIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 127),
    _SystemStatisticsDiffTxNoOutSaPreIpsecDrops_Type()
)
systemStatisticsDiffTxNoOutSaPreIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxNoOutSaPreIpsecDrops.setStatus("current")
_SystemStatisticsDiffTxNoTunnPreIpsecDrops_Type = Counter64
_SystemStatisticsDiffTxNoTunnPreIpsecDrops_Object = MibScalar
systemStatisticsDiffTxNoTunnPreIpsecDrops = _SystemStatisticsDiffTxNoTunnPreIpsecDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 128),
    _SystemStatisticsDiffTxNoTunnPreIpsecDrops_Type()
)
systemStatisticsDiffTxNoTunnPreIpsecDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxNoTunnPreIpsecDrops.setStatus("current")
_SystemStatisticsDiffOpensslAesEncrypt_Type = Counter64
_SystemStatisticsDiffOpensslAesEncrypt_Object = MibScalar
systemStatisticsDiffOpensslAesEncrypt = _SystemStatisticsDiffOpensslAesEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 129),
    _SystemStatisticsDiffOpensslAesEncrypt_Type()
)
systemStatisticsDiffOpensslAesEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffOpensslAesEncrypt.setStatus("current")
_SystemStatisticsDiffTxPreIpsecPolicerDrops_Type = Counter64
_SystemStatisticsDiffTxPreIpsecPolicerDrops_Object = MibScalar
systemStatisticsDiffTxPreIpsecPolicerDrops = _SystemStatisticsDiffTxPreIpsecPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 130),
    _SystemStatisticsDiffTxPreIpsecPolicerDrops_Type()
)
systemStatisticsDiffTxPreIpsecPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxPreIpsecPolicerDrops.setStatus("current")
_SystemStatisticsDiffTxPreIpsecEncap_Type = Counter64
_SystemStatisticsDiffTxPreIpsecEncap_Object = MibScalar
systemStatisticsDiffTxPreIpsecEncap = _SystemStatisticsDiffTxPreIpsecEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 131),
    _SystemStatisticsDiffTxPreIpsecEncap_Type()
)
systemStatisticsDiffTxPreIpsecEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxPreIpsecEncap.setStatus("current")
_SystemStatisticsDiffTxArpReplies_Type = Counter64
_SystemStatisticsDiffTxArpReplies_Object = MibScalar
systemStatisticsDiffTxArpReplies = _SystemStatisticsDiffTxArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 132),
    _SystemStatisticsDiffTxArpReplies_Type()
)
systemStatisticsDiffTxArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxArpReplies.setStatus("current")
_SystemStatisticsDiffTxArpReqs_Type = Counter64
_SystemStatisticsDiffTxArpReqs_Object = MibScalar
systemStatisticsDiffTxArpReqs = _SystemStatisticsDiffTxArpReqs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 133),
    _SystemStatisticsDiffTxArpReqs_Type()
)
systemStatisticsDiffTxArpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxArpReqs.setStatus("current")
_SystemStatisticsDiffTxArpReqFail_Type = Counter64
_SystemStatisticsDiffTxArpReqFail_Object = MibScalar
systemStatisticsDiffTxArpReqFail = _SystemStatisticsDiffTxArpReqFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 134),
    _SystemStatisticsDiffTxArpReqFail_Type()
)
systemStatisticsDiffTxArpReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxArpReqFail.setStatus("current")
_SystemStatisticsDiffTxNoArpDrop_Type = Counter64
_SystemStatisticsDiffTxNoArpDrop_Object = MibScalar
systemStatisticsDiffTxNoArpDrop = _SystemStatisticsDiffTxNoArpDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 135),
    _SystemStatisticsDiffTxNoArpDrop_Type()
)
systemStatisticsDiffTxNoArpDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxNoArpDrop.setStatus("current")
_SystemStatisticsDiffTxArpRateLimitDrops_Type = Counter64
_SystemStatisticsDiffTxArpRateLimitDrops_Object = MibScalar
systemStatisticsDiffTxArpRateLimitDrops = _SystemStatisticsDiffTxArpRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 136),
    _SystemStatisticsDiffTxArpRateLimitDrops_Type()
)
systemStatisticsDiffTxArpRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxArpRateLimitDrops.setStatus("current")
_SystemStatisticsDiffTxIcmpPolicerDrops_Type = Counter64
_SystemStatisticsDiffTxIcmpPolicerDrops_Object = MibScalar
systemStatisticsDiffTxIcmpPolicerDrops = _SystemStatisticsDiffTxIcmpPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 137),
    _SystemStatisticsDiffTxIcmpPolicerDrops_Type()
)
systemStatisticsDiffTxIcmpPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpPolicerDrops.setStatus("current")
_SystemStatisticsDiffTxIcmpMirroredDrops_Type = Counter64
_SystemStatisticsDiffTxIcmpMirroredDrops_Object = MibScalar
systemStatisticsDiffTxIcmpMirroredDrops = _SystemStatisticsDiffTxIcmpMirroredDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 138),
    _SystemStatisticsDiffTxIcmpMirroredDrops_Type()
)
systemStatisticsDiffTxIcmpMirroredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpMirroredDrops.setStatus("current")
_SystemStatisticsDiffBfdTxFail_Type = Counter64
_SystemStatisticsDiffBfdTxFail_Object = MibScalar
systemStatisticsDiffBfdTxFail = _SystemStatisticsDiffBfdTxFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 139),
    _SystemStatisticsDiffBfdTxFail_Type()
)
systemStatisticsDiffBfdTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdTxFail.setStatus("current")
_SystemStatisticsDiffBfdAllocFail_Type = Counter64
_SystemStatisticsDiffBfdAllocFail_Object = MibScalar
systemStatisticsDiffBfdAllocFail = _SystemStatisticsDiffBfdAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 140),
    _SystemStatisticsDiffBfdAllocFail_Type()
)
systemStatisticsDiffBfdAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdAllocFail.setStatus("current")
_SystemStatisticsDiffBfdTimerAddFail_Type = Counter64
_SystemStatisticsDiffBfdTimerAddFail_Object = MibScalar
systemStatisticsDiffBfdTimerAddFail = _SystemStatisticsDiffBfdTimerAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 141),
    _SystemStatisticsDiffBfdTimerAddFail_Type()
)
systemStatisticsDiffBfdTimerAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdTimerAddFail.setStatus("current")
_SystemStatisticsDiffBfdTxPkts_Type = Counter64
_SystemStatisticsDiffBfdTxPkts_Object = MibScalar
systemStatisticsDiffBfdTxPkts = _SystemStatisticsDiffBfdTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 142),
    _SystemStatisticsDiffBfdTxPkts_Type()
)
systemStatisticsDiffBfdTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdTxPkts.setStatus("current")
_SystemStatisticsDiffBfdRxPkts_Type = Counter64
_SystemStatisticsDiffBfdRxPkts_Object = MibScalar
systemStatisticsDiffBfdRxPkts = _SystemStatisticsDiffBfdRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 143),
    _SystemStatisticsDiffBfdRxPkts_Type()
)
systemStatisticsDiffBfdRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdRxPkts.setStatus("current")
_SystemStatisticsDiffBfdRecDown_Type = Counter64
_SystemStatisticsDiffBfdRecDown_Object = MibScalar
systemStatisticsDiffBfdRecDown = _SystemStatisticsDiffBfdRecDown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 144),
    _SystemStatisticsDiffBfdRecDown_Type()
)
systemStatisticsDiffBfdRecDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdRecDown.setStatus("current")
_SystemStatisticsDiffBfdRecInvalid_Type = Counter64
_SystemStatisticsDiffBfdRecInvalid_Object = MibScalar
systemStatisticsDiffBfdRecInvalid = _SystemStatisticsDiffBfdRecInvalid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 145),
    _SystemStatisticsDiffBfdRecInvalid_Type()
)
systemStatisticsDiffBfdRecInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdRecInvalid.setStatus("current")
_SystemStatisticsDiffBfdLkupFail_Type = Counter64
_SystemStatisticsDiffBfdLkupFail_Object = MibScalar
systemStatisticsDiffBfdLkupFail = _SystemStatisticsDiffBfdLkupFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 146),
    _SystemStatisticsDiffBfdLkupFail_Type()
)
systemStatisticsDiffBfdLkupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdLkupFail.setStatus("current")
_SystemStatisticsDiffRxIcmpEchoRequests_Type = Counter64
_SystemStatisticsDiffRxIcmpEchoRequests_Object = MibScalar
systemStatisticsDiffRxIcmpEchoRequests = _SystemStatisticsDiffRxIcmpEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 147),
    _SystemStatisticsDiffRxIcmpEchoRequests_Type()
)
systemStatisticsDiffRxIcmpEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpEchoRequests.setStatus("current")
_SystemStatisticsDiffRxIcmpEchoReplies_Type = Counter64
_SystemStatisticsDiffRxIcmpEchoReplies_Object = MibScalar
systemStatisticsDiffRxIcmpEchoReplies = _SystemStatisticsDiffRxIcmpEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 148),
    _SystemStatisticsDiffRxIcmpEchoReplies_Type()
)
systemStatisticsDiffRxIcmpEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpEchoReplies.setStatus("current")
_SystemStatisticsDiffRxIcmpNetworkUnreach_Type = Counter64
_SystemStatisticsDiffRxIcmpNetworkUnreach_Object = MibScalar
systemStatisticsDiffRxIcmpNetworkUnreach = _SystemStatisticsDiffRxIcmpNetworkUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 149),
    _SystemStatisticsDiffRxIcmpNetworkUnreach_Type()
)
systemStatisticsDiffRxIcmpNetworkUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpNetworkUnreach.setStatus("current")
_SystemStatisticsDiffRxIcmpHostUnreach_Type = Counter64
_SystemStatisticsDiffRxIcmpHostUnreach_Object = MibScalar
systemStatisticsDiffRxIcmpHostUnreach = _SystemStatisticsDiffRxIcmpHostUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 150),
    _SystemStatisticsDiffRxIcmpHostUnreach_Type()
)
systemStatisticsDiffRxIcmpHostUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpHostUnreach.setStatus("current")
_SystemStatisticsDiffRxIcmpPortUnreach_Type = Counter64
_SystemStatisticsDiffRxIcmpPortUnreach_Object = MibScalar
systemStatisticsDiffRxIcmpPortUnreach = _SystemStatisticsDiffRxIcmpPortUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 151),
    _SystemStatisticsDiffRxIcmpPortUnreach_Type()
)
systemStatisticsDiffRxIcmpPortUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpPortUnreach.setStatus("current")
_SystemStatisticsDiffRxIcmpProtocolUnreach_Type = Counter64
_SystemStatisticsDiffRxIcmpProtocolUnreach_Object = MibScalar
systemStatisticsDiffRxIcmpProtocolUnreach = _SystemStatisticsDiffRxIcmpProtocolUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 152),
    _SystemStatisticsDiffRxIcmpProtocolUnreach_Type()
)
systemStatisticsDiffRxIcmpProtocolUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpProtocolUnreach.setStatus("current")
_SystemStatisticsDiffRxIcmpFragmentRequired_Type = Counter64
_SystemStatisticsDiffRxIcmpFragmentRequired_Object = MibScalar
systemStatisticsDiffRxIcmpFragmentRequired = _SystemStatisticsDiffRxIcmpFragmentRequired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 153),
    _SystemStatisticsDiffRxIcmpFragmentRequired_Type()
)
systemStatisticsDiffRxIcmpFragmentRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpFragmentRequired.setStatus("current")
_SystemStatisticsDiffRxIcmpDstUnreachOther_Type = Counter64
_SystemStatisticsDiffRxIcmpDstUnreachOther_Object = MibScalar
systemStatisticsDiffRxIcmpDstUnreachOther = _SystemStatisticsDiffRxIcmpDstUnreachOther_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 154),
    _SystemStatisticsDiffRxIcmpDstUnreachOther_Type()
)
systemStatisticsDiffRxIcmpDstUnreachOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpDstUnreachOther.setStatus("current")
_SystemStatisticsDiffRxIcmpTtlExpired_Type = Counter64
_SystemStatisticsDiffRxIcmpTtlExpired_Object = MibScalar
systemStatisticsDiffRxIcmpTtlExpired = _SystemStatisticsDiffRxIcmpTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 155),
    _SystemStatisticsDiffRxIcmpTtlExpired_Type()
)
systemStatisticsDiffRxIcmpTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpTtlExpired.setStatus("current")
_SystemStatisticsDiffRxIcmpRedirect_Type = Counter64
_SystemStatisticsDiffRxIcmpRedirect_Object = MibScalar
systemStatisticsDiffRxIcmpRedirect = _SystemStatisticsDiffRxIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 156),
    _SystemStatisticsDiffRxIcmpRedirect_Type()
)
systemStatisticsDiffRxIcmpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpRedirect.setStatus("current")
_SystemStatisticsDiffRxIcmpSrcQuench_Type = Counter64
_SystemStatisticsDiffRxIcmpSrcQuench_Object = MibScalar
systemStatisticsDiffRxIcmpSrcQuench = _SystemStatisticsDiffRxIcmpSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 157),
    _SystemStatisticsDiffRxIcmpSrcQuench_Type()
)
systemStatisticsDiffRxIcmpSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpSrcQuench.setStatus("current")
_SystemStatisticsDiffRxIcmpBadIpHdr_Type = Counter64
_SystemStatisticsDiffRxIcmpBadIpHdr_Object = MibScalar
systemStatisticsDiffRxIcmpBadIpHdr = _SystemStatisticsDiffRxIcmpBadIpHdr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 158),
    _SystemStatisticsDiffRxIcmpBadIpHdr_Type()
)
systemStatisticsDiffRxIcmpBadIpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpBadIpHdr.setStatus("current")
_SystemStatisticsDiffRxIcmpOtherTypes_Type = Counter64
_SystemStatisticsDiffRxIcmpOtherTypes_Object = MibScalar
systemStatisticsDiffRxIcmpOtherTypes = _SystemStatisticsDiffRxIcmpOtherTypes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 159),
    _SystemStatisticsDiffRxIcmpOtherTypes_Type()
)
systemStatisticsDiffRxIcmpOtherTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxIcmpOtherTypes.setStatus("current")
_SystemStatisticsDiffTxIcmpEchoRequests_Type = Counter64
_SystemStatisticsDiffTxIcmpEchoRequests_Object = MibScalar
systemStatisticsDiffTxIcmpEchoRequests = _SystemStatisticsDiffTxIcmpEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 160),
    _SystemStatisticsDiffTxIcmpEchoRequests_Type()
)
systemStatisticsDiffTxIcmpEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpEchoRequests.setStatus("current")
_SystemStatisticsDiffTxIcmpEchoReplies_Type = Counter64
_SystemStatisticsDiffTxIcmpEchoReplies_Object = MibScalar
systemStatisticsDiffTxIcmpEchoReplies = _SystemStatisticsDiffTxIcmpEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 161),
    _SystemStatisticsDiffTxIcmpEchoReplies_Type()
)
systemStatisticsDiffTxIcmpEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpEchoReplies.setStatus("current")
_SystemStatisticsDiffTxIcmpNetworkUnreach_Type = Counter64
_SystemStatisticsDiffTxIcmpNetworkUnreach_Object = MibScalar
systemStatisticsDiffTxIcmpNetworkUnreach = _SystemStatisticsDiffTxIcmpNetworkUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 162),
    _SystemStatisticsDiffTxIcmpNetworkUnreach_Type()
)
systemStatisticsDiffTxIcmpNetworkUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpNetworkUnreach.setStatus("current")
_SystemStatisticsDiffTxIcmpHostUnreach_Type = Counter64
_SystemStatisticsDiffTxIcmpHostUnreach_Object = MibScalar
systemStatisticsDiffTxIcmpHostUnreach = _SystemStatisticsDiffTxIcmpHostUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 163),
    _SystemStatisticsDiffTxIcmpHostUnreach_Type()
)
systemStatisticsDiffTxIcmpHostUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpHostUnreach.setStatus("current")
_SystemStatisticsDiffTxIcmpPortUnreach_Type = Counter64
_SystemStatisticsDiffTxIcmpPortUnreach_Object = MibScalar
systemStatisticsDiffTxIcmpPortUnreach = _SystemStatisticsDiffTxIcmpPortUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 164),
    _SystemStatisticsDiffTxIcmpPortUnreach_Type()
)
systemStatisticsDiffTxIcmpPortUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpPortUnreach.setStatus("current")
_SystemStatisticsDiffTxIcmpProtocolUnreach_Type = Counter64
_SystemStatisticsDiffTxIcmpProtocolUnreach_Object = MibScalar
systemStatisticsDiffTxIcmpProtocolUnreach = _SystemStatisticsDiffTxIcmpProtocolUnreach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 165),
    _SystemStatisticsDiffTxIcmpProtocolUnreach_Type()
)
systemStatisticsDiffTxIcmpProtocolUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpProtocolUnreach.setStatus("current")
_SystemStatisticsDiffTxIcmpFragmentRequired_Type = Counter64
_SystemStatisticsDiffTxIcmpFragmentRequired_Object = MibScalar
systemStatisticsDiffTxIcmpFragmentRequired = _SystemStatisticsDiffTxIcmpFragmentRequired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 166),
    _SystemStatisticsDiffTxIcmpFragmentRequired_Type()
)
systemStatisticsDiffTxIcmpFragmentRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpFragmentRequired.setStatus("current")
_SystemStatisticsDiffTxIcmpDstUnreachOther_Type = Counter64
_SystemStatisticsDiffTxIcmpDstUnreachOther_Object = MibScalar
systemStatisticsDiffTxIcmpDstUnreachOther = _SystemStatisticsDiffTxIcmpDstUnreachOther_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 167),
    _SystemStatisticsDiffTxIcmpDstUnreachOther_Type()
)
systemStatisticsDiffTxIcmpDstUnreachOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpDstUnreachOther.setStatus("current")
_SystemStatisticsDiffTxIcmpTtlExpired_Type = Counter64
_SystemStatisticsDiffTxIcmpTtlExpired_Object = MibScalar
systemStatisticsDiffTxIcmpTtlExpired = _SystemStatisticsDiffTxIcmpTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 168),
    _SystemStatisticsDiffTxIcmpTtlExpired_Type()
)
systemStatisticsDiffTxIcmpTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpTtlExpired.setStatus("current")
_SystemStatisticsDiffTxIcmpRedirect_Type = Counter64
_SystemStatisticsDiffTxIcmpRedirect_Object = MibScalar
systemStatisticsDiffTxIcmpRedirect = _SystemStatisticsDiffTxIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 169),
    _SystemStatisticsDiffTxIcmpRedirect_Type()
)
systemStatisticsDiffTxIcmpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpRedirect.setStatus("current")
_SystemStatisticsDiffTxIcmpSrcQuench_Type = Counter64
_SystemStatisticsDiffTxIcmpSrcQuench_Object = MibScalar
systemStatisticsDiffTxIcmpSrcQuench = _SystemStatisticsDiffTxIcmpSrcQuench_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 170),
    _SystemStatisticsDiffTxIcmpSrcQuench_Type()
)
systemStatisticsDiffTxIcmpSrcQuench.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpSrcQuench.setStatus("current")
_SystemStatisticsDiffTxIcmpBadIpHdr_Type = Counter64
_SystemStatisticsDiffTxIcmpBadIpHdr_Object = MibScalar
systemStatisticsDiffTxIcmpBadIpHdr = _SystemStatisticsDiffTxIcmpBadIpHdr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 171),
    _SystemStatisticsDiffTxIcmpBadIpHdr_Type()
)
systemStatisticsDiffTxIcmpBadIpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpBadIpHdr.setStatus("current")
_SystemStatisticsDiffTxIcmpOtherTypes_Type = Counter64
_SystemStatisticsDiffTxIcmpOtherTypes_Object = MibScalar
systemStatisticsDiffTxIcmpOtherTypes = _SystemStatisticsDiffTxIcmpOtherTypes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 172),
    _SystemStatisticsDiffTxIcmpOtherTypes_Type()
)
systemStatisticsDiffTxIcmpOtherTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxIcmpOtherTypes.setStatus("current")
_SystemStatisticsDiffGreKaTxPkts_Type = Counter64
_SystemStatisticsDiffGreKaTxPkts_Object = MibScalar
systemStatisticsDiffGreKaTxPkts = _SystemStatisticsDiffGreKaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 174),
    _SystemStatisticsDiffGreKaTxPkts_Type()
)
systemStatisticsDiffGreKaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaTxPkts.setStatus("current")
_SystemStatisticsDiffGreKaRxPkts_Type = Counter64
_SystemStatisticsDiffGreKaRxPkts_Object = MibScalar
systemStatisticsDiffGreKaRxPkts = _SystemStatisticsDiffGreKaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 175),
    _SystemStatisticsDiffGreKaRxPkts_Type()
)
systemStatisticsDiffGreKaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaRxPkts.setStatus("current")
_SystemStatisticsDiffGreKaTxIpv4OptionsDrop_Type = Counter64
_SystemStatisticsDiffGreKaTxIpv4OptionsDrop_Object = MibScalar
systemStatisticsDiffGreKaTxIpv4OptionsDrop = _SystemStatisticsDiffGreKaTxIpv4OptionsDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 176),
    _SystemStatisticsDiffGreKaTxIpv4OptionsDrop_Type()
)
systemStatisticsDiffGreKaTxIpv4OptionsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaTxIpv4OptionsDrop.setStatus("current")
_SystemStatisticsDiffGreKaTxNonIp_Type = Counter64
_SystemStatisticsDiffGreKaTxNonIp_Object = MibScalar
systemStatisticsDiffGreKaTxNonIp = _SystemStatisticsDiffGreKaTxNonIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 177),
    _SystemStatisticsDiffGreKaTxNonIp_Type()
)
systemStatisticsDiffGreKaTxNonIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaTxNonIp.setStatus("current")
_SystemStatisticsDiffGreKaTxParseErr_Type = Counter64
_SystemStatisticsDiffGreKaTxParseErr_Object = MibScalar
systemStatisticsDiffGreKaTxParseErr = _SystemStatisticsDiffGreKaTxParseErr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 178),
    _SystemStatisticsDiffGreKaTxParseErr_Type()
)
systemStatisticsDiffGreKaTxParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaTxParseErr.setStatus("current")
_SystemStatisticsDiffGreKaTxRecordChanged_Type = Counter64
_SystemStatisticsDiffGreKaTxRecordChanged_Object = MibScalar
systemStatisticsDiffGreKaTxRecordChanged = _SystemStatisticsDiffGreKaTxRecordChanged_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 179),
    _SystemStatisticsDiffGreKaTxRecordChanged_Type()
)
systemStatisticsDiffGreKaTxRecordChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaTxRecordChanged.setStatus("current")
_SystemStatisticsDiffGreKaTxFail_Type = Counter64
_SystemStatisticsDiffGreKaTxFail_Object = MibScalar
systemStatisticsDiffGreKaTxFail = _SystemStatisticsDiffGreKaTxFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 180),
    _SystemStatisticsDiffGreKaTxFail_Type()
)
systemStatisticsDiffGreKaTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaTxFail.setStatus("current")
_SystemStatisticsDiffGreKaAllocFail_Type = Counter64
_SystemStatisticsDiffGreKaAllocFail_Object = MibScalar
systemStatisticsDiffGreKaAllocFail = _SystemStatisticsDiffGreKaAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 181),
    _SystemStatisticsDiffGreKaAllocFail_Type()
)
systemStatisticsDiffGreKaAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaAllocFail.setStatus("current")
_SystemStatisticsDiffGreKaTimerAddFail_Type = Counter64
_SystemStatisticsDiffGreKaTimerAddFail_Object = MibScalar
systemStatisticsDiffGreKaTimerAddFail = _SystemStatisticsDiffGreKaTimerAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 182),
    _SystemStatisticsDiffGreKaTimerAddFail_Type()
)
systemStatisticsDiffGreKaTimerAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaTimerAddFail.setStatus("current")
_SystemStatisticsDiffGreKaRxNonIp_Type = Counter64
_SystemStatisticsDiffGreKaRxNonIp_Object = MibScalar
systemStatisticsDiffGreKaRxNonIp = _SystemStatisticsDiffGreKaRxNonIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 183),
    _SystemStatisticsDiffGreKaRxNonIp_Type()
)
systemStatisticsDiffGreKaRxNonIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaRxNonIp.setStatus("current")
_SystemStatisticsDiffGreKaRxRecInvalid_Type = Counter64
_SystemStatisticsDiffGreKaRxRecInvalid_Object = MibScalar
systemStatisticsDiffGreKaRxRecInvalid = _SystemStatisticsDiffGreKaRxRecInvalid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 184),
    _SystemStatisticsDiffGreKaRxRecInvalid_Type()
)
systemStatisticsDiffGreKaRxRecInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffGreKaRxRecInvalid.setStatus("current")
_SystemStatisticsDiffDot1xRxPkts_Type = Counter64
_SystemStatisticsDiffDot1xRxPkts_Object = MibScalar
systemStatisticsDiffDot1xRxPkts = _SystemStatisticsDiffDot1xRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 185),
    _SystemStatisticsDiffDot1xRxPkts_Type()
)
systemStatisticsDiffDot1xRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDot1xRxPkts.setStatus("current")
_SystemStatisticsDiffDot1xTxPkts_Type = Counter64
_SystemStatisticsDiffDot1xTxPkts_Object = MibScalar
systemStatisticsDiffDot1xTxPkts = _SystemStatisticsDiffDot1xTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 186),
    _SystemStatisticsDiffDot1xTxPkts_Type()
)
systemStatisticsDiffDot1xTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDot1xTxPkts.setStatus("current")
_SystemStatisticsDiffDot1xRxDrops_Type = Counter64
_SystemStatisticsDiffDot1xRxDrops_Object = MibScalar
systemStatisticsDiffDot1xRxDrops = _SystemStatisticsDiffDot1xRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 187),
    _SystemStatisticsDiffDot1xRxDrops_Type()
)
systemStatisticsDiffDot1xRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDot1xRxDrops.setStatus("current")
_SystemStatisticsDiffDot1xTxDrops_Type = Counter64
_SystemStatisticsDiffDot1xTxDrops_Object = MibScalar
systemStatisticsDiffDot1xTxDrops = _SystemStatisticsDiffDot1xTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 188),
    _SystemStatisticsDiffDot1xTxDrops_Type()
)
systemStatisticsDiffDot1xTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDot1xTxDrops.setStatus("current")
_SystemStatisticsDiffDot1xVlanIfNotFoundDrops_Type = Counter64
_SystemStatisticsDiffDot1xVlanIfNotFoundDrops_Object = MibScalar
systemStatisticsDiffDot1xVlanIfNotFoundDrops = _SystemStatisticsDiffDot1xVlanIfNotFoundDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 189),
    _SystemStatisticsDiffDot1xVlanIfNotFoundDrops_Type()
)
systemStatisticsDiffDot1xVlanIfNotFoundDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDot1xVlanIfNotFoundDrops.setStatus("current")
_SystemStatisticsDiffDot1xMacLearnDrops_Type = Counter64
_SystemStatisticsDiffDot1xMacLearnDrops_Object = MibScalar
systemStatisticsDiffDot1xMacLearnDrops = _SystemStatisticsDiffDot1xMacLearnDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 190),
    _SystemStatisticsDiffDot1xMacLearnDrops_Type()
)
systemStatisticsDiffDot1xMacLearnDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDot1xMacLearnDrops.setStatus("current")
_SystemStatisticsDiffRxPolicerRemark_Type = Counter64
_SystemStatisticsDiffRxPolicerRemark_Object = MibScalar
systemStatisticsDiffRxPolicerRemark = _SystemStatisticsDiffRxPolicerRemark_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 191),
    _SystemStatisticsDiffRxPolicerRemark_Type()
)
systemStatisticsDiffRxPolicerRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxPolicerRemark.setStatus("current")
_SystemStatisticsDiffBfdTxOctets_Type = Counter64
_SystemStatisticsDiffBfdTxOctets_Object = MibScalar
systemStatisticsDiffBfdTxOctets = _SystemStatisticsDiffBfdTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 192),
    _SystemStatisticsDiffBfdTxOctets_Type()
)
systemStatisticsDiffBfdTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdTxOctets.setStatus("current")
_SystemStatisticsDiffBfdRxOctets_Type = Counter64
_SystemStatisticsDiffBfdRxOctets_Object = MibScalar
systemStatisticsDiffBfdRxOctets = _SystemStatisticsDiffBfdRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 193),
    _SystemStatisticsDiffBfdRxOctets_Type()
)
systemStatisticsDiffBfdRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdRxOctets.setStatus("current")
_SystemStatisticsDiffBfdPmtuTxPkts_Type = Counter64
_SystemStatisticsDiffBfdPmtuTxPkts_Object = MibScalar
systemStatisticsDiffBfdPmtuTxPkts = _SystemStatisticsDiffBfdPmtuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 194),
    _SystemStatisticsDiffBfdPmtuTxPkts_Type()
)
systemStatisticsDiffBfdPmtuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdPmtuTxPkts.setStatus("current")
_SystemStatisticsDiffBfdPmtuRxPkts_Type = Counter64
_SystemStatisticsDiffBfdPmtuRxPkts_Object = MibScalar
systemStatisticsDiffBfdPmtuRxPkts = _SystemStatisticsDiffBfdPmtuRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 195),
    _SystemStatisticsDiffBfdPmtuRxPkts_Type()
)
systemStatisticsDiffBfdPmtuRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdPmtuRxPkts.setStatus("current")
_SystemStatisticsDiffBfdPmtuTxOctets_Type = Counter64
_SystemStatisticsDiffBfdPmtuTxOctets_Object = MibScalar
systemStatisticsDiffBfdPmtuTxOctets = _SystemStatisticsDiffBfdPmtuTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 196),
    _SystemStatisticsDiffBfdPmtuTxOctets_Type()
)
systemStatisticsDiffBfdPmtuTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdPmtuTxOctets.setStatus("current")
_SystemStatisticsDiffBfdPmtuRxOctets_Type = Counter64
_SystemStatisticsDiffBfdPmtuRxOctets_Object = MibScalar
systemStatisticsDiffBfdPmtuRxOctets = _SystemStatisticsDiffBfdPmtuRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 197),
    _SystemStatisticsDiffBfdPmtuRxOctets_Type()
)
systemStatisticsDiffBfdPmtuRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffBfdPmtuRxOctets.setStatus("current")
_SystemStatisticsDiffDnsReqSnoop_Type = Counter64
_SystemStatisticsDiffDnsReqSnoop_Object = MibScalar
systemStatisticsDiffDnsReqSnoop = _SystemStatisticsDiffDnsReqSnoop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 198),
    _SystemStatisticsDiffDnsReqSnoop_Type()
)
systemStatisticsDiffDnsReqSnoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDnsReqSnoop.setStatus("current")
_SystemStatisticsDiffDnsResSnoop_Type = Counter64
_SystemStatisticsDiffDnsResSnoop_Object = MibScalar
systemStatisticsDiffDnsResSnoop = _SystemStatisticsDiffDnsResSnoop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 199),
    _SystemStatisticsDiffDnsResSnoop_Type()
)
systemStatisticsDiffDnsResSnoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDnsResSnoop.setStatus("current")
_SystemStatisticsDiffCtrlLoopFwd_Type = Counter64
_SystemStatisticsDiffCtrlLoopFwd_Object = MibScalar
systemStatisticsDiffCtrlLoopFwd = _SystemStatisticsDiffCtrlLoopFwd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 200),
    _SystemStatisticsDiffCtrlLoopFwd_Type()
)
systemStatisticsDiffCtrlLoopFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffCtrlLoopFwd.setStatus("current")
_SystemStatisticsDiffCtrlLoopFwdDrops_Type = Counter64
_SystemStatisticsDiffCtrlLoopFwdDrops_Object = MibScalar
systemStatisticsDiffCtrlLoopFwdDrops = _SystemStatisticsDiffCtrlLoopFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 201),
    _SystemStatisticsDiffCtrlLoopFwdDrops_Type()
)
systemStatisticsDiffCtrlLoopFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffCtrlLoopFwdDrops.setStatus("current")
_SystemStatisticsDiffQatAesDecrypt_Type = Counter64
_SystemStatisticsDiffQatAesDecrypt_Object = MibScalar
systemStatisticsDiffQatAesDecrypt = _SystemStatisticsDiffQatAesDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 204),
    _SystemStatisticsDiffQatAesDecrypt_Type()
)
systemStatisticsDiffQatAesDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffQatAesDecrypt.setStatus("current")
_SystemStatisticsDiffQatAesEncrypt_Type = Counter64
_SystemStatisticsDiffQatAesEncrypt_Object = MibScalar
systemStatisticsDiffQatAesEncrypt = _SystemStatisticsDiffQatAesEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 205),
    _SystemStatisticsDiffQatAesEncrypt_Type()
)
systemStatisticsDiffQatAesEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffQatAesEncrypt.setStatus("current")
_SystemStatisticsDiffQatGcmDecrypt_Type = Counter64
_SystemStatisticsDiffQatGcmDecrypt_Object = MibScalar
systemStatisticsDiffQatGcmDecrypt = _SystemStatisticsDiffQatGcmDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 206),
    _SystemStatisticsDiffQatGcmDecrypt_Type()
)
systemStatisticsDiffQatGcmDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffQatGcmDecrypt.setStatus("current")
_SystemStatisticsDiffQatGcmEncrypt_Type = Counter64
_SystemStatisticsDiffQatGcmEncrypt_Object = MibScalar
systemStatisticsDiffQatGcmEncrypt = _SystemStatisticsDiffQatGcmEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 207),
    _SystemStatisticsDiffQatGcmEncrypt_Type()
)
systemStatisticsDiffQatGcmEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffQatGcmEncrypt.setStatus("current")
_SystemStatisticsDiffOpensslGcmDecrypt_Type = Counter64
_SystemStatisticsDiffOpensslGcmDecrypt_Object = MibScalar
systemStatisticsDiffOpensslGcmDecrypt = _SystemStatisticsDiffOpensslGcmDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 208),
    _SystemStatisticsDiffOpensslGcmDecrypt_Type()
)
systemStatisticsDiffOpensslGcmDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffOpensslGcmDecrypt.setStatus("current")
_SystemStatisticsDiffOpensslGcmEncrypt_Type = Counter64
_SystemStatisticsDiffOpensslGcmEncrypt_Object = MibScalar
systemStatisticsDiffOpensslGcmEncrypt = _SystemStatisticsDiffOpensslGcmEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 209),
    _SystemStatisticsDiffOpensslGcmEncrypt_Type()
)
systemStatisticsDiffOpensslGcmEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffOpensslGcmEncrypt.setStatus("current")
_SystemStatisticsDiffRxReplayDropsTc0_Type = Counter64
_SystemStatisticsDiffRxReplayDropsTc0_Object = MibScalar
systemStatisticsDiffRxReplayDropsTc0 = _SystemStatisticsDiffRxReplayDropsTc0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 210),
    _SystemStatisticsDiffRxReplayDropsTc0_Type()
)
systemStatisticsDiffRxReplayDropsTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDropsTc0.setStatus("current")
_SystemStatisticsDiffRxReplayDropsTc1_Type = Counter64
_SystemStatisticsDiffRxReplayDropsTc1_Object = MibScalar
systemStatisticsDiffRxReplayDropsTc1 = _SystemStatisticsDiffRxReplayDropsTc1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 211),
    _SystemStatisticsDiffRxReplayDropsTc1_Type()
)
systemStatisticsDiffRxReplayDropsTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDropsTc1.setStatus("current")
_SystemStatisticsDiffRxReplayDropsTc2_Type = Counter64
_SystemStatisticsDiffRxReplayDropsTc2_Object = MibScalar
systemStatisticsDiffRxReplayDropsTc2 = _SystemStatisticsDiffRxReplayDropsTc2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 212),
    _SystemStatisticsDiffRxReplayDropsTc2_Type()
)
systemStatisticsDiffRxReplayDropsTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDropsTc2.setStatus("current")
_SystemStatisticsDiffRxReplayDropsTc3_Type = Counter64
_SystemStatisticsDiffRxReplayDropsTc3_Object = MibScalar
systemStatisticsDiffRxReplayDropsTc3 = _SystemStatisticsDiffRxReplayDropsTc3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 213),
    _SystemStatisticsDiffRxReplayDropsTc3_Type()
)
systemStatisticsDiffRxReplayDropsTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDropsTc3.setStatus("current")
_SystemStatisticsDiffRxReplayDropsTc4_Type = Counter64
_SystemStatisticsDiffRxReplayDropsTc4_Object = MibScalar
systemStatisticsDiffRxReplayDropsTc4 = _SystemStatisticsDiffRxReplayDropsTc4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 214),
    _SystemStatisticsDiffRxReplayDropsTc4_Type()
)
systemStatisticsDiffRxReplayDropsTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDropsTc4.setStatus("current")
_SystemStatisticsDiffRxReplayDropsTc5_Type = Counter64
_SystemStatisticsDiffRxReplayDropsTc5_Object = MibScalar
systemStatisticsDiffRxReplayDropsTc5 = _SystemStatisticsDiffRxReplayDropsTc5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 215),
    _SystemStatisticsDiffRxReplayDropsTc5_Type()
)
systemStatisticsDiffRxReplayDropsTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDropsTc5.setStatus("current")
_SystemStatisticsDiffRxReplayDropsTc6_Type = Counter64
_SystemStatisticsDiffRxReplayDropsTc6_Object = MibScalar
systemStatisticsDiffRxReplayDropsTc6 = _SystemStatisticsDiffRxReplayDropsTc6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 216),
    _SystemStatisticsDiffRxReplayDropsTc6_Type()
)
systemStatisticsDiffRxReplayDropsTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDropsTc6.setStatus("current")
_SystemStatisticsDiffRxReplayDropsTc7_Type = Counter64
_SystemStatisticsDiffRxReplayDropsTc7_Object = MibScalar
systemStatisticsDiffRxReplayDropsTc7 = _SystemStatisticsDiffRxReplayDropsTc7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 217),
    _SystemStatisticsDiffRxReplayDropsTc7_Type()
)
systemStatisticsDiffRxReplayDropsTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayDropsTc7.setStatus("current")
_SystemStatisticsDiffRxWindowDropsTc0_Type = Counter64
_SystemStatisticsDiffRxWindowDropsTc0_Object = MibScalar
systemStatisticsDiffRxWindowDropsTc0 = _SystemStatisticsDiffRxWindowDropsTc0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 218),
    _SystemStatisticsDiffRxWindowDropsTc0_Type()
)
systemStatisticsDiffRxWindowDropsTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxWindowDropsTc0.setStatus("current")
_SystemStatisticsDiffRxWindowDropsTc1_Type = Counter64
_SystemStatisticsDiffRxWindowDropsTc1_Object = MibScalar
systemStatisticsDiffRxWindowDropsTc1 = _SystemStatisticsDiffRxWindowDropsTc1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 219),
    _SystemStatisticsDiffRxWindowDropsTc1_Type()
)
systemStatisticsDiffRxWindowDropsTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxWindowDropsTc1.setStatus("current")
_SystemStatisticsDiffRxWindowDropsTc2_Type = Counter64
_SystemStatisticsDiffRxWindowDropsTc2_Object = MibScalar
systemStatisticsDiffRxWindowDropsTc2 = _SystemStatisticsDiffRxWindowDropsTc2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 220),
    _SystemStatisticsDiffRxWindowDropsTc2_Type()
)
systemStatisticsDiffRxWindowDropsTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxWindowDropsTc2.setStatus("current")
_SystemStatisticsDiffRxWindowDropsTc3_Type = Counter64
_SystemStatisticsDiffRxWindowDropsTc3_Object = MibScalar
systemStatisticsDiffRxWindowDropsTc3 = _SystemStatisticsDiffRxWindowDropsTc3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 221),
    _SystemStatisticsDiffRxWindowDropsTc3_Type()
)
systemStatisticsDiffRxWindowDropsTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxWindowDropsTc3.setStatus("current")
_SystemStatisticsDiffRxWindowDropsTc4_Type = Counter64
_SystemStatisticsDiffRxWindowDropsTc4_Object = MibScalar
systemStatisticsDiffRxWindowDropsTc4 = _SystemStatisticsDiffRxWindowDropsTc4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 222),
    _SystemStatisticsDiffRxWindowDropsTc4_Type()
)
systemStatisticsDiffRxWindowDropsTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxWindowDropsTc4.setStatus("current")
_SystemStatisticsDiffRxWindowDropsTc5_Type = Counter64
_SystemStatisticsDiffRxWindowDropsTc5_Object = MibScalar
systemStatisticsDiffRxWindowDropsTc5 = _SystemStatisticsDiffRxWindowDropsTc5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 223),
    _SystemStatisticsDiffRxWindowDropsTc5_Type()
)
systemStatisticsDiffRxWindowDropsTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxWindowDropsTc5.setStatus("current")
_SystemStatisticsDiffRxWindowDropsTc6_Type = Counter64
_SystemStatisticsDiffRxWindowDropsTc6_Object = MibScalar
systemStatisticsDiffRxWindowDropsTc6 = _SystemStatisticsDiffRxWindowDropsTc6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 224),
    _SystemStatisticsDiffRxWindowDropsTc6_Type()
)
systemStatisticsDiffRxWindowDropsTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxWindowDropsTc6.setStatus("current")
_SystemStatisticsDiffRxWindowDropsTc7_Type = Counter64
_SystemStatisticsDiffRxWindowDropsTc7_Object = MibScalar
systemStatisticsDiffRxWindowDropsTc7 = _SystemStatisticsDiffRxWindowDropsTc7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 225),
    _SystemStatisticsDiffRxWindowDropsTc7_Type()
)
systemStatisticsDiffRxWindowDropsTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxWindowDropsTc7.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDropsTc0_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDropsTc0_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDropsTc0 = _SystemStatisticsDiffRxUnexpectedReplayDropsTc0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 226),
    _SystemStatisticsDiffRxUnexpectedReplayDropsTc0_Type()
)
systemStatisticsDiffRxUnexpectedReplayDropsTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDropsTc0.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDropsTc1_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDropsTc1_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDropsTc1 = _SystemStatisticsDiffRxUnexpectedReplayDropsTc1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 227),
    _SystemStatisticsDiffRxUnexpectedReplayDropsTc1_Type()
)
systemStatisticsDiffRxUnexpectedReplayDropsTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDropsTc1.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDropsTc2_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDropsTc2_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDropsTc2 = _SystemStatisticsDiffRxUnexpectedReplayDropsTc2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 228),
    _SystemStatisticsDiffRxUnexpectedReplayDropsTc2_Type()
)
systemStatisticsDiffRxUnexpectedReplayDropsTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDropsTc2.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDropsTc3_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDropsTc3_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDropsTc3 = _SystemStatisticsDiffRxUnexpectedReplayDropsTc3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 229),
    _SystemStatisticsDiffRxUnexpectedReplayDropsTc3_Type()
)
systemStatisticsDiffRxUnexpectedReplayDropsTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDropsTc3.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDropsTc4_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDropsTc4_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDropsTc4 = _SystemStatisticsDiffRxUnexpectedReplayDropsTc4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 230),
    _SystemStatisticsDiffRxUnexpectedReplayDropsTc4_Type()
)
systemStatisticsDiffRxUnexpectedReplayDropsTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDropsTc4.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDropsTc5_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDropsTc5_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDropsTc5 = _SystemStatisticsDiffRxUnexpectedReplayDropsTc5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 231),
    _SystemStatisticsDiffRxUnexpectedReplayDropsTc5_Type()
)
systemStatisticsDiffRxUnexpectedReplayDropsTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDropsTc5.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDropsTc6_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDropsTc6_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDropsTc6 = _SystemStatisticsDiffRxUnexpectedReplayDropsTc6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 232),
    _SystemStatisticsDiffRxUnexpectedReplayDropsTc6_Type()
)
systemStatisticsDiffRxUnexpectedReplayDropsTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDropsTc6.setStatus("current")
_SystemStatisticsDiffRxUnexpectedReplayDropsTc7_Type = Counter64
_SystemStatisticsDiffRxUnexpectedReplayDropsTc7_Object = MibScalar
systemStatisticsDiffRxUnexpectedReplayDropsTc7 = _SystemStatisticsDiffRxUnexpectedReplayDropsTc7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 233),
    _SystemStatisticsDiffRxUnexpectedReplayDropsTc7_Type()
)
systemStatisticsDiffRxUnexpectedReplayDropsTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxUnexpectedReplayDropsTc7.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDropsTc0_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDropsTc0_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDropsTc0 = _SystemStatisticsDiffRxReplayIntegrityDropsTc0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 234),
    _SystemStatisticsDiffRxReplayIntegrityDropsTc0_Type()
)
systemStatisticsDiffRxReplayIntegrityDropsTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDropsTc0.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDropsTc1_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDropsTc1_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDropsTc1 = _SystemStatisticsDiffRxReplayIntegrityDropsTc1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 235),
    _SystemStatisticsDiffRxReplayIntegrityDropsTc1_Type()
)
systemStatisticsDiffRxReplayIntegrityDropsTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDropsTc1.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDropsTc2_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDropsTc2_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDropsTc2 = _SystemStatisticsDiffRxReplayIntegrityDropsTc2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 236),
    _SystemStatisticsDiffRxReplayIntegrityDropsTc2_Type()
)
systemStatisticsDiffRxReplayIntegrityDropsTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDropsTc2.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDropsTc3_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDropsTc3_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDropsTc3 = _SystemStatisticsDiffRxReplayIntegrityDropsTc3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 237),
    _SystemStatisticsDiffRxReplayIntegrityDropsTc3_Type()
)
systemStatisticsDiffRxReplayIntegrityDropsTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDropsTc3.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDropsTc4_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDropsTc4_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDropsTc4 = _SystemStatisticsDiffRxReplayIntegrityDropsTc4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 238),
    _SystemStatisticsDiffRxReplayIntegrityDropsTc4_Type()
)
systemStatisticsDiffRxReplayIntegrityDropsTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDropsTc4.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDropsTc5_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDropsTc5_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDropsTc5 = _SystemStatisticsDiffRxReplayIntegrityDropsTc5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 239),
    _SystemStatisticsDiffRxReplayIntegrityDropsTc5_Type()
)
systemStatisticsDiffRxReplayIntegrityDropsTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDropsTc5.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDropsTc6_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDropsTc6_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDropsTc6 = _SystemStatisticsDiffRxReplayIntegrityDropsTc6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 240),
    _SystemStatisticsDiffRxReplayIntegrityDropsTc6_Type()
)
systemStatisticsDiffRxReplayIntegrityDropsTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDropsTc6.setStatus("current")
_SystemStatisticsDiffRxReplayIntegrityDropsTc7_Type = Counter64
_SystemStatisticsDiffRxReplayIntegrityDropsTc7_Object = MibScalar
systemStatisticsDiffRxReplayIntegrityDropsTc7 = _SystemStatisticsDiffRxReplayIntegrityDropsTc7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 241),
    _SystemStatisticsDiffRxReplayIntegrityDropsTc7_Type()
)
systemStatisticsDiffRxReplayIntegrityDropsTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxReplayIntegrityDropsTc7.setStatus("current")
_SystemStatisticsDiffIcmpRedirectTxDrops_Type = Counter64
_SystemStatisticsDiffIcmpRedirectTxDrops_Object = MibScalar
systemStatisticsDiffIcmpRedirectTxDrops = _SystemStatisticsDiffIcmpRedirectTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 242),
    _SystemStatisticsDiffIcmpRedirectTxDrops_Type()
)
systemStatisticsDiffIcmpRedirectTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIcmpRedirectTxDrops.setStatus("current")
_SystemStatisticsDiffIcmpRedirectRxDrops_Type = Counter64
_SystemStatisticsDiffIcmpRedirectRxDrops_Object = MibScalar
systemStatisticsDiffIcmpRedirectRxDrops = _SystemStatisticsDiffIcmpRedirectRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 243),
    _SystemStatisticsDiffIcmpRedirectRxDrops_Type()
)
systemStatisticsDiffIcmpRedirectRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIcmpRedirectRxDrops.setStatus("current")
_SystemStatisticsDiffRxL2MtuExceeded_Type = Counter64
_SystemStatisticsDiffRxL2MtuExceeded_Object = MibScalar
systemStatisticsDiffRxL2MtuExceeded = _SystemStatisticsDiffRxL2MtuExceeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 244),
    _SystemStatisticsDiffRxL2MtuExceeded_Type()
)
systemStatisticsDiffRxL2MtuExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxL2MtuExceeded.setStatus("deprecated")
_SystemStatisticsDiffIpDirectBcastTxDrops_Type = Counter64
_SystemStatisticsDiffIpDirectBcastTxDrops_Object = MibScalar
systemStatisticsDiffIpDirectBcastTxDrops = _SystemStatisticsDiffIpDirectBcastTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 245),
    _SystemStatisticsDiffIpDirectBcastTxDrops_Type()
)
systemStatisticsDiffIpDirectBcastTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpDirectBcastTxDrops.setStatus("current")
_SystemStatisticsDiffIpDirectBcastTxL2Bcast_Type = Counter64
_SystemStatisticsDiffIpDirectBcastTxL2Bcast_Object = MibScalar
systemStatisticsDiffIpDirectBcastTxL2Bcast = _SystemStatisticsDiffIpDirectBcastTxL2Bcast_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 246),
    _SystemStatisticsDiffIpDirectBcastTxL2Bcast_Type()
)
systemStatisticsDiffIpDirectBcastTxL2Bcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpDirectBcastTxL2Bcast.setStatus("current")
_SystemStatisticsDiffRxInvalidIpHdr_Type = Counter64
_SystemStatisticsDiffRxInvalidIpHdr_Object = MibScalar
systemStatisticsDiffRxInvalidIpHdr = _SystemStatisticsDiffRxInvalidIpHdr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 247),
    _SystemStatisticsDiffRxInvalidIpHdr_Type()
)
systemStatisticsDiffRxInvalidIpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffRxInvalidIpHdr.setStatus("current")
_SystemStatisticsDiffNatDstNatMapInvalid_Type = Counter64
_SystemStatisticsDiffNatDstNatMapInvalid_Object = MibScalar
systemStatisticsDiffNatDstNatMapInvalid = _SystemStatisticsDiffNatDstNatMapInvalid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 248),
    _SystemStatisticsDiffNatDstNatMapInvalid_Type()
)
systemStatisticsDiffNatDstNatMapInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffNatDstNatMapInvalid.setStatus("current")
_SystemStatisticsDiffDevicePolicyDrops_Type = Counter64
_SystemStatisticsDiffDevicePolicyDrops_Object = MibScalar
systemStatisticsDiffDevicePolicyDrops = _SystemStatisticsDiffDevicePolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 249),
    _SystemStatisticsDiffDevicePolicyDrops_Type()
)
systemStatisticsDiffDevicePolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffDevicePolicyDrops.setStatus("current")
_SystemStatisticsDiffInvalidLoopHdrDrops_Type = Counter64
_SystemStatisticsDiffInvalidLoopHdrDrops_Object = MibScalar
systemStatisticsDiffInvalidLoopHdrDrops = _SystemStatisticsDiffInvalidLoopHdrDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 250),
    _SystemStatisticsDiffInvalidLoopHdrDrops_Type()
)
systemStatisticsDiffInvalidLoopHdrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffInvalidLoopHdrDrops.setStatus("current")
_SystemStatisticsDiffZbfFragCacheDrops_Type = Counter64
_SystemStatisticsDiffZbfFragCacheDrops_Object = MibScalar
systemStatisticsDiffZbfFragCacheDrops = _SystemStatisticsDiffZbfFragCacheDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 251),
    _SystemStatisticsDiffZbfFragCacheDrops_Type()
)
systemStatisticsDiffZbfFragCacheDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffZbfFragCacheDrops.setStatus("current")
_SystemStatisticsDiffNatFragCacheDrops_Type = Counter64
_SystemStatisticsDiffNatFragCacheDrops_Object = MibScalar
systemStatisticsDiffNatFragCacheDrops = _SystemStatisticsDiffNatFragCacheDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 252),
    _SystemStatisticsDiffNatFragCacheDrops_Type()
)
systemStatisticsDiffNatFragCacheDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffNatFragCacheDrops.setStatus("current")
_SystemStatisticsDiffTxTrackerIfNotPreferred_Type = Counter64
_SystemStatisticsDiffTxTrackerIfNotPreferred_Object = MibScalar
systemStatisticsDiffTxTrackerIfNotPreferred = _SystemStatisticsDiffTxTrackerIfNotPreferred_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 253),
    _SystemStatisticsDiffTxTrackerIfNotPreferred_Type()
)
systemStatisticsDiffTxTrackerIfNotPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffTxTrackerIfNotPreferred.setStatus("current")
_SystemStatisticsDiffIpfragAllfragsSeen_Type = Counter64
_SystemStatisticsDiffIpfragAllfragsSeen_Object = MibScalar
systemStatisticsDiffIpfragAllfragsSeen = _SystemStatisticsDiffIpfragAllfragsSeen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 254),
    _SystemStatisticsDiffIpfragAllfragsSeen_Type()
)
systemStatisticsDiffIpfragAllfragsSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpfragAllfragsSeen.setStatus("current")
_SystemStatisticsDiffIpfragManyFrags_Type = Counter64
_SystemStatisticsDiffIpfragManyFrags_Object = MibScalar
systemStatisticsDiffIpfragManyFrags = _SystemStatisticsDiffIpfragManyFrags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 255),
    _SystemStatisticsDiffIpfragManyFrags_Type()
)
systemStatisticsDiffIpfragManyFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffIpfragManyFrags.setStatus("current")
_SystemStatisticsDiffVRRPMismatchedDMACDrops_Type = Counter64
_SystemStatisticsDiffVRRPMismatchedDMACDrops_Object = MibScalar
systemStatisticsDiffVRRPMismatchedDMACDrops = _SystemStatisticsDiffVRRPMismatchedDMACDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 3, 256),
    _SystemStatisticsDiffVRRPMismatchedDMACDrops_Type()
)
systemStatisticsDiffVRRPMismatchedDMACDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatisticsDiffVRRPMismatchedDMACDrops.setStatus("current")
_Reboot_ObjectIdentity = ObjectIdentity
reboot = _Reboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11, 4)
)
_RebootHistoryTable_Object = MibTable
rebootHistoryTable = _RebootHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 4, 1)
)
if mibBuilder.loadTexts:
    rebootHistoryTable.setStatus("current")
_RebootHistoryEntry_Object = MibTableRow
rebootHistoryEntry = _RebootHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 4, 1, 1)
)
rebootHistoryEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "rebootHistoryRebootDateTime"),
)
if mibBuilder.loadTexts:
    rebootHistoryEntry.setStatus("current")
_RebootHistoryRebootDateTime_Type = DateAndTime
_RebootHistoryRebootDateTime_Object = MibTableColumn
rebootHistoryRebootDateTime = _RebootHistoryRebootDateTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 4, 1, 1, 1),
    _RebootHistoryRebootDateTime_Type()
)
rebootHistoryRebootDateTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rebootHistoryRebootDateTime.setStatus("current")
_RebootHistoryRebootReason_Type = String
_RebootHistoryRebootReason_Object = MibTableColumn
rebootHistoryRebootReason = _RebootHistoryRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 4, 1, 1, 3),
    _RebootHistoryRebootReason_Type()
)
rebootHistoryRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rebootHistoryRebootReason.setStatus("current")
_BootPartitionTable_Object = MibTable
bootPartitionTable = _BootPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 5)
)
if mibBuilder.loadTexts:
    bootPartitionTable.setStatus("current")
_BootPartitionEntry_Object = MibTableRow
bootPartitionEntry = _BootPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 5, 1)
)
bootPartitionEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "bootPartitionPartition"),
)
if mibBuilder.loadTexts:
    bootPartitionEntry.setStatus("current")


class _BootPartitionPartition_Type(Integer32):
    """Custom type bootPartitionPartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("a1", 0),
          ("a2", 1))
    )


_BootPartitionPartition_Type.__name__ = "Integer32"
_BootPartitionPartition_Object = MibTableColumn
bootPartitionPartition = _BootPartitionPartition_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 5, 1, 1),
    _BootPartitionPartition_Type()
)
bootPartitionPartition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bootPartitionPartition.setStatus("current")
_BootPartitionActive_Type = TruthValue
_BootPartitionActive_Object = MibTableColumn
bootPartitionActive = _BootPartitionActive_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 5, 1, 2),
    _BootPartitionActive_Type()
)
bootPartitionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootPartitionActive.setStatus("current")


class _BootPartitionVersion_Type(String):
    """Custom type bootPartitionVersion based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_BootPartitionVersion_Type.__name__ = "String"
_BootPartitionVersion_Object = MibTableColumn
bootPartitionVersion = _BootPartitionVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 5, 1, 3),
    _BootPartitionVersion_Type()
)
bootPartitionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootPartitionVersion.setStatus("current")
_BootPartitionTimestamp_Type = DateAndTime
_BootPartitionTimestamp_Object = MibTableColumn
bootPartitionTimestamp = _BootPartitionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 5, 1, 4),
    _BootPartitionTimestamp_Type()
)
bootPartitionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootPartitionTimestamp.setStatus("current")
_UsersTable_Object = MibTable
usersTable = _UsersTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6)
)
if mibBuilder.loadTexts:
    usersTable.setStatus("current")
_UsersEntry_Object = MibTableRow
usersEntry = _UsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6, 1)
)
usersEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "usersSession"),
)
if mibBuilder.loadTexts:
    usersEntry.setStatus("current")
_UsersSession_Type = Unsigned32
_UsersSession_Object = MibTableColumn
usersSession = _UsersSession_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6, 1, 1),
    _UsersSession_Type()
)
usersSession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usersSession.setStatus("current")


class _UsersUser_Type(String):
    """Custom type usersUser based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_UsersUser_Type.__name__ = "String"
_UsersUser_Object = MibTableColumn
usersUser = _UsersUser_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6, 1, 2),
    _UsersUser_Type()
)
usersUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersUser.setStatus("current")
_UsersContext_Type = String
_UsersContext_Object = MibTableColumn
usersContext = _UsersContext_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6, 1, 3),
    _UsersContext_Type()
)
usersContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersContext.setStatus("current")
_UsersFrom_Type = InetAddressIP
_UsersFrom_Object = MibTableColumn
usersFrom = _UsersFrom_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6, 1, 4),
    _UsersFrom_Type()
)
usersFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersFrom.setStatus("current")


class _UsersProto_Type(Integer32):
    """Custom type usersProto based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tcp", 1),
          ("ssh", 2),
          ("system", 3),
          ("console", 4),
          ("ssl", 5),
          ("http", 6),
          ("https", 7),
          ("udp", 8))
    )


_UsersProto_Type.__name__ = "Integer32"
_UsersProto_Object = MibTableColumn
usersProto = _UsersProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6, 1, 5),
    _UsersProto_Type()
)
usersProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersProto.setStatus("current")
_UsersAuthGroup_Type = String
_UsersAuthGroup_Object = MibTableColumn
usersAuthGroup = _UsersAuthGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6, 1, 6),
    _UsersAuthGroup_Type()
)
usersAuthGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersAuthGroup.setStatus("current")
_UsersLoginTime_Type = DateAndTime
_UsersLoginTime_Object = MibTableColumn
usersLoginTime = _UsersLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 6, 1, 7),
    _UsersLoginTime_Type()
)
usersLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersLoginTime.setStatus("current")
_Aaa_ObjectIdentity = ObjectIdentity
aaa = _Aaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11, 7)
)
_AaaUsergroupTable_Object = MibTable
aaaUsergroupTable = _AaaUsergroupTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 7, 1)
)
if mibBuilder.loadTexts:
    aaaUsergroupTable.setStatus("current")
_AaaUsergroupEntry_Object = MibTableRow
aaaUsergroupEntry = _AaaUsergroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 7, 1, 1)
)
aaaUsergroupEntry.setIndexNames(
    (1, "VIPTELA-OPER-SYSTEM", "aaaUsergroupName"),
)
if mibBuilder.loadTexts:
    aaaUsergroupEntry.setStatus("current")


class _AaaUsergroupName_Type(String):
    """Custom type aaaUsergroupName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AaaUsergroupName_Type.__name__ = "String"
_AaaUsergroupName_Object = MibTableColumn
aaaUsergroupName = _AaaUsergroupName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 7, 1, 1, 1),
    _AaaUsergroupName_Type()
)
aaaUsergroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaUsergroupName.setStatus("current")
_AaaUsergroupTaskTable_Object = MibTable
aaaUsergroupTaskTable = _AaaUsergroupTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 8)
)
if mibBuilder.loadTexts:
    aaaUsergroupTaskTable.setStatus("current")
_AaaUsergroupTaskEntry_Object = MibTableRow
aaaUsergroupTaskEntry = _AaaUsergroupTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 8, 1)
)
aaaUsergroupTaskEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "aaaUsergroupName"),
    (0, "VIPTELA-OPER-SYSTEM", "aaaUsergroupTaskMode"),
)
if mibBuilder.loadTexts:
    aaaUsergroupTaskEntry.setStatus("current")


class _AaaUsergroupTaskMode_Type(Integer32):
    """Custom type aaaUsergroupTaskMode based on Integer32"""
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
        *(("system", 0),
          ("interface", 1),
          ("policy", 2),
          ("routing", 3),
          ("security", 4))
    )


_AaaUsergroupTaskMode_Type.__name__ = "Integer32"
_AaaUsergroupTaskMode_Object = MibTableColumn
aaaUsergroupTaskMode = _AaaUsergroupTaskMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 8, 1, 1),
    _AaaUsergroupTaskMode_Type()
)
aaaUsergroupTaskMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaUsergroupTaskMode.setStatus("current")
_AaaUsergroupTaskPermission_Type = Permission1
_AaaUsergroupTaskPermission_Object = MibTableColumn
aaaUsergroupTaskPermission = _AaaUsergroupTaskPermission_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 8, 1, 2),
    _AaaUsergroupTaskPermission_Type()
)
aaaUsergroupTaskPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaUsergroupTaskPermission.setStatus("current")
_Logging_ObjectIdentity = ObjectIdentity
logging = _Logging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9)
)
_LoggingHostStatus_Type = String
_LoggingHostStatus_Object = MibScalar
loggingHostStatus = _LoggingHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 1),
    _LoggingHostStatus_Type()
)
loggingHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingHostStatus.setStatus("current")
_LoggingHostName_Type = String
_LoggingHostName_Object = MibScalar
loggingHostName = _LoggingHostName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 2),
    _LoggingHostName_Type()
)
loggingHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingHostName.setStatus("current")
_LoggingHostPriority_Type = String
_LoggingHostPriority_Object = MibScalar
loggingHostPriority = _LoggingHostPriority_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 3),
    _LoggingHostPriority_Type()
)
loggingHostPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingHostPriority.setStatus("current")


class _LoggingHostVpnId_Type(Unsigned32):
    """Custom type loggingHostVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_LoggingHostVpnId_Type.__name__ = "Unsigned32"
_LoggingHostVpnId_Object = MibScalar
loggingHostVpnId = _LoggingHostVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 4),
    _LoggingHostVpnId_Type()
)
loggingHostVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingHostVpnId.setStatus("current")
_LoggingDiskStatus_Type = String
_LoggingDiskStatus_Object = MibScalar
loggingDiskStatus = _LoggingDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 5),
    _LoggingDiskStatus_Type()
)
loggingDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingDiskStatus.setStatus("current")
_LoggingDiskPriority_Type = String
_LoggingDiskPriority_Object = MibScalar
loggingDiskPriority = _LoggingDiskPriority_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 6),
    _LoggingDiskPriority_Type()
)
loggingDiskPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingDiskPriority.setStatus("current")
_LoggingDiskFilename_Type = String
_LoggingDiskFilename_Object = MibScalar
loggingDiskFilename = _LoggingDiskFilename_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 7),
    _LoggingDiskFilename_Type()
)
loggingDiskFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingDiskFilename.setStatus("current")
_LoggingDiskFilesize_Type = UnsignedShort
_LoggingDiskFilesize_Object = MibScalar
loggingDiskFilesize = _LoggingDiskFilesize_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 8),
    _LoggingDiskFilesize_Type()
)
loggingDiskFilesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingDiskFilesize.setStatus("current")
_LoggingDiskFilerotate_Type = UnsignedByte
_LoggingDiskFilerotate_Object = MibScalar
loggingDiskFilerotate = _LoggingDiskFilerotate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 9, 9),
    _LoggingDiskFilerotate_Type()
)
loggingDiskFilerotate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggingDiskFilerotate.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10)
)
_NtpPeerTable_Object = MibTable
ntpPeerTable = _NtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1)
)
if mibBuilder.loadTexts:
    ntpPeerTable.setStatus("current")
_NtpPeerEntry_Object = MibTableRow
ntpPeerEntry = _NtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1)
)
ntpPeerEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "ntpPeerIndex"),
)
if mibBuilder.loadTexts:
    ntpPeerEntry.setStatus("current")
_NtpPeerIndex_Type = Unsigned32
_NtpPeerIndex_Object = MibTableColumn
ntpPeerIndex = _NtpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 1),
    _NtpPeerIndex_Type()
)
ntpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpPeerIndex.setStatus("current")


class _NtpPeerRemote_Type(String):
    """Custom type ntpPeerRemote based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpPeerRemote_Type.__name__ = "String"
_NtpPeerRemote_Object = MibTableColumn
ntpPeerRemote = _NtpPeerRemote_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 2),
    _NtpPeerRemote_Type()
)
ntpPeerRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerRemote.setStatus("current")


class _NtpPeerRefid_Type(String):
    """Custom type ntpPeerRefid based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpPeerRefid_Type.__name__ = "String"
_NtpPeerRefid_Object = MibTableColumn
ntpPeerRefid = _NtpPeerRefid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 3),
    _NtpPeerRefid_Type()
)
ntpPeerRefid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerRefid.setStatus("current")
_NtpPeerSt_Type = Integer32
_NtpPeerSt_Object = MibTableColumn
ntpPeerSt = _NtpPeerSt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 4),
    _NtpPeerSt_Type()
)
ntpPeerSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerSt.setStatus("current")


class _NtpPeerType_Type(String):
    """Custom type ntpPeerType based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpPeerType_Type.__name__ = "String"
_NtpPeerType_Object = MibTableColumn
ntpPeerType = _NtpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 5),
    _NtpPeerType_Type()
)
ntpPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerType.setStatus("current")


class _NtpPeerWhen_Type(String):
    """Custom type ntpPeerWhen based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpPeerWhen_Type.__name__ = "String"
_NtpPeerWhen_Object = MibTableColumn
ntpPeerWhen = _NtpPeerWhen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 6),
    _NtpPeerWhen_Type()
)
ntpPeerWhen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerWhen.setStatus("current")
_NtpPeerPoll_Type = Integer32
_NtpPeerPoll_Object = MibTableColumn
ntpPeerPoll = _NtpPeerPoll_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 7),
    _NtpPeerPoll_Type()
)
ntpPeerPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerPoll.setStatus("current")


class _NtpPeerReach_Type(String):
    """Custom type ntpPeerReach based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpPeerReach_Type.__name__ = "String"
_NtpPeerReach_Object = MibTableColumn
ntpPeerReach = _NtpPeerReach_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 8),
    _NtpPeerReach_Type()
)
ntpPeerReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerReach.setStatus("current")


class _NtpPeerDelay_Type(String):
    """Custom type ntpPeerDelay based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpPeerDelay_Type.__name__ = "String"
_NtpPeerDelay_Object = MibTableColumn
ntpPeerDelay = _NtpPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 9),
    _NtpPeerDelay_Type()
)
ntpPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerDelay.setStatus("current")


class _NtpPeerOffset_Type(String):
    """Custom type ntpPeerOffset based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpPeerOffset_Type.__name__ = "String"
_NtpPeerOffset_Object = MibTableColumn
ntpPeerOffset = _NtpPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 10),
    _NtpPeerOffset_Type()
)
ntpPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerOffset.setStatus("current")


class _NtpPeerJitter_Type(String):
    """Custom type ntpPeerJitter based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpPeerJitter_Type.__name__ = "String"
_NtpPeerJitter_Object = MibTableColumn
ntpPeerJitter = _NtpPeerJitter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 1, 1, 11),
    _NtpPeerJitter_Type()
)
ntpPeerJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerJitter.setStatus("current")
_NtpAssociationsTable_Object = MibTable
ntpAssociationsTable = _NtpAssociationsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2)
)
if mibBuilder.loadTexts:
    ntpAssociationsTable.setStatus("current")
_NtpAssociationsEntry_Object = MibTableRow
ntpAssociationsEntry = _NtpAssociationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1)
)
ntpAssociationsEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "ntpAssociationsIdx"),
)
if mibBuilder.loadTexts:
    ntpAssociationsEntry.setStatus("current")


class _NtpAssociationsIdx_Type(Integer32):
    """Custom type ntpAssociationsIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NtpAssociationsIdx_Type.__name__ = "Integer32"
_NtpAssociationsIdx_Object = MibTableColumn
ntpAssociationsIdx = _NtpAssociationsIdx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 1),
    _NtpAssociationsIdx_Type()
)
ntpAssociationsIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpAssociationsIdx.setStatus("current")


class _NtpAssociationsAssocid_Type(String):
    """Custom type ntpAssociationsAssocid based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAssociationsAssocid_Type.__name__ = "String"
_NtpAssociationsAssocid_Object = MibTableColumn
ntpAssociationsAssocid = _NtpAssociationsAssocid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 2),
    _NtpAssociationsAssocid_Type()
)
ntpAssociationsAssocid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationsAssocid.setStatus("current")


class _NtpAssociationsStatus_Type(String):
    """Custom type ntpAssociationsStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAssociationsStatus_Type.__name__ = "String"
_NtpAssociationsStatus_Object = MibTableColumn
ntpAssociationsStatus = _NtpAssociationsStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 3),
    _NtpAssociationsStatus_Type()
)
ntpAssociationsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationsStatus.setStatus("current")


class _NtpAssociationsConf_Type(String):
    """Custom type ntpAssociationsConf based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAssociationsConf_Type.__name__ = "String"
_NtpAssociationsConf_Object = MibTableColumn
ntpAssociationsConf = _NtpAssociationsConf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 4),
    _NtpAssociationsConf_Type()
)
ntpAssociationsConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationsConf.setStatus("current")


class _NtpAssociationsReachability_Type(String):
    """Custom type ntpAssociationsReachability based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAssociationsReachability_Type.__name__ = "String"
_NtpAssociationsReachability_Object = MibTableColumn
ntpAssociationsReachability = _NtpAssociationsReachability_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 5),
    _NtpAssociationsReachability_Type()
)
ntpAssociationsReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationsReachability.setStatus("current")


class _NtpAssociationsAuth_Type(String):
    """Custom type ntpAssociationsAuth based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAssociationsAuth_Type.__name__ = "String"
_NtpAssociationsAuth_Object = MibTableColumn
ntpAssociationsAuth = _NtpAssociationsAuth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 6),
    _NtpAssociationsAuth_Type()
)
ntpAssociationsAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationsAuth.setStatus("current")


class _NtpAssociationsCondition_Type(String):
    """Custom type ntpAssociationsCondition based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAssociationsCondition_Type.__name__ = "String"
_NtpAssociationsCondition_Object = MibTableColumn
ntpAssociationsCondition = _NtpAssociationsCondition_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 7),
    _NtpAssociationsCondition_Type()
)
ntpAssociationsCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationsCondition.setStatus("current")


class _NtpAssociationsLastEvent_Type(String):
    """Custom type ntpAssociationsLastEvent based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAssociationsLastEvent_Type.__name__ = "String"
_NtpAssociationsLastEvent_Object = MibTableColumn
ntpAssociationsLastEvent = _NtpAssociationsLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 8),
    _NtpAssociationsLastEvent_Type()
)
ntpAssociationsLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationsLastEvent.setStatus("current")
_NtpAssociationsCount_Type = Integer32
_NtpAssociationsCount_Object = MibTableColumn
ntpAssociationsCount = _NtpAssociationsCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 2, 1, 9),
    _NtpAssociationsCount_Type()
)
ntpAssociationsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssociationsCount.setStatus("current")


class _NtpRefid_Type(String):
    """Custom type ntpRefid based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpRefid_Type.__name__ = "String"
_NtpRefid_Object = MibScalar
ntpRefid = _NtpRefid_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 3),
    _NtpRefid_Type()
)
ntpRefid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpRefid.setStatus("obsolete")


class _NtpReftime_Type(String):
    """Custom type ntpReftime based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpReftime_Type.__name__ = "String"
_NtpReftime_Object = MibScalar
ntpReftime = _NtpReftime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 4),
    _NtpReftime_Type()
)
ntpReftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpReftime.setStatus("obsolete")
_NtpStratum_Type = Unsigned32
_NtpStratum_Object = MibScalar
ntpStratum = _NtpStratum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 5),
    _NtpStratum_Type()
)
ntpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStratum.setStatus("obsolete")


class _NtpRootdelay_Type(String):
    """Custom type ntpRootdelay based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpRootdelay_Type.__name__ = "String"
_NtpRootdelay_Object = MibScalar
ntpRootdelay = _NtpRootdelay_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 6),
    _NtpRootdelay_Type()
)
ntpRootdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpRootdelay.setStatus("obsolete")


class _NtpRootdisp_Type(String):
    """Custom type ntpRootdisp based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpRootdisp_Type.__name__ = "String"
_NtpRootdisp_Object = MibScalar
ntpRootdisp = _NtpRootdisp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 7),
    _NtpRootdisp_Type()
)
ntpRootdisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpRootdisp.setStatus("obsolete")


class _NtpFreqDriftPpm_Type(String):
    """Custom type ntpFreqDriftPpm based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpFreqDriftPpm_Type.__name__ = "String"
_NtpFreqDriftPpm_Object = MibScalar
ntpFreqDriftPpm = _NtpFreqDriftPpm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 8),
    _NtpFreqDriftPpm_Type()
)
ntpFreqDriftPpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpFreqDriftPpm.setStatus("obsolete")
_NtpPollInterval_Type = Unsigned32
_NtpPollInterval_Object = MibScalar
ntpPollInterval = _NtpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 9),
    _NtpPollInterval_Type()
)
ntpPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPollInterval.setStatus("obsolete")


class _NtpOffset_Type(String):
    """Custom type ntpOffset based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpOffset_Type.__name__ = "String"
_NtpOffset_Object = MibScalar
ntpOffset = _NtpOffset_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 10, 10),
    _NtpOffset_Type()
)
ntpOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpOffset.setStatus("obsolete")
_Transport_ObjectIdentity = ObjectIdentity
transport = _Transport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 11, 11)
)
_TransportConnectionTable_Object = MibTable
transportConnectionTable = _TransportConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 11, 1)
)
if mibBuilder.loadTexts:
    transportConnectionTable.setStatus("current")
_TransportConnectionEntry_Object = MibTableRow
transportConnectionEntry = _TransportConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 11, 1, 1)
)
transportConnectionEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "transportConnectionTrackType"),
    (0, "VIPTELA-OPER-SYSTEM", "transportConnectionSource"),
    (0, "VIPTELA-OPER-SYSTEM", "transportConnectionDestination"),
)
if mibBuilder.loadTexts:
    transportConnectionEntry.setStatus("current")


class _TransportConnectionTrackType_Type(Integer32):
    """Custom type transportConnectionTrackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("system", 0),
          ("tloc", 1))
    )


_TransportConnectionTrackType_Type.__name__ = "Integer32"
_TransportConnectionTrackType_Object = MibTableColumn
transportConnectionTrackType = _TransportConnectionTrackType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 11, 1, 1, 1),
    _TransportConnectionTrackType_Type()
)
transportConnectionTrackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    transportConnectionTrackType.setStatus("current")
_TransportConnectionSource_Type = InetAddressIP
_TransportConnectionSource_Object = MibTableColumn
transportConnectionSource = _TransportConnectionSource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 11, 1, 1, 2),
    _TransportConnectionSource_Type()
)
transportConnectionSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    transportConnectionSource.setStatus("current")
_TransportConnectionDestination_Type = InetAddressIP
_TransportConnectionDestination_Object = MibTableColumn
transportConnectionDestination = _TransportConnectionDestination_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 11, 1, 1, 3),
    _TransportConnectionDestination_Type()
)
transportConnectionDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    transportConnectionDestination.setStatus("current")
_TransportConnectionHost_Type = String
_TransportConnectionHost_Object = MibTableColumn
transportConnectionHost = _TransportConnectionHost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 11, 1, 1, 4),
    _TransportConnectionHost_Type()
)
transportConnectionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transportConnectionHost.setStatus("current")
_TransportConnectionHistoryTable_Object = MibTable
transportConnectionHistoryTable = _TransportConnectionHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 12)
)
if mibBuilder.loadTexts:
    transportConnectionHistoryTable.setStatus("current")
_TransportConnectionHistoryEntry_Object = MibTableRow
transportConnectionHistoryEntry = _TransportConnectionHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 12, 1)
)
transportConnectionHistoryEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "transportConnectionTrackType"),
    (0, "VIPTELA-OPER-SYSTEM", "transportConnectionSource"),
    (0, "VIPTELA-OPER-SYSTEM", "transportConnectionDestination"),
    (0, "VIPTELA-OPER-SYSTEM", "transportConnectionHistoryIndex"),
)
if mibBuilder.loadTexts:
    transportConnectionHistoryEntry.setStatus("current")
_TransportConnectionHistoryIndex_Type = Unsigned32
_TransportConnectionHistoryIndex_Object = MibTableColumn
transportConnectionHistoryIndex = _TransportConnectionHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 12, 1, 1),
    _TransportConnectionHistoryIndex_Type()
)
transportConnectionHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    transportConnectionHistoryIndex.setStatus("current")
_TransportConnectionHistoryTime_Type = String
_TransportConnectionHistoryTime_Object = MibTableColumn
transportConnectionHistoryTime = _TransportConnectionHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 12, 1, 2),
    _TransportConnectionHistoryTime_Type()
)
transportConnectionHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transportConnectionHistoryTime.setStatus("current")


class _TransportConnectionHistoryState_Type(Integer32):
    """Custom type transportConnectionHistoryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_TransportConnectionHistoryState_Type.__name__ = "Integer32"
_TransportConnectionHistoryState_Object = MibTableColumn
transportConnectionHistoryState = _TransportConnectionHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 12, 1, 3),
    _TransportConnectionHistoryState_Type()
)
transportConnectionHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transportConnectionHistoryState.setStatus("current")
_CrashTable_Object = MibTable
crashTable = _CrashTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 13)
)
if mibBuilder.loadTexts:
    crashTable.setStatus("current")
_CrashEntry_Object = MibTableRow
crashEntry = _CrashEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 13, 1)
)
crashEntry.setIndexNames(
    (0, "VIPTELA-OPER-SYSTEM", "crashIndex"),
)
if mibBuilder.loadTexts:
    crashEntry.setStatus("current")


class _CrashIndex_Type(Integer32):
    """Custom type crashIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CrashIndex_Type.__name__ = "Integer32"
_CrashIndex_Object = MibTableColumn
crashIndex = _CrashIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 13, 1, 1),
    _CrashIndex_Type()
)
crashIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crashIndex.setStatus("current")
_CrashCoreTime_Type = String
_CrashCoreTime_Object = MibTableColumn
crashCoreTime = _CrashCoreTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 13, 1, 2),
    _CrashCoreTime_Type()
)
crashCoreTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crashCoreTime.setStatus("current")
_CrashCoreFilename_Type = String
_CrashCoreFilename_Object = MibTableColumn
crashCoreFilename = _CrashCoreFilename_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 13, 1, 3),
    _CrashCoreFilename_Type()
)
crashCoreFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crashCoreFilename.setStatus("current")
_SoftwareTable_Object = MibTable
softwareTable = _SoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14)
)
if mibBuilder.loadTexts:
    softwareTable.setStatus("current")
_SoftwareEntry_Object = MibTableRow
softwareEntry = _SoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14, 1)
)
softwareEntry.setIndexNames(
    (1, "VIPTELA-OPER-SYSTEM", "softwareVersion"),
)
if mibBuilder.loadTexts:
    softwareEntry.setStatus("current")


class _SoftwareVersion_Type(String):
    """Custom type softwareVersion based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SoftwareVersion_Type.__name__ = "String"
_SoftwareVersion_Object = MibTableColumn
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14, 1, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_SoftwareActive_Type = TruthValue
_SoftwareActive_Object = MibTableColumn
softwareActive = _SoftwareActive_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14, 1, 2),
    _SoftwareActive_Type()
)
softwareActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareActive.setStatus("current")
_SoftwareDefault_Type = TruthValue
_SoftwareDefault_Object = MibTableColumn
softwareDefault = _SoftwareDefault_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14, 1, 3),
    _SoftwareDefault_Type()
)
softwareDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareDefault.setStatus("current")
_SoftwarePrevious_Type = TruthValue
_SoftwarePrevious_Object = MibTableColumn
softwarePrevious = _SoftwarePrevious_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14, 1, 4),
    _SoftwarePrevious_Type()
)
softwarePrevious.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwarePrevious.setStatus("current")
_SoftwareTimestamp_Type = DateAndTime
_SoftwareTimestamp_Object = MibTableColumn
softwareTimestamp = _SoftwareTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14, 1, 5),
    _SoftwareTimestamp_Type()
)
softwareTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareTimestamp.setStatus("current")


class _SoftwareConfirmed_Type(String):
    """Custom type softwareConfirmed based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SoftwareConfirmed_Type.__name__ = "String"
_SoftwareConfirmed_Object = MibTableColumn
softwareConfirmed = _SoftwareConfirmed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14, 1, 6),
    _SoftwareConfirmed_Type()
)
softwareConfirmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareConfirmed.setStatus("current")
_SoftwareNext_Type = TruthValue
_SoftwareNext_Object = MibTableColumn
softwareNext = _SoftwareNext_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 14, 1, 7),
    _SoftwareNext_Type()
)
softwareNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareNext.setStatus("current")
_SystemLocalOnDemandTable_Object = MibTable
systemLocalOnDemandTable = _SystemLocalOnDemandTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 15)
)
if mibBuilder.loadTexts:
    systemLocalOnDemandTable.setStatus("current")
_SystemLocalOnDemandEntry_Object = MibTableRow
systemLocalOnDemandEntry = _SystemLocalOnDemandEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 15, 1)
)
systemLocalOnDemandEntry.setIndexNames(
    (1, "VIPTELA-OPER-SYSTEM", "systemLocalOnDemandSystemIP"),
)
if mibBuilder.loadTexts:
    systemLocalOnDemandEntry.setStatus("current")
_SystemLocalOnDemandSystemIP_Type = InetAddressIP
_SystemLocalOnDemandSystemIP_Object = MibTableColumn
systemLocalOnDemandSystemIP = _SystemLocalOnDemandSystemIP_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 15, 1, 1),
    _SystemLocalOnDemandSystemIP_Type()
)
systemLocalOnDemandSystemIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLocalOnDemandSystemIP.setStatus("current")
_SystemLocalOnDemandSiteID_Type = Unsigned32
_SystemLocalOnDemandSiteID_Object = MibTableColumn
systemLocalOnDemandSiteID = _SystemLocalOnDemandSiteID_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 15, 1, 2),
    _SystemLocalOnDemandSiteID_Type()
)
systemLocalOnDemandSiteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLocalOnDemandSiteID.setStatus("current")
_SystemLocalOnDemandOnDemand_Type = String
_SystemLocalOnDemandOnDemand_Object = MibTableColumn
systemLocalOnDemandOnDemand = _SystemLocalOnDemandOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 15, 1, 3),
    _SystemLocalOnDemandOnDemand_Type()
)
systemLocalOnDemandOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLocalOnDemandOnDemand.setStatus("current")
_SystemLocalOnDemandStatus_Type = String
_SystemLocalOnDemandStatus_Object = MibTableColumn
systemLocalOnDemandStatus = _SystemLocalOnDemandStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 15, 1, 4),
    _SystemLocalOnDemandStatus_Type()
)
systemLocalOnDemandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLocalOnDemandStatus.setStatus("current")
_SystemLocalOnDemandIdleTimeoutExpiry_Type = String
_SystemLocalOnDemandIdleTimeoutExpiry_Object = MibTableColumn
systemLocalOnDemandIdleTimeoutExpiry = _SystemLocalOnDemandIdleTimeoutExpiry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 15, 1, 5),
    _SystemLocalOnDemandIdleTimeoutExpiry_Type()
)
systemLocalOnDemandIdleTimeoutExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLocalOnDemandIdleTimeoutExpiry.setStatus("current")
_SystemRemoteOnDemandTable_Object = MibTable
systemRemoteOnDemandTable = _SystemRemoteOnDemandTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 16)
)
if mibBuilder.loadTexts:
    systemRemoteOnDemandTable.setStatus("current")
_SystemRemoteOnDemandEntry_Object = MibTableRow
systemRemoteOnDemandEntry = _SystemRemoteOnDemandEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 16, 1)
)
systemRemoteOnDemandEntry.setIndexNames(
    (1, "VIPTELA-OPER-SYSTEM", "systemRemoteOnDemandSystemIP"),
)
if mibBuilder.loadTexts:
    systemRemoteOnDemandEntry.setStatus("current")
_SystemRemoteOnDemandSystemIP_Type = InetAddressIP
_SystemRemoteOnDemandSystemIP_Object = MibTableColumn
systemRemoteOnDemandSystemIP = _SystemRemoteOnDemandSystemIP_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 16, 1, 1),
    _SystemRemoteOnDemandSystemIP_Type()
)
systemRemoteOnDemandSystemIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRemoteOnDemandSystemIP.setStatus("current")
_SystemRemoteOnDemandSiteID_Type = Unsigned32
_SystemRemoteOnDemandSiteID_Object = MibTableColumn
systemRemoteOnDemandSiteID = _SystemRemoteOnDemandSiteID_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 16, 1, 2),
    _SystemRemoteOnDemandSiteID_Type()
)
systemRemoteOnDemandSiteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRemoteOnDemandSiteID.setStatus("current")
_SystemRemoteOnDemandOnDemand_Type = String
_SystemRemoteOnDemandOnDemand_Object = MibTableColumn
systemRemoteOnDemandOnDemand = _SystemRemoteOnDemandOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 16, 1, 3),
    _SystemRemoteOnDemandOnDemand_Type()
)
systemRemoteOnDemandOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRemoteOnDemandOnDemand.setStatus("current")
_SystemRemoteOnDemandStatus_Type = String
_SystemRemoteOnDemandStatus_Object = MibTableColumn
systemRemoteOnDemandStatus = _SystemRemoteOnDemandStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 16, 1, 4),
    _SystemRemoteOnDemandStatus_Type()
)
systemRemoteOnDemandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRemoteOnDemandStatus.setStatus("current")
_SystemRemoteOnDemandIdleTimeoutExpiry_Type = String
_SystemRemoteOnDemandIdleTimeoutExpiry_Object = MibTableColumn
systemRemoteOnDemandIdleTimeoutExpiry = _SystemRemoteOnDemandIdleTimeoutExpiry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 11, 16, 1, 5),
    _SystemRemoteOnDemandIdleTimeoutExpiry_Type()
)
systemRemoteOnDemandIdleTimeoutExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRemoteOnDemandIdleTimeoutExpiry.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-OPER-SYSTEM",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "Permission1": Permission1,
       "Permission": Permission,
       "viptela-oper-system": viptela_oper_system,
       "systemStatus": systemStatus,
       "systemStatusPersonality": systemStatusPersonality,
       "systemStatusVersion": systemStatusVersion,
       "systemStatusLoghostStatus": systemStatusLoghostStatus,
       "systemStatusLoghostName": systemStatusLoghostName,
       "systemStatusDiskStatus": systemStatusDiskStatus,
       "systemStatusRebootReason": systemStatusRebootReason,
       "systemStatusCoreFilesStatus": systemStatusCoreFilesStatus,
       "systemStatusUptime": systemStatusUptime,
       "systemStatusMin1Avg": systemStatusMin1Avg,
       "systemStatusMin5Avg": systemStatusMin5Avg,
       "systemStatusMin15Avg": systemStatusMin15Avg,
       "systemStatusTotalp": systemStatusTotalp,
       "systemStatusRunningp": systemStatusRunningp,
       "systemStatusCpuUser": systemStatusCpuUser,
       "systemStatusCpuSystem": systemStatusCpuSystem,
       "systemStatusCpuIdle": systemStatusCpuIdle,
       "systemStatusMemTotal": systemStatusMemTotal,
       "systemStatusMemUsed": systemStatusMemUsed,
       "systemStatusMemFree": systemStatusMemFree,
       "systemStatusMemBuffers": systemStatusMemBuffers,
       "systemStatusMemCached": systemStatusMemCached,
       "systemStatusDiskFs": systemStatusDiskFs,
       "systemStatusDiskSize": systemStatusDiskSize,
       "systemStatusDiskUsed": systemStatusDiskUsed,
       "systemStatusDiskAvail": systemStatusDiskAvail,
       "systemStatusDiskUse": systemStatusDiskUse,
       "systemStatusDiskTotalBytes": systemStatusDiskTotalBytes,
       "systemStatusDiskUsedBytes": systemStatusDiskUsedBytes,
       "systemStatusDiskAvailBytes": systemStatusDiskAvailBytes,
       "systemStatusDiskMount": systemStatusDiskMount,
       "systemStatusServices": systemStatusServices,
       "systemStatusBoardType": systemStatusBoardType,
       "systemStatusConfigDateDateTimeString": systemStatusConfigDateDateTimeString,
       "systemStatusCurrentDateDateTimeString": systemStatusCurrentDateDateTimeString,
       "systemStatusStandaloneVbond": systemStatusStandaloneVbond,
       "systemStatusVmanaged": systemStatusVmanaged,
       "systemStatusPseudoConfirmCommit": systemStatusPseudoConfirmCommit,
       "systemStatusConfigTemplateName": systemStatusConfigTemplateName,
       "systemStatusPolicyTemplateName": systemStatusPolicyTemplateName,
       "systemStatusPolicyTemplateVersion": systemStatusPolicyTemplateVersion,
       "systemStatusVmanageStorageDiskFs": systemStatusVmanageStorageDiskFs,
       "systemStatusVmanageStorageDiskSize": systemStatusVmanageStorageDiskSize,
       "systemStatusVmanageStorageDiskUsed": systemStatusVmanageStorageDiskUsed,
       "systemStatusVmanageStorageDiskAvail": systemStatusVmanageStorageDiskAvail,
       "systemStatusVmanageStorageDiskUse": systemStatusVmanageStorageDiskUse,
       "systemStatusVmanageStorageDiskMount": systemStatusVmanageStorageDiskMount,
       "systemStatusModel": systemStatusModel,
       "systemStatusRebootType": systemStatusRebootType,
       "systemStatusTotalCpuCount": systemStatusTotalCpuCount,
       "systemStatusFpCpuCount": systemStatusFpCpuCount,
       "systemStatusLinuxCpuCount": systemStatusLinuxCpuCount,
       "systemStatusBootloaderVersion": systemStatusBootloaderVersion,
       "systemStatusBuildNumber": systemStatusBuildNumber,
       "systemStatusState": systemStatusState,
       "systemStatusSystemStateDescription": systemStatusSystemStateDescription,
       "systemStatusSystemModelSku": systemStatusSystemModelSku,
       "systemStatusTcpdCpuCount": systemStatusTcpdCpuCount,
       "systemStatusSystemFipsMode": systemStatusSystemFipsMode,
       "systemStatusSystemTestbedMode": systemStatusSystemTestbedMode,
       "systemStatusSystemCtrlCompatibility": systemStatusSystemCtrlCompatibility,
       "systemStatusSystemTimezone": systemStatusSystemTimezone,
       "systemStatusSystemEngineeringSigned": systemStatusSystemEngineeringSigned,
       "systemStatusSystemLiLicenseEnabled": systemStatusSystemLiLicenseEnabled,
       "systemStatusSystemChassisSerialNumber": systemStatusSystemChassisSerialNumber,
       "systemStatusProcs": systemStatusProcs,
       "systemStatusDiskBsize": systemStatusDiskBsize,
       "systemStatusDiskBlocks": systemStatusDiskBlocks,
       "systemStatusDiskBused": systemStatusDiskBused,
       "systemStatusDiskBavail": systemStatusDiskBavail,
       "systemStatistics": systemStatistics,
       "systemStatisticsRxPkts": systemStatisticsRxPkts,
       "systemStatisticsRxDrops": systemStatisticsRxDrops,
       "systemStatisticsIpFwd": systemStatisticsIpFwd,
       "systemStatisticsIpFwdMirrorPkts": systemStatisticsIpFwdMirrorPkts,
       "systemStatisticsIpFwdArp": systemStatisticsIpFwdArp,
       "systemStatisticsIpFwdToEgress": systemStatisticsIpFwdToEgress,
       "systemStatisticsIpFwdInvalidOil": systemStatisticsIpFwdInvalidOil,
       "systemStatisticsIpV6McastDrops": systemStatisticsIpV6McastDrops,
       "systemStatisticsIpFwdMcastInvalidIif": systemStatisticsIpFwdMcastInvalidIif,
       "systemStatisticsIpFwdMcastLifeExceededDrops": systemStatisticsIpFwdMcastLifeExceededDrops,
       "systemStatisticsRxMcastThresholdExceeded": systemStatisticsRxMcastThresholdExceeded,
       "systemStatisticsIpFwdInvalidTunOil": systemStatisticsIpFwdInvalidTunOil,
       "systemStatisticsRxMcastPolicyFwdDrops": systemStatisticsRxMcastPolicyFwdDrops,
       "systemStatisticsRxMcastMirrorFwdDrops": systemStatisticsRxMcastMirrorFwdDrops,
       "systemStatisticsIpFwdNullMcastGroup": systemStatisticsIpFwdNullMcastGroup,
       "systemStatisticsIpFwdNullNhop": systemStatisticsIpFwdNullNhop,
       "systemStatisticsIpFwdUnknownNhType": systemStatisticsIpFwdUnknownNhType,
       "systemStatisticsIpFwdNatOnTunnel": systemStatisticsIpFwdNatOnTunnel,
       "systemStatisticsIpFwdToCpu": systemStatisticsIpFwdToCpu,
       "systemStatisticsIpFwdToCpuNatXlates": systemStatisticsIpFwdToCpuNatXlates,
       "systemStatisticsIpFwdFromCpuNatXlates": systemStatisticsIpFwdFromCpuNatXlates,
       "systemStatisticsIpFwdToCpuNatDrops": systemStatisticsIpFwdToCpuNatDrops,
       "systemStatisticsIpFwdFromCpuNonLocal": systemStatisticsIpFwdFromCpuNonLocal,
       "systemStatisticsIpFwdRxIpsec": systemStatisticsIpFwdRxIpsec,
       "systemStatisticsIpFwdMcastPkts": systemStatisticsIpFwdMcastPkts,
       "systemStatisticsIpFwdRxGre": systemStatisticsIpFwdRxGre,
       "systemStatisticsNatXlateOutbound": systemStatisticsNatXlateOutbound,
       "systemStatisticsNatXlateOutboundDrops": systemStatisticsNatXlateOutboundDrops,
       "systemStatisticsNatXlateInbound": systemStatisticsNatXlateInbound,
       "systemStatisticsNatXlateInboundFail": systemStatisticsNatXlateInboundFail,
       "systemStatisticsCflowdPkts": systemStatisticsCflowdPkts,
       "systemStatisticsNoNatNexthop": systemStatisticsNoNatNexthop,
       "systemStatisticsRxBcast": systemStatisticsRxBcast,
       "systemStatisticsRxMcast": systemStatisticsRxMcast,
       "systemStatisticsRxMcastLinkLocal": systemStatisticsRxMcastLinkLocal,
       "systemStatisticsRxMcastFilterToCpu": systemStatisticsRxMcastFilterToCpu,
       "systemStatisticsRxMcastFilterToCpuAndFwd": systemStatisticsRxMcastFilterToCpuAndFwd,
       "systemStatisticsRxGreDecap": systemStatisticsRxGreDecap,
       "systemStatisticsRxGreDrops": systemStatisticsRxGreDrops,
       "systemStatisticsRxGrePolicerDrops": systemStatisticsRxGrePolicerDrops,
       "systemStatisticsRxImplicitAclDrops": systemStatisticsRxImplicitAclDrops,
       "systemStatisticsRxIpsecDecap": systemStatisticsRxIpsecDecap,
       "systemStatisticsRxIp6IpsecDrops": systemStatisticsRxIp6IpsecDrops,
       "systemStatisticsRxSaIpsecDrops": systemStatisticsRxSaIpsecDrops,
       "systemStatisticsRxInvalidIpsecPktSize": systemStatisticsRxInvalidIpsecPktSize,
       "systemStatisticsRxSpiIpsecDrops": systemStatisticsRxSpiIpsecDrops,
       "systemStatisticsRxReplayDrops": systemStatisticsRxReplayDrops,
       "systemStatisticsRxReplayIntegrityDrops": systemStatisticsRxReplayIntegrityDrops,
       "systemStatisticsRxUnexpectedReplayDrops": systemStatisticsRxUnexpectedReplayDrops,
       "systemStatisticsRxNextHdrIpsecDrops": systemStatisticsRxNextHdrIpsecDrops,
       "systemStatisticsRxMacCompareIpsecDrops": systemStatisticsRxMacCompareIpsecDrops,
       "systemStatisticsRxErrPadIpsecDrops": systemStatisticsRxErrPadIpsecDrops,
       "systemStatisticsRxIpsecPolicerDrops": systemStatisticsRxIpsecPolicerDrops,
       "systemStatisticsRxPreIpsecPkts": systemStatisticsRxPreIpsecPkts,
       "systemStatisticsRxPreIpsecDrops": systemStatisticsRxPreIpsecDrops,
       "systemStatisticsRxPreIpsecPolicerDrops": systemStatisticsRxPreIpsecPolicerDrops,
       "systemStatisticsRxPreIpsecDecap": systemStatisticsRxPreIpsecDecap,
       "systemStatisticsOpensslAesDecrypt": systemStatisticsOpensslAesDecrypt,
       "systemStatisticsRxIpsecBadInner": systemStatisticsRxIpsecBadInner,
       "systemStatisticsRxBadLabel": systemStatisticsRxBadLabel,
       "systemStatisticsServiceLabelFwd": systemStatisticsServiceLabelFwd,
       "systemStatisticsRxHostLocalPkt": systemStatisticsRxHostLocalPkt,
       "systemStatisticsRxHostMirrorDrops": systemStatisticsRxHostMirrorDrops,
       "systemStatisticsRxTunneledPkts": systemStatisticsRxTunneledPkts,
       "systemStatisticsRxCpNonLocal": systemStatisticsRxCpNonLocal,
       "systemStatisticsTxIfNotPreferred": systemStatisticsTxIfNotPreferred,
       "systemStatisticsTxVsmartDrop": systemStatisticsTxVsmartDrop,
       "systemStatisticsRxInvalidPort": systemStatisticsRxInvalidPort,
       "systemStatisticsPortDisabledRx": systemStatisticsPortDisabledRx,
       "systemStatisticsIpDisabledRx": systemStatisticsIpDisabledRx,
       "systemStatisticsRxInvalidQtags": systemStatisticsRxInvalidQtags,
       "systemStatisticsRxNonIpDrops": systemStatisticsRxNonIpDrops,
       "systemStatisticsRxIpErrs": systemStatisticsRxIpErrs,
       "systemStatisticsPkoWredDrops": systemStatisticsPkoWredDrops,
       "systemStatisticsTxQueueExceeded": systemStatisticsTxQueueExceeded,
       "systemStatisticsRxPolicerDrops": systemStatisticsRxPolicerDrops,
       "systemStatisticsRouteToHost": systemStatisticsRouteToHost,
       "systemStatisticsTtlExpired": systemStatisticsTtlExpired,
       "systemStatisticsIcmpRedirect": systemStatisticsIcmpRedirect,
       "systemStatisticsBfdRxNonIp": systemStatisticsBfdRxNonIp,
       "systemStatisticsBfdTxRecordChanged": systemStatisticsBfdTxRecordChanged,
       "systemStatisticsBfdRxRecordInvalid": systemStatisticsBfdRxRecordInvalid,
       "systemStatisticsBfdRxParseErr": systemStatisticsBfdRxParseErr,
       "systemStatisticsRxArpRateLimitDrops": systemStatisticsRxArpRateLimitDrops,
       "systemStatisticsRxArpNonLocalDrops": systemStatisticsRxArpNonLocalDrops,
       "systemStatisticsRxArpReqs": systemStatisticsRxArpReqs,
       "systemStatisticsRxArpReplies": systemStatisticsRxArpReplies,
       "systemStatisticsArpAddFail": systemStatisticsArpAddFail,
       "systemStatisticsUnknownNhType": systemStatisticsUnknownNhType,
       "systemStatisticsBufAllocFails": systemStatisticsBufAllocFails,
       "systemStatisticsEcmpDiscards": systemStatisticsEcmpDiscards,
       "systemStatisticsAppRoutePolicyDiscards": systemStatisticsAppRoutePolicyDiscards,
       "systemStatisticsCbfDiscards": systemStatisticsCbfDiscards,
       "systemStatisticsFilterDrops": systemStatisticsFilterDrops,
       "systemStatisticsInvalidBackPtr": systemStatisticsInvalidBackPtr,
       "systemStatisticsTunnelLoopDrops": systemStatisticsTunnelLoopDrops,
       "systemStatisticsToCpuPolicerDrops": systemStatisticsToCpuPolicerDrops,
       "systemStatisticsMirrorDrops": systemStatisticsMirrorDrops,
       "systemStatisticsSplitHorizonDrops": systemStatisticsSplitHorizonDrops,
       "systemStatisticsRxNoTunIf": systemStatisticsRxNoTunIf,
       "systemStatisticsTxPkts": systemStatisticsTxPkts,
       "systemStatisticsTxErrors": systemStatisticsTxErrors,
       "systemStatisticsTxBcast": systemStatisticsTxBcast,
       "systemStatisticsTxMcast": systemStatisticsTxMcast,
       "systemStatisticsPortDisabledTx": systemStatisticsPortDisabledTx,
       "systemStatisticsIpDisabledTx": systemStatisticsIpDisabledTx,
       "systemStatisticsTxFragmentNeeded": systemStatisticsTxFragmentNeeded,
       "systemStatisticsTxMcastFragmentNeeded": systemStatisticsTxMcastFragmentNeeded,
       "systemStatisticsFragmentDfDrops": systemStatisticsFragmentDfDrops,
       "systemStatisticsTxFragments": systemStatisticsTxFragments,
       "systemStatisticsTxFragmentDrops": systemStatisticsTxFragmentDrops,
       "systemStatisticsTxFragmentFail": systemStatisticsTxFragmentFail,
       "systemStatisticsTxFragmentAllocFail": systemStatisticsTxFragmentAllocFail,
       "systemStatisticsTunnelPmtuLowered": systemStatisticsTunnelPmtuLowered,
       "systemStatisticsTxGrePkts": systemStatisticsTxGrePkts,
       "systemStatisticsTxGreDrops": systemStatisticsTxGreDrops,
       "systemStatisticsTxGrePolicerDrops": systemStatisticsTxGrePolicerDrops,
       "systemStatisticsTxGreEncap": systemStatisticsTxGreEncap,
       "systemStatisticsTxIpsecPkts": systemStatisticsTxIpsecPkts,
       "systemStatisticsTxIpsecMcastPkts": systemStatisticsTxIpsecMcastPkts,
       "systemStatisticsTxIp6IpsecDrops": systemStatisticsTxIp6IpsecDrops,
       "systemStatisticsTxNoOutSaIpsecDrops": systemStatisticsTxNoOutSaIpsecDrops,
       "systemStatisticsTxNoTunnIpsecDrops": systemStatisticsTxNoTunnIpsecDrops,
       "systemStatisticsTxIpsecPolicerDrops": systemStatisticsTxIpsecPolicerDrops,
       "systemStatisticsTxIpsecEncap": systemStatisticsTxIpsecEncap,
       "systemStatisticsTxIpsecMcastEncap": systemStatisticsTxIpsecMcastEncap,
       "systemStatisticsTxPreIpsecPkts": systemStatisticsTxPreIpsecPkts,
       "systemStatisticsTxNoOutSaPreIpsecDrops": systemStatisticsTxNoOutSaPreIpsecDrops,
       "systemStatisticsTxNoTunnPreIpsecDrops": systemStatisticsTxNoTunnPreIpsecDrops,
       "systemStatisticsOpensslAesEncrypt": systemStatisticsOpensslAesEncrypt,
       "systemStatisticsTxPreIpsecPolicerDrops": systemStatisticsTxPreIpsecPolicerDrops,
       "systemStatisticsTxPreIpsecEncap": systemStatisticsTxPreIpsecEncap,
       "systemStatisticsTxArpReplies": systemStatisticsTxArpReplies,
       "systemStatisticsTxArpReqs": systemStatisticsTxArpReqs,
       "systemStatisticsTxArpReqFail": systemStatisticsTxArpReqFail,
       "systemStatisticsTxNoArpDrop": systemStatisticsTxNoArpDrop,
       "systemStatisticsTxArpRateLimitDrops": systemStatisticsTxArpRateLimitDrops,
       "systemStatisticsTxIcmpPolicerDrops": systemStatisticsTxIcmpPolicerDrops,
       "systemStatisticsTxIcmpMirroredDrops": systemStatisticsTxIcmpMirroredDrops,
       "systemStatisticsBfdTxFail": systemStatisticsBfdTxFail,
       "systemStatisticsBfdAllocFail": systemStatisticsBfdAllocFail,
       "systemStatisticsBfdTimerAddFail": systemStatisticsBfdTimerAddFail,
       "systemStatisticsBfdTxPkts": systemStatisticsBfdTxPkts,
       "systemStatisticsBfdRxPkts": systemStatisticsBfdRxPkts,
       "systemStatisticsBfdRecDown": systemStatisticsBfdRecDown,
       "systemStatisticsBfdRecInvalid": systemStatisticsBfdRecInvalid,
       "systemStatisticsBfdLkupFail": systemStatisticsBfdLkupFail,
       "systemStatisticsRxIcmpEchoRequests": systemStatisticsRxIcmpEchoRequests,
       "systemStatisticsRxIcmpEchoReplies": systemStatisticsRxIcmpEchoReplies,
       "systemStatisticsRxIcmpNetworkUnreach": systemStatisticsRxIcmpNetworkUnreach,
       "systemStatisticsRxIcmpHostUnreach": systemStatisticsRxIcmpHostUnreach,
       "systemStatisticsRxIcmpPortUnreach": systemStatisticsRxIcmpPortUnreach,
       "systemStatisticsRxIcmpProtocolUnreach": systemStatisticsRxIcmpProtocolUnreach,
       "systemStatisticsRxIcmpFragmentRequired": systemStatisticsRxIcmpFragmentRequired,
       "systemStatisticsRxIcmpDstUnreachOther": systemStatisticsRxIcmpDstUnreachOther,
       "systemStatisticsRxIcmpTtlExpired": systemStatisticsRxIcmpTtlExpired,
       "systemStatisticsRxIcmpRedirect": systemStatisticsRxIcmpRedirect,
       "systemStatisticsRxIcmpSrcQuench": systemStatisticsRxIcmpSrcQuench,
       "systemStatisticsRxIcmpBadIpHdr": systemStatisticsRxIcmpBadIpHdr,
       "systemStatisticsRxIcmpOtherTypes": systemStatisticsRxIcmpOtherTypes,
       "systemStatisticsTxIcmpEchoRequests": systemStatisticsTxIcmpEchoRequests,
       "systemStatisticsTxIcmpEchoReplies": systemStatisticsTxIcmpEchoReplies,
       "systemStatisticsTxIcmpNetworkUnreach": systemStatisticsTxIcmpNetworkUnreach,
       "systemStatisticsTxIcmpHostUnreach": systemStatisticsTxIcmpHostUnreach,
       "systemStatisticsTxIcmpPortUnreach": systemStatisticsTxIcmpPortUnreach,
       "systemStatisticsTxIcmpProtocolUnreach": systemStatisticsTxIcmpProtocolUnreach,
       "systemStatisticsTxIcmpFragmentRequired": systemStatisticsTxIcmpFragmentRequired,
       "systemStatisticsTxIcmpDstUnreachOther": systemStatisticsTxIcmpDstUnreachOther,
       "systemStatisticsTxIcmpTtlExpired": systemStatisticsTxIcmpTtlExpired,
       "systemStatisticsTxIcmpRedirect": systemStatisticsTxIcmpRedirect,
       "systemStatisticsTxIcmpSrcQuench": systemStatisticsTxIcmpSrcQuench,
       "systemStatisticsTxIcmpBadIpHdr": systemStatisticsTxIcmpBadIpHdr,
       "systemStatisticsTxIcmpOtherTypes": systemStatisticsTxIcmpOtherTypes,
       "systemStatisticsGreKaTxPkts": systemStatisticsGreKaTxPkts,
       "systemStatisticsGreKaRxPkts": systemStatisticsGreKaRxPkts,
       "systemStatisticsGreKaTxIpv4OptionsDrop": systemStatisticsGreKaTxIpv4OptionsDrop,
       "systemStatisticsGreKaTxNonIp": systemStatisticsGreKaTxNonIp,
       "systemStatisticsGreKaTxParseErr": systemStatisticsGreKaTxParseErr,
       "systemStatisticsGreKaTxRecordChanged": systemStatisticsGreKaTxRecordChanged,
       "systemStatisticsGreKaTxFail": systemStatisticsGreKaTxFail,
       "systemStatisticsGreKaAllocFail": systemStatisticsGreKaAllocFail,
       "systemStatisticsGreKaTimerAddFail": systemStatisticsGreKaTimerAddFail,
       "systemStatisticsGreKaRxNonIp": systemStatisticsGreKaRxNonIp,
       "systemStatisticsGreKaRxRecInvalid": systemStatisticsGreKaRxRecInvalid,
       "systemStatisticsDot1xRxPkts": systemStatisticsDot1xRxPkts,
       "systemStatisticsDot1xTxPkts": systemStatisticsDot1xTxPkts,
       "systemStatisticsDot1xRxDrops": systemStatisticsDot1xRxDrops,
       "systemStatisticsDot1xTxDrops": systemStatisticsDot1xTxDrops,
       "systemStatisticsDot1xVlanIfNotFoundDrops": systemStatisticsDot1xVlanIfNotFoundDrops,
       "systemStatisticsDot1xMacLearnDrops": systemStatisticsDot1xMacLearnDrops,
       "systemStatisticsRxPolicerRemark": systemStatisticsRxPolicerRemark,
       "systemStatisticsBfdTxOctets": systemStatisticsBfdTxOctets,
       "systemStatisticsBfdRxOctets": systemStatisticsBfdRxOctets,
       "systemStatisticsBfdPmtuTxPkts": systemStatisticsBfdPmtuTxPkts,
       "systemStatisticsBfdPmtuRxPkts": systemStatisticsBfdPmtuRxPkts,
       "systemStatisticsBfdPmtuTxOctets": systemStatisticsBfdPmtuTxOctets,
       "systemStatisticsBfdPmtuRxOctets": systemStatisticsBfdPmtuRxOctets,
       "systemStatisticsDnsReqSnoop": systemStatisticsDnsReqSnoop,
       "systemStatisticsDnsResSnoop": systemStatisticsDnsResSnoop,
       "systemStatisticsCtrlLoopFwd": systemStatisticsCtrlLoopFwd,
       "systemStatisticsCtrlLoopFwdDrops": systemStatisticsCtrlLoopFwdDrops,
       "systemStatisticsRedirectDnsReq": systemStatisticsRedirectDnsReq,
       "systemStatisticsQatAesDecrypt": systemStatisticsQatAesDecrypt,
       "systemStatisticsQatAesEncrypt": systemStatisticsQatAesEncrypt,
       "systemStatisticsQatGcmDecrypt": systemStatisticsQatGcmDecrypt,
       "systemStatisticsQatGcmEncrypt": systemStatisticsQatGcmEncrypt,
       "systemStatisticsOpensslGcmDecrypt": systemStatisticsOpensslGcmDecrypt,
       "systemStatisticsOpensslGcmEncrypt": systemStatisticsOpensslGcmEncrypt,
       "systemStatisticsRxReplayDropsTc0": systemStatisticsRxReplayDropsTc0,
       "systemStatisticsRxReplayDropsTc1": systemStatisticsRxReplayDropsTc1,
       "systemStatisticsRxReplayDropsTc2": systemStatisticsRxReplayDropsTc2,
       "systemStatisticsRxReplayDropsTc3": systemStatisticsRxReplayDropsTc3,
       "systemStatisticsRxReplayDropsTc4": systemStatisticsRxReplayDropsTc4,
       "systemStatisticsRxReplayDropsTc5": systemStatisticsRxReplayDropsTc5,
       "systemStatisticsRxReplayDropsTc6": systemStatisticsRxReplayDropsTc6,
       "systemStatisticsRxReplayDropsTc7": systemStatisticsRxReplayDropsTc7,
       "systemStatisticsRxWindowDropsTc0": systemStatisticsRxWindowDropsTc0,
       "systemStatisticsRxWindowDropsTc1": systemStatisticsRxWindowDropsTc1,
       "systemStatisticsRxWindowDropsTc2": systemStatisticsRxWindowDropsTc2,
       "systemStatisticsRxWindowDropsTc3": systemStatisticsRxWindowDropsTc3,
       "systemStatisticsRxWindowDropsTc4": systemStatisticsRxWindowDropsTc4,
       "systemStatisticsRxWindowDropsTc5": systemStatisticsRxWindowDropsTc5,
       "systemStatisticsRxWindowDropsTc6": systemStatisticsRxWindowDropsTc6,
       "systemStatisticsRxWindowDropsTc7": systemStatisticsRxWindowDropsTc7,
       "systemStatisticsRxUnexpectedReplayDropsTc0": systemStatisticsRxUnexpectedReplayDropsTc0,
       "systemStatisticsRxUnexpectedReplayDropsTc1": systemStatisticsRxUnexpectedReplayDropsTc1,
       "systemStatisticsRxUnexpectedReplayDropsTc2": systemStatisticsRxUnexpectedReplayDropsTc2,
       "systemStatisticsRxUnexpectedReplayDropsTc3": systemStatisticsRxUnexpectedReplayDropsTc3,
       "systemStatisticsRxUnexpectedReplayDropsTc4": systemStatisticsRxUnexpectedReplayDropsTc4,
       "systemStatisticsRxUnexpectedReplayDropsTc5": systemStatisticsRxUnexpectedReplayDropsTc5,
       "systemStatisticsRxUnexpectedReplayDropsTc6": systemStatisticsRxUnexpectedReplayDropsTc6,
       "systemStatisticsRxUnexpectedReplayDropsTc7": systemStatisticsRxUnexpectedReplayDropsTc7,
       "systemStatisticsRxReplayIntegrityDropsTc0": systemStatisticsRxReplayIntegrityDropsTc0,
       "systemStatisticsRxReplayIntegrityDropsTc1": systemStatisticsRxReplayIntegrityDropsTc1,
       "systemStatisticsRxReplayIntegrityDropsTc2": systemStatisticsRxReplayIntegrityDropsTc2,
       "systemStatisticsRxReplayIntegrityDropsTc3": systemStatisticsRxReplayIntegrityDropsTc3,
       "systemStatisticsRxReplayIntegrityDropsTc4": systemStatisticsRxReplayIntegrityDropsTc4,
       "systemStatisticsRxReplayIntegrityDropsTc5": systemStatisticsRxReplayIntegrityDropsTc5,
       "systemStatisticsRxReplayIntegrityDropsTc6": systemStatisticsRxReplayIntegrityDropsTc6,
       "systemStatisticsRxReplayIntegrityDropsTc7": systemStatisticsRxReplayIntegrityDropsTc7,
       "systemStatisticsIcmpRedirectTxDrops": systemStatisticsIcmpRedirectTxDrops,
       "systemStatisticsIcmpRedirectRxDrops": systemStatisticsIcmpRedirectRxDrops,
       "systemStatisticsRxL2MtuExceeded": systemStatisticsRxL2MtuExceeded,
       "systemStatisticsTcpOptTimeoutStateErr": systemStatisticsTcpOptTimeoutStateErr,
       "systemStatisticsTcpOptThirdSynPt": systemStatisticsTcpOptThirdSynPt,
       "systemStatisticsTcpOptInitLimitPt": systemStatisticsTcpOptInitLimitPt,
       "systemStatisticsTcpOptToCpu": systemStatisticsTcpOptToCpu,
       "systemStatisticsTcpOptFromCpu": systemStatisticsTcpOptFromCpu,
       "systemStatisticsTcpOptCtrlInvalidSeq": systemStatisticsTcpOptCtrlInvalidSeq,
       "systemStatisticsTcpOptMboxTotal": systemStatisticsTcpOptMboxTotal,
       "systemStatisticsTcpOptNewFlow": systemStatisticsTcpOptNewFlow,
       "systemStatisticsTcpOptDelFlow": systemStatisticsTcpOptDelFlow,
       "systemStatisticsIpDirectBcastTxDrops": systemStatisticsIpDirectBcastTxDrops,
       "systemStatisticsIpDirectBcastTxL2Bcast": systemStatisticsIpDirectBcastTxL2Bcast,
       "systemStatisticsRxInvalidIpHdr": systemStatisticsRxInvalidIpHdr,
       "systemStatisticsNatDstNatMapInvalid": systemStatisticsNatDstNatMapInvalid,
       "systemStatisticsDevicePolicyDrops": systemStatisticsDevicePolicyDrops,
       "systemStatisticsInvalidLoopHdrDrops": systemStatisticsInvalidLoopHdrDrops,
       "systemStatisticsZbfFragCacheDrops": systemStatisticsZbfFragCacheDrops,
       "systemStatisticsNatFragCacheDrops": systemStatisticsNatFragCacheDrops,
       "systemStatisticsTxTrackerIfNotPreferred": systemStatisticsTxTrackerIfNotPreferred,
       "systemStatisticsIpfragAllfragsSeen": systemStatisticsIpfragAllfragsSeen,
       "systemStatisticsIpfragManyFrags": systemStatisticsIpfragManyFrags,
       "systemStatisticsVRRPMismatchedDMACDrops": systemStatisticsVRRPMismatchedDMACDrops,
       "systemStatisticsDiff": systemStatisticsDiff,
       "systemStatisticsDiffRxPkts": systemStatisticsDiffRxPkts,
       "systemStatisticsDiffRxDrops": systemStatisticsDiffRxDrops,
       "systemStatisticsDiffIpFwd": systemStatisticsDiffIpFwd,
       "systemStatisticsDiffIpFwdMirrorPkts": systemStatisticsDiffIpFwdMirrorPkts,
       "systemStatisticsDiffIpFwdArp": systemStatisticsDiffIpFwdArp,
       "systemStatisticsDiffIpFwdToEgress": systemStatisticsDiffIpFwdToEgress,
       "systemStatisticsDiffIpFwdInvalidOil": systemStatisticsDiffIpFwdInvalidOil,
       "systemStatisticsDiffIpV6McastDrops": systemStatisticsDiffIpV6McastDrops,
       "systemStatisticsDiffIpFwdMcastInvalidIif": systemStatisticsDiffIpFwdMcastInvalidIif,
       "systemStatisticsDiffIpFwdMcastLifeExceededDrops": systemStatisticsDiffIpFwdMcastLifeExceededDrops,
       "systemStatisticsDiffRxMcastThresholdExceeded": systemStatisticsDiffRxMcastThresholdExceeded,
       "systemStatisticsDiffIpFwdInvalidTunOil": systemStatisticsDiffIpFwdInvalidTunOil,
       "systemStatisticsDiffRxMcastPolicyFwdDrops": systemStatisticsDiffRxMcastPolicyFwdDrops,
       "systemStatisticsDiffRxMcastMirrorFwdDrops": systemStatisticsDiffRxMcastMirrorFwdDrops,
       "systemStatisticsDiffIpFwdNullMcastGroup": systemStatisticsDiffIpFwdNullMcastGroup,
       "systemStatisticsDiffIpFwdNullNhop": systemStatisticsDiffIpFwdNullNhop,
       "systemStatisticsDiffIpFwdUnknownNhType": systemStatisticsDiffIpFwdUnknownNhType,
       "systemStatisticsDiffIpFwdNatOnTunnel": systemStatisticsDiffIpFwdNatOnTunnel,
       "systemStatisticsDiffIpFwdToCpu": systemStatisticsDiffIpFwdToCpu,
       "systemStatisticsDiffIpFwdToCpuNatXlates": systemStatisticsDiffIpFwdToCpuNatXlates,
       "systemStatisticsDiffIpFwdFromCpuNatXlates": systemStatisticsDiffIpFwdFromCpuNatXlates,
       "systemStatisticsDiffIpFwdToCpuNatDrops": systemStatisticsDiffIpFwdToCpuNatDrops,
       "systemStatisticsDiffIpFwdFromCpuNonLocal": systemStatisticsDiffIpFwdFromCpuNonLocal,
       "systemStatisticsDiffIpFwdRxIpsec": systemStatisticsDiffIpFwdRxIpsec,
       "systemStatisticsDiffIpFwdMcastPkts": systemStatisticsDiffIpFwdMcastPkts,
       "systemStatisticsDiffIpFwdRxGre": systemStatisticsDiffIpFwdRxGre,
       "systemStatisticsDiffNatXlateOutbound": systemStatisticsDiffNatXlateOutbound,
       "systemStatisticsDiffNatXlateOutboundDrops": systemStatisticsDiffNatXlateOutboundDrops,
       "systemStatisticsDiffNatXlateInbound": systemStatisticsDiffNatXlateInbound,
       "systemStatisticsDiffNatXlateInboundFail": systemStatisticsDiffNatXlateInboundFail,
       "systemStatisticsDiffCflowdPkts": systemStatisticsDiffCflowdPkts,
       "systemStatisticsDiffRxBcast": systemStatisticsDiffRxBcast,
       "systemStatisticsDiffRxMcast": systemStatisticsDiffRxMcast,
       "systemStatisticsDiffRxMcastLinkLocal": systemStatisticsDiffRxMcastLinkLocal,
       "systemStatisticsDiffRxMcastFilterToCpu": systemStatisticsDiffRxMcastFilterToCpu,
       "systemStatisticsDiffRxMcastFilterToCpuAndFwd": systemStatisticsDiffRxMcastFilterToCpuAndFwd,
       "systemStatisticsDiffRxGreDecap": systemStatisticsDiffRxGreDecap,
       "systemStatisticsDiffRxGreDrops": systemStatisticsDiffRxGreDrops,
       "systemStatisticsDiffRxGrePolicerDrops": systemStatisticsDiffRxGrePolicerDrops,
       "systemStatisticsDiffRxImplicitAclDrops": systemStatisticsDiffRxImplicitAclDrops,
       "systemStatisticsDiffRxIpsecDecap": systemStatisticsDiffRxIpsecDecap,
       "systemStatisticsDiffRxIp6IpsecDrops": systemStatisticsDiffRxIp6IpsecDrops,
       "systemStatisticsDiffRxSaIpsecDrops": systemStatisticsDiffRxSaIpsecDrops,
       "systemStatisticsDiffRxInvalidIpsecPktSize": systemStatisticsDiffRxInvalidIpsecPktSize,
       "systemStatisticsDiffRxSpiIpsecDrops": systemStatisticsDiffRxSpiIpsecDrops,
       "systemStatisticsDiffRxReplayDrops": systemStatisticsDiffRxReplayDrops,
       "systemStatisticsDiffRxReplayIntegrityDrops": systemStatisticsDiffRxReplayIntegrityDrops,
       "systemStatisticsDiffRxUnexpectedReplayDrops": systemStatisticsDiffRxUnexpectedReplayDrops,
       "systemStatisticsDiffRxNextHdrIpsecDrops": systemStatisticsDiffRxNextHdrIpsecDrops,
       "systemStatisticsDiffRxMacCompareIpsecDrops": systemStatisticsDiffRxMacCompareIpsecDrops,
       "systemStatisticsDiffRxErrPadIpsecDrops": systemStatisticsDiffRxErrPadIpsecDrops,
       "systemStatisticsDiffRxIpsecPolicerDrops": systemStatisticsDiffRxIpsecPolicerDrops,
       "systemStatisticsDiffRxPreIpsecPkts": systemStatisticsDiffRxPreIpsecPkts,
       "systemStatisticsDiffRxPreIpsecDrops": systemStatisticsDiffRxPreIpsecDrops,
       "systemStatisticsDiffRxPreIpsecPolicerDrops": systemStatisticsDiffRxPreIpsecPolicerDrops,
       "systemStatisticsDiffRxPreIpsecDecap": systemStatisticsDiffRxPreIpsecDecap,
       "systemStatisticsDiffOpensslAesDecrypt": systemStatisticsDiffOpensslAesDecrypt,
       "systemStatisticsDiffRxIpsecBadInner": systemStatisticsDiffRxIpsecBadInner,
       "systemStatisticsDiffRxBadLabel": systemStatisticsDiffRxBadLabel,
       "systemStatisticsDiffServiceLabelFwd": systemStatisticsDiffServiceLabelFwd,
       "systemStatisticsDiffRxHostLocalPkt": systemStatisticsDiffRxHostLocalPkt,
       "systemStatisticsDiffRxHostMirrorDrops": systemStatisticsDiffRxHostMirrorDrops,
       "systemStatisticsDiffRxTunneledPkts": systemStatisticsDiffRxTunneledPkts,
       "systemStatisticsDiffRxCpNonLocal": systemStatisticsDiffRxCpNonLocal,
       "systemStatisticsDiffTxIfNotPreferred": systemStatisticsDiffTxIfNotPreferred,
       "systemStatisticsDiffTxVsmartDrop": systemStatisticsDiffTxVsmartDrop,
       "systemStatisticsDiffRxInvalidPort": systemStatisticsDiffRxInvalidPort,
       "systemStatisticsDiffPortDisabledRx": systemStatisticsDiffPortDisabledRx,
       "systemStatisticsDiffIpDisabledRx": systemStatisticsDiffIpDisabledRx,
       "systemStatisticsDiffRxInvalidQtags": systemStatisticsDiffRxInvalidQtags,
       "systemStatisticsDiffRxNonIpDrops": systemStatisticsDiffRxNonIpDrops,
       "systemStatisticsDiffRxIpErrs": systemStatisticsDiffRxIpErrs,
       "systemStatisticsDiffPkoWredDrops": systemStatisticsDiffPkoWredDrops,
       "systemStatisticsDiffTxQueueExceeded": systemStatisticsDiffTxQueueExceeded,
       "systemStatisticsDiffRxPolicerDrops": systemStatisticsDiffRxPolicerDrops,
       "systemStatisticsDiffRouteToHost": systemStatisticsDiffRouteToHost,
       "systemStatisticsDiffTtlExpired": systemStatisticsDiffTtlExpired,
       "systemStatisticsDiffIcmpRedirect": systemStatisticsDiffIcmpRedirect,
       "systemStatisticsDiffBfdRxNonIp": systemStatisticsDiffBfdRxNonIp,
       "systemStatisticsDiffBfdTxRecordChanged": systemStatisticsDiffBfdTxRecordChanged,
       "systemStatisticsDiffBfdRxRecordInvalid": systemStatisticsDiffBfdRxRecordInvalid,
       "systemStatisticsDiffBfdRxParseErr": systemStatisticsDiffBfdRxParseErr,
       "systemStatisticsDiffRxArpRateLimitDrops": systemStatisticsDiffRxArpRateLimitDrops,
       "systemStatisticsDiffRxArpNonLocalDrops": systemStatisticsDiffRxArpNonLocalDrops,
       "systemStatisticsDiffRxArpReqs": systemStatisticsDiffRxArpReqs,
       "systemStatisticsDiffRxArpReplies": systemStatisticsDiffRxArpReplies,
       "systemStatisticsDiffArpAddFail": systemStatisticsDiffArpAddFail,
       "systemStatisticsDiffUnknownNhType": systemStatisticsDiffUnknownNhType,
       "systemStatisticsDiffBufAllocFails": systemStatisticsDiffBufAllocFails,
       "systemStatisticsDiffEcmpDiscards": systemStatisticsDiffEcmpDiscards,
       "systemStatisticsDiffAppRoutePolicyDiscards": systemStatisticsDiffAppRoutePolicyDiscards,
       "systemStatisticsDiffCbfDiscards": systemStatisticsDiffCbfDiscards,
       "systemStatisticsDiffFilterDrops": systemStatisticsDiffFilterDrops,
       "systemStatisticsDiffInvalidBackPtr": systemStatisticsDiffInvalidBackPtr,
       "systemStatisticsDiffTunnelLoopDrops": systemStatisticsDiffTunnelLoopDrops,
       "systemStatisticsDiffToCpuPolicerDrops": systemStatisticsDiffToCpuPolicerDrops,
       "systemStatisticsDiffMirrorDrops": systemStatisticsDiffMirrorDrops,
       "systemStatisticsDiffSplitHorizonDrops": systemStatisticsDiffSplitHorizonDrops,
       "systemStatisticsDiffRxNoTunIf": systemStatisticsDiffRxNoTunIf,
       "systemStatisticsDiffTxPkts": systemStatisticsDiffTxPkts,
       "systemStatisticsDiffTxErrors": systemStatisticsDiffTxErrors,
       "systemStatisticsDiffTxBcast": systemStatisticsDiffTxBcast,
       "systemStatisticsDiffTxMcast": systemStatisticsDiffTxMcast,
       "systemStatisticsDiffPortDisabledTx": systemStatisticsDiffPortDisabledTx,
       "systemStatisticsDiffIpDisabledTx": systemStatisticsDiffIpDisabledTx,
       "systemStatisticsDiffTxFragmentNeeded": systemStatisticsDiffTxFragmentNeeded,
       "systemStatisticsDiffTxMcastFragmentNeeded": systemStatisticsDiffTxMcastFragmentNeeded,
       "systemStatisticsDiffFragmentDfDrops": systemStatisticsDiffFragmentDfDrops,
       "systemStatisticsDiffTxFragments": systemStatisticsDiffTxFragments,
       "systemStatisticsDiffTxFragmentDrops": systemStatisticsDiffTxFragmentDrops,
       "systemStatisticsDiffTxFragmentFail": systemStatisticsDiffTxFragmentFail,
       "systemStatisticsDiffTxFragmentAllocFail": systemStatisticsDiffTxFragmentAllocFail,
       "systemStatisticsDiffTunnelPmtuLowered": systemStatisticsDiffTunnelPmtuLowered,
       "systemStatisticsDiffTxGrePkts": systemStatisticsDiffTxGrePkts,
       "systemStatisticsDiffTxGreDrops": systemStatisticsDiffTxGreDrops,
       "systemStatisticsDiffTxGrePolicerDrops": systemStatisticsDiffTxGrePolicerDrops,
       "systemStatisticsDiffTxGreEncap": systemStatisticsDiffTxGreEncap,
       "systemStatisticsDiffTxIpsecPkts": systemStatisticsDiffTxIpsecPkts,
       "systemStatisticsDiffTxIpsecMcastPkts": systemStatisticsDiffTxIpsecMcastPkts,
       "systemStatisticsDiffTxIp6IpsecDrops": systemStatisticsDiffTxIp6IpsecDrops,
       "systemStatisticsDiffTxNoOutSaIpsecDrops": systemStatisticsDiffTxNoOutSaIpsecDrops,
       "systemStatisticsDiffTxNoTunnIpsecDrops": systemStatisticsDiffTxNoTunnIpsecDrops,
       "systemStatisticsDiffTxIpsecPolicerDrops": systemStatisticsDiffTxIpsecPolicerDrops,
       "systemStatisticsDiffTxIpsecEncap": systemStatisticsDiffTxIpsecEncap,
       "systemStatisticsDiffTxIpsecMcastEncap": systemStatisticsDiffTxIpsecMcastEncap,
       "systemStatisticsDiffTxPreIpsecPkts": systemStatisticsDiffTxPreIpsecPkts,
       "systemStatisticsDiffTxNoOutSaPreIpsecDrops": systemStatisticsDiffTxNoOutSaPreIpsecDrops,
       "systemStatisticsDiffTxNoTunnPreIpsecDrops": systemStatisticsDiffTxNoTunnPreIpsecDrops,
       "systemStatisticsDiffOpensslAesEncrypt": systemStatisticsDiffOpensslAesEncrypt,
       "systemStatisticsDiffTxPreIpsecPolicerDrops": systemStatisticsDiffTxPreIpsecPolicerDrops,
       "systemStatisticsDiffTxPreIpsecEncap": systemStatisticsDiffTxPreIpsecEncap,
       "systemStatisticsDiffTxArpReplies": systemStatisticsDiffTxArpReplies,
       "systemStatisticsDiffTxArpReqs": systemStatisticsDiffTxArpReqs,
       "systemStatisticsDiffTxArpReqFail": systemStatisticsDiffTxArpReqFail,
       "systemStatisticsDiffTxNoArpDrop": systemStatisticsDiffTxNoArpDrop,
       "systemStatisticsDiffTxArpRateLimitDrops": systemStatisticsDiffTxArpRateLimitDrops,
       "systemStatisticsDiffTxIcmpPolicerDrops": systemStatisticsDiffTxIcmpPolicerDrops,
       "systemStatisticsDiffTxIcmpMirroredDrops": systemStatisticsDiffTxIcmpMirroredDrops,
       "systemStatisticsDiffBfdTxFail": systemStatisticsDiffBfdTxFail,
       "systemStatisticsDiffBfdAllocFail": systemStatisticsDiffBfdAllocFail,
       "systemStatisticsDiffBfdTimerAddFail": systemStatisticsDiffBfdTimerAddFail,
       "systemStatisticsDiffBfdTxPkts": systemStatisticsDiffBfdTxPkts,
       "systemStatisticsDiffBfdRxPkts": systemStatisticsDiffBfdRxPkts,
       "systemStatisticsDiffBfdRecDown": systemStatisticsDiffBfdRecDown,
       "systemStatisticsDiffBfdRecInvalid": systemStatisticsDiffBfdRecInvalid,
       "systemStatisticsDiffBfdLkupFail": systemStatisticsDiffBfdLkupFail,
       "systemStatisticsDiffRxIcmpEchoRequests": systemStatisticsDiffRxIcmpEchoRequests,
       "systemStatisticsDiffRxIcmpEchoReplies": systemStatisticsDiffRxIcmpEchoReplies,
       "systemStatisticsDiffRxIcmpNetworkUnreach": systemStatisticsDiffRxIcmpNetworkUnreach,
       "systemStatisticsDiffRxIcmpHostUnreach": systemStatisticsDiffRxIcmpHostUnreach,
       "systemStatisticsDiffRxIcmpPortUnreach": systemStatisticsDiffRxIcmpPortUnreach,
       "systemStatisticsDiffRxIcmpProtocolUnreach": systemStatisticsDiffRxIcmpProtocolUnreach,
       "systemStatisticsDiffRxIcmpFragmentRequired": systemStatisticsDiffRxIcmpFragmentRequired,
       "systemStatisticsDiffRxIcmpDstUnreachOther": systemStatisticsDiffRxIcmpDstUnreachOther,
       "systemStatisticsDiffRxIcmpTtlExpired": systemStatisticsDiffRxIcmpTtlExpired,
       "systemStatisticsDiffRxIcmpRedirect": systemStatisticsDiffRxIcmpRedirect,
       "systemStatisticsDiffRxIcmpSrcQuench": systemStatisticsDiffRxIcmpSrcQuench,
       "systemStatisticsDiffRxIcmpBadIpHdr": systemStatisticsDiffRxIcmpBadIpHdr,
       "systemStatisticsDiffRxIcmpOtherTypes": systemStatisticsDiffRxIcmpOtherTypes,
       "systemStatisticsDiffTxIcmpEchoRequests": systemStatisticsDiffTxIcmpEchoRequests,
       "systemStatisticsDiffTxIcmpEchoReplies": systemStatisticsDiffTxIcmpEchoReplies,
       "systemStatisticsDiffTxIcmpNetworkUnreach": systemStatisticsDiffTxIcmpNetworkUnreach,
       "systemStatisticsDiffTxIcmpHostUnreach": systemStatisticsDiffTxIcmpHostUnreach,
       "systemStatisticsDiffTxIcmpPortUnreach": systemStatisticsDiffTxIcmpPortUnreach,
       "systemStatisticsDiffTxIcmpProtocolUnreach": systemStatisticsDiffTxIcmpProtocolUnreach,
       "systemStatisticsDiffTxIcmpFragmentRequired": systemStatisticsDiffTxIcmpFragmentRequired,
       "systemStatisticsDiffTxIcmpDstUnreachOther": systemStatisticsDiffTxIcmpDstUnreachOther,
       "systemStatisticsDiffTxIcmpTtlExpired": systemStatisticsDiffTxIcmpTtlExpired,
       "systemStatisticsDiffTxIcmpRedirect": systemStatisticsDiffTxIcmpRedirect,
       "systemStatisticsDiffTxIcmpSrcQuench": systemStatisticsDiffTxIcmpSrcQuench,
       "systemStatisticsDiffTxIcmpBadIpHdr": systemStatisticsDiffTxIcmpBadIpHdr,
       "systemStatisticsDiffTxIcmpOtherTypes": systemStatisticsDiffTxIcmpOtherTypes,
       "systemStatisticsDiffGreKaTxPkts": systemStatisticsDiffGreKaTxPkts,
       "systemStatisticsDiffGreKaRxPkts": systemStatisticsDiffGreKaRxPkts,
       "systemStatisticsDiffGreKaTxIpv4OptionsDrop": systemStatisticsDiffGreKaTxIpv4OptionsDrop,
       "systemStatisticsDiffGreKaTxNonIp": systemStatisticsDiffGreKaTxNonIp,
       "systemStatisticsDiffGreKaTxParseErr": systemStatisticsDiffGreKaTxParseErr,
       "systemStatisticsDiffGreKaTxRecordChanged": systemStatisticsDiffGreKaTxRecordChanged,
       "systemStatisticsDiffGreKaTxFail": systemStatisticsDiffGreKaTxFail,
       "systemStatisticsDiffGreKaAllocFail": systemStatisticsDiffGreKaAllocFail,
       "systemStatisticsDiffGreKaTimerAddFail": systemStatisticsDiffGreKaTimerAddFail,
       "systemStatisticsDiffGreKaRxNonIp": systemStatisticsDiffGreKaRxNonIp,
       "systemStatisticsDiffGreKaRxRecInvalid": systemStatisticsDiffGreKaRxRecInvalid,
       "systemStatisticsDiffDot1xRxPkts": systemStatisticsDiffDot1xRxPkts,
       "systemStatisticsDiffDot1xTxPkts": systemStatisticsDiffDot1xTxPkts,
       "systemStatisticsDiffDot1xRxDrops": systemStatisticsDiffDot1xRxDrops,
       "systemStatisticsDiffDot1xTxDrops": systemStatisticsDiffDot1xTxDrops,
       "systemStatisticsDiffDot1xVlanIfNotFoundDrops": systemStatisticsDiffDot1xVlanIfNotFoundDrops,
       "systemStatisticsDiffDot1xMacLearnDrops": systemStatisticsDiffDot1xMacLearnDrops,
       "systemStatisticsDiffRxPolicerRemark": systemStatisticsDiffRxPolicerRemark,
       "systemStatisticsDiffBfdTxOctets": systemStatisticsDiffBfdTxOctets,
       "systemStatisticsDiffBfdRxOctets": systemStatisticsDiffBfdRxOctets,
       "systemStatisticsDiffBfdPmtuTxPkts": systemStatisticsDiffBfdPmtuTxPkts,
       "systemStatisticsDiffBfdPmtuRxPkts": systemStatisticsDiffBfdPmtuRxPkts,
       "systemStatisticsDiffBfdPmtuTxOctets": systemStatisticsDiffBfdPmtuTxOctets,
       "systemStatisticsDiffBfdPmtuRxOctets": systemStatisticsDiffBfdPmtuRxOctets,
       "systemStatisticsDiffDnsReqSnoop": systemStatisticsDiffDnsReqSnoop,
       "systemStatisticsDiffDnsResSnoop": systemStatisticsDiffDnsResSnoop,
       "systemStatisticsDiffCtrlLoopFwd": systemStatisticsDiffCtrlLoopFwd,
       "systemStatisticsDiffCtrlLoopFwdDrops": systemStatisticsDiffCtrlLoopFwdDrops,
       "systemStatisticsDiffQatAesDecrypt": systemStatisticsDiffQatAesDecrypt,
       "systemStatisticsDiffQatAesEncrypt": systemStatisticsDiffQatAesEncrypt,
       "systemStatisticsDiffQatGcmDecrypt": systemStatisticsDiffQatGcmDecrypt,
       "systemStatisticsDiffQatGcmEncrypt": systemStatisticsDiffQatGcmEncrypt,
       "systemStatisticsDiffOpensslGcmDecrypt": systemStatisticsDiffOpensslGcmDecrypt,
       "systemStatisticsDiffOpensslGcmEncrypt": systemStatisticsDiffOpensslGcmEncrypt,
       "systemStatisticsDiffRxReplayDropsTc0": systemStatisticsDiffRxReplayDropsTc0,
       "systemStatisticsDiffRxReplayDropsTc1": systemStatisticsDiffRxReplayDropsTc1,
       "systemStatisticsDiffRxReplayDropsTc2": systemStatisticsDiffRxReplayDropsTc2,
       "systemStatisticsDiffRxReplayDropsTc3": systemStatisticsDiffRxReplayDropsTc3,
       "systemStatisticsDiffRxReplayDropsTc4": systemStatisticsDiffRxReplayDropsTc4,
       "systemStatisticsDiffRxReplayDropsTc5": systemStatisticsDiffRxReplayDropsTc5,
       "systemStatisticsDiffRxReplayDropsTc6": systemStatisticsDiffRxReplayDropsTc6,
       "systemStatisticsDiffRxReplayDropsTc7": systemStatisticsDiffRxReplayDropsTc7,
       "systemStatisticsDiffRxWindowDropsTc0": systemStatisticsDiffRxWindowDropsTc0,
       "systemStatisticsDiffRxWindowDropsTc1": systemStatisticsDiffRxWindowDropsTc1,
       "systemStatisticsDiffRxWindowDropsTc2": systemStatisticsDiffRxWindowDropsTc2,
       "systemStatisticsDiffRxWindowDropsTc3": systemStatisticsDiffRxWindowDropsTc3,
       "systemStatisticsDiffRxWindowDropsTc4": systemStatisticsDiffRxWindowDropsTc4,
       "systemStatisticsDiffRxWindowDropsTc5": systemStatisticsDiffRxWindowDropsTc5,
       "systemStatisticsDiffRxWindowDropsTc6": systemStatisticsDiffRxWindowDropsTc6,
       "systemStatisticsDiffRxWindowDropsTc7": systemStatisticsDiffRxWindowDropsTc7,
       "systemStatisticsDiffRxUnexpectedReplayDropsTc0": systemStatisticsDiffRxUnexpectedReplayDropsTc0,
       "systemStatisticsDiffRxUnexpectedReplayDropsTc1": systemStatisticsDiffRxUnexpectedReplayDropsTc1,
       "systemStatisticsDiffRxUnexpectedReplayDropsTc2": systemStatisticsDiffRxUnexpectedReplayDropsTc2,
       "systemStatisticsDiffRxUnexpectedReplayDropsTc3": systemStatisticsDiffRxUnexpectedReplayDropsTc3,
       "systemStatisticsDiffRxUnexpectedReplayDropsTc4": systemStatisticsDiffRxUnexpectedReplayDropsTc4,
       "systemStatisticsDiffRxUnexpectedReplayDropsTc5": systemStatisticsDiffRxUnexpectedReplayDropsTc5,
       "systemStatisticsDiffRxUnexpectedReplayDropsTc6": systemStatisticsDiffRxUnexpectedReplayDropsTc6,
       "systemStatisticsDiffRxUnexpectedReplayDropsTc7": systemStatisticsDiffRxUnexpectedReplayDropsTc7,
       "systemStatisticsDiffRxReplayIntegrityDropsTc0": systemStatisticsDiffRxReplayIntegrityDropsTc0,
       "systemStatisticsDiffRxReplayIntegrityDropsTc1": systemStatisticsDiffRxReplayIntegrityDropsTc1,
       "systemStatisticsDiffRxReplayIntegrityDropsTc2": systemStatisticsDiffRxReplayIntegrityDropsTc2,
       "systemStatisticsDiffRxReplayIntegrityDropsTc3": systemStatisticsDiffRxReplayIntegrityDropsTc3,
       "systemStatisticsDiffRxReplayIntegrityDropsTc4": systemStatisticsDiffRxReplayIntegrityDropsTc4,
       "systemStatisticsDiffRxReplayIntegrityDropsTc5": systemStatisticsDiffRxReplayIntegrityDropsTc5,
       "systemStatisticsDiffRxReplayIntegrityDropsTc6": systemStatisticsDiffRxReplayIntegrityDropsTc6,
       "systemStatisticsDiffRxReplayIntegrityDropsTc7": systemStatisticsDiffRxReplayIntegrityDropsTc7,
       "systemStatisticsDiffIcmpRedirectTxDrops": systemStatisticsDiffIcmpRedirectTxDrops,
       "systemStatisticsDiffIcmpRedirectRxDrops": systemStatisticsDiffIcmpRedirectRxDrops,
       "systemStatisticsDiffRxL2MtuExceeded": systemStatisticsDiffRxL2MtuExceeded,
       "systemStatisticsDiffIpDirectBcastTxDrops": systemStatisticsDiffIpDirectBcastTxDrops,
       "systemStatisticsDiffIpDirectBcastTxL2Bcast": systemStatisticsDiffIpDirectBcastTxL2Bcast,
       "systemStatisticsDiffRxInvalidIpHdr": systemStatisticsDiffRxInvalidIpHdr,
       "systemStatisticsDiffNatDstNatMapInvalid": systemStatisticsDiffNatDstNatMapInvalid,
       "systemStatisticsDiffDevicePolicyDrops": systemStatisticsDiffDevicePolicyDrops,
       "systemStatisticsDiffInvalidLoopHdrDrops": systemStatisticsDiffInvalidLoopHdrDrops,
       "systemStatisticsDiffZbfFragCacheDrops": systemStatisticsDiffZbfFragCacheDrops,
       "systemStatisticsDiffNatFragCacheDrops": systemStatisticsDiffNatFragCacheDrops,
       "systemStatisticsDiffTxTrackerIfNotPreferred": systemStatisticsDiffTxTrackerIfNotPreferred,
       "systemStatisticsDiffIpfragAllfragsSeen": systemStatisticsDiffIpfragAllfragsSeen,
       "systemStatisticsDiffIpfragManyFrags": systemStatisticsDiffIpfragManyFrags,
       "systemStatisticsDiffVRRPMismatchedDMACDrops": systemStatisticsDiffVRRPMismatchedDMACDrops,
       "reboot": reboot,
       "rebootHistoryTable": rebootHistoryTable,
       "rebootHistoryEntry": rebootHistoryEntry,
       "rebootHistoryRebootDateTime": rebootHistoryRebootDateTime,
       "rebootHistoryRebootReason": rebootHistoryRebootReason,
       "bootPartitionTable": bootPartitionTable,
       "bootPartitionEntry": bootPartitionEntry,
       "bootPartitionPartition": bootPartitionPartition,
       "bootPartitionActive": bootPartitionActive,
       "bootPartitionVersion": bootPartitionVersion,
       "bootPartitionTimestamp": bootPartitionTimestamp,
       "usersTable": usersTable,
       "usersEntry": usersEntry,
       "usersSession": usersSession,
       "usersUser": usersUser,
       "usersContext": usersContext,
       "usersFrom": usersFrom,
       "usersProto": usersProto,
       "usersAuthGroup": usersAuthGroup,
       "usersLoginTime": usersLoginTime,
       "aaa": aaa,
       "aaaUsergroupTable": aaaUsergroupTable,
       "aaaUsergroupEntry": aaaUsergroupEntry,
       "aaaUsergroupName": aaaUsergroupName,
       "aaaUsergroupTaskTable": aaaUsergroupTaskTable,
       "aaaUsergroupTaskEntry": aaaUsergroupTaskEntry,
       "aaaUsergroupTaskMode": aaaUsergroupTaskMode,
       "aaaUsergroupTaskPermission": aaaUsergroupTaskPermission,
       "logging": logging,
       "loggingHostStatus": loggingHostStatus,
       "loggingHostName": loggingHostName,
       "loggingHostPriority": loggingHostPriority,
       "loggingHostVpnId": loggingHostVpnId,
       "loggingDiskStatus": loggingDiskStatus,
       "loggingDiskPriority": loggingDiskPriority,
       "loggingDiskFilename": loggingDiskFilename,
       "loggingDiskFilesize": loggingDiskFilesize,
       "loggingDiskFilerotate": loggingDiskFilerotate,
       "ntp": ntp,
       "ntpPeerTable": ntpPeerTable,
       "ntpPeerEntry": ntpPeerEntry,
       "ntpPeerIndex": ntpPeerIndex,
       "ntpPeerRemote": ntpPeerRemote,
       "ntpPeerRefid": ntpPeerRefid,
       "ntpPeerSt": ntpPeerSt,
       "ntpPeerType": ntpPeerType,
       "ntpPeerWhen": ntpPeerWhen,
       "ntpPeerPoll": ntpPeerPoll,
       "ntpPeerReach": ntpPeerReach,
       "ntpPeerDelay": ntpPeerDelay,
       "ntpPeerOffset": ntpPeerOffset,
       "ntpPeerJitter": ntpPeerJitter,
       "ntpAssociationsTable": ntpAssociationsTable,
       "ntpAssociationsEntry": ntpAssociationsEntry,
       "ntpAssociationsIdx": ntpAssociationsIdx,
       "ntpAssociationsAssocid": ntpAssociationsAssocid,
       "ntpAssociationsStatus": ntpAssociationsStatus,
       "ntpAssociationsConf": ntpAssociationsConf,
       "ntpAssociationsReachability": ntpAssociationsReachability,
       "ntpAssociationsAuth": ntpAssociationsAuth,
       "ntpAssociationsCondition": ntpAssociationsCondition,
       "ntpAssociationsLastEvent": ntpAssociationsLastEvent,
       "ntpAssociationsCount": ntpAssociationsCount,
       "ntpRefid": ntpRefid,
       "ntpReftime": ntpReftime,
       "ntpStratum": ntpStratum,
       "ntpRootdelay": ntpRootdelay,
       "ntpRootdisp": ntpRootdisp,
       "ntpFreqDriftPpm": ntpFreqDriftPpm,
       "ntpPollInterval": ntpPollInterval,
       "ntpOffset": ntpOffset,
       "transport": transport,
       "transportConnectionTable": transportConnectionTable,
       "transportConnectionEntry": transportConnectionEntry,
       "transportConnectionTrackType": transportConnectionTrackType,
       "transportConnectionSource": transportConnectionSource,
       "transportConnectionDestination": transportConnectionDestination,
       "transportConnectionHost": transportConnectionHost,
       "transportConnectionHistoryTable": transportConnectionHistoryTable,
       "transportConnectionHistoryEntry": transportConnectionHistoryEntry,
       "transportConnectionHistoryIndex": transportConnectionHistoryIndex,
       "transportConnectionHistoryTime": transportConnectionHistoryTime,
       "transportConnectionHistoryState": transportConnectionHistoryState,
       "crashTable": crashTable,
       "crashEntry": crashEntry,
       "crashIndex": crashIndex,
       "crashCoreTime": crashCoreTime,
       "crashCoreFilename": crashCoreFilename,
       "softwareTable": softwareTable,
       "softwareEntry": softwareEntry,
       "softwareVersion": softwareVersion,
       "softwareActive": softwareActive,
       "softwareDefault": softwareDefault,
       "softwarePrevious": softwarePrevious,
       "softwareTimestamp": softwareTimestamp,
       "softwareConfirmed": softwareConfirmed,
       "softwareNext": softwareNext,
       "systemLocalOnDemandTable": systemLocalOnDemandTable,
       "systemLocalOnDemandEntry": systemLocalOnDemandEntry,
       "systemLocalOnDemandSystemIP": systemLocalOnDemandSystemIP,
       "systemLocalOnDemandSiteID": systemLocalOnDemandSiteID,
       "systemLocalOnDemandOnDemand": systemLocalOnDemandOnDemand,
       "systemLocalOnDemandStatus": systemLocalOnDemandStatus,
       "systemLocalOnDemandIdleTimeoutExpiry": systemLocalOnDemandIdleTimeoutExpiry,
       "systemRemoteOnDemandTable": systemRemoteOnDemandTable,
       "systemRemoteOnDemandEntry": systemRemoteOnDemandEntry,
       "systemRemoteOnDemandSystemIP": systemRemoteOnDemandSystemIP,
       "systemRemoteOnDemandSiteID": systemRemoteOnDemandSiteID,
       "systemRemoteOnDemandOnDemand": systemRemoteOnDemandOnDemand,
       "systemRemoteOnDemandStatus": systemRemoteOnDemandStatus,
       "systemRemoteOnDemandIdleTimeoutExpiry": systemRemoteOnDemandIdleTimeoutExpiry}
)
