# SNMP MIB module (BCN-TFTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-TFTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:31 2025
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

(bcnServices,) = mibBuilder.importSymbols(
    "BCN-SMI-MIB",
    "bcnServices")

(BcnAlarmSeverity,) = mibBuilder.importSymbols(
    "BCN-TC-MIB",
    "BcnAlarmSeverity")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bcnTftpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bcnTftpMIB.setRevisions(
        ("2010-11-30 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnTftp_ObjectIdentity = ObjectIdentity
bcnTftp = _BcnTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3)
)
_BcnTftpObjects_ObjectIdentity = ObjectIdentity
bcnTftpObjects = _BcnTftpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2)
)
_BcnTftpServiceStatus_ObjectIdentity = ObjectIdentity
bcnTftpServiceStatus = _BcnTftpServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    bcnTftpServiceStatus.setStatus("current")


class _BcnTftpSerOperState_Type(Integer32):
    """Custom type bcnTftpSerOperState based on Integer32"""
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
        *(("running", 1),
          ("notRunning", 2),
          ("starting", 3),
          ("stopping", 4),
          ("fault", 5))
    )


_BcnTftpSerOperState_Type.__name__ = "Integer32"
_BcnTftpSerOperState_Object = MibScalar
bcnTftpSerOperState = _BcnTftpSerOperState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 1, 1),
    _BcnTftpSerOperState_Type()
)
bcnTftpSerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnTftpSerOperState.setStatus("current")
_BcnTftpServiceStatistics_ObjectIdentity = ObjectIdentity
bcnTftpServiceStatistics = _BcnTftpServiceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    bcnTftpServiceStatistics.setStatus("current")
_BcnTftpSerDirs_Type = Unsigned32
_BcnTftpSerDirs_Object = MibScalar
bcnTftpSerDirs = _BcnTftpSerDirs_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2, 1),
    _BcnTftpSerDirs_Type()
)
bcnTftpSerDirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnTftpSerDirs.setStatus("current")
_BcnTftpSerFiles_Type = Unsigned32
_BcnTftpSerFiles_Object = MibScalar
bcnTftpSerFiles = _BcnTftpSerFiles_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2, 2),
    _BcnTftpSerFiles_Type()
)
bcnTftpSerFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnTftpSerFiles.setStatus("current")
_BcnTftpSerFilesSize_Type = Unsigned32
_BcnTftpSerFilesSize_Object = MibScalar
bcnTftpSerFilesSize = _BcnTftpSerFilesSize_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2, 3),
    _BcnTftpSerFilesSize_Type()
)
bcnTftpSerFilesSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnTftpSerFilesSize.setStatus("current")
if mibBuilder.loadTexts:
    bcnTftpSerFilesSize.setUnits("KBytes")
_BcnTftpSerPartialList_Type = TruthValue
_BcnTftpSerPartialList_Object = MibScalar
bcnTftpSerPartialList = _BcnTftpSerPartialList_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2, 4),
    _BcnTftpSerPartialList_Type()
)
bcnTftpSerPartialList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnTftpSerPartialList.setStatus("current")
_BcnTftpNotification_ObjectIdentity = ObjectIdentity
bcnTftpNotification = _BcnTftpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3)
)
_BcnTftpNotificationEvents_ObjectIdentity = ObjectIdentity
bcnTftpNotificationEvents = _BcnTftpNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 0)
)
_BcnTftpNotificationData_ObjectIdentity = ObjectIdentity
bcnTftpNotificationData = _BcnTftpNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 1)
)
_BcnTftpAlarmSeverity_Type = BcnAlarmSeverity
_BcnTftpAlarmSeverity_Object = MibScalar
bcnTftpAlarmSeverity = _BcnTftpAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 1, 1),
    _BcnTftpAlarmSeverity_Type()
)
bcnTftpAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnTftpAlarmSeverity.setStatus("current")
_BcnTftpAlarmInfo_Type = DisplayString
_BcnTftpAlarmInfo_Object = MibScalar
bcnTftpAlarmInfo = _BcnTftpAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 1, 2),
    _BcnTftpAlarmInfo_Type()
)
bcnTftpAlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnTftpAlarmInfo.setStatus("current")
_BcnTftpConformance_ObjectIdentity = ObjectIdentity
bcnTftpConformance = _BcnTftpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4)
)
_BcnTftpServiceCompliances_ObjectIdentity = ObjectIdentity
bcnTftpServiceCompliances = _BcnTftpServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 1)
)
_BcnTftpServiceGroups_ObjectIdentity = ObjectIdentity
bcnTftpServiceGroups = _BcnTftpServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 2)
)

# Managed Objects groups

bcnTftpServiceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 2, 1)
)
bcnTftpServiceStatusGroup.setObjects(
      *(("BCN-TFTP-MIB", "bcnTftpSerOperState"),
        ("BCN-TFTP-MIB", "bcnTftpSerDirs"),
        ("BCN-TFTP-MIB", "bcnTftpSerFiles"),
        ("BCN-TFTP-MIB", "bcnTftpSerFilesSize"),
        ("BCN-TFTP-MIB", "bcnTftpSerPartialList"))
)
if mibBuilder.loadTexts:
    bcnTftpServiceStatusGroup.setStatus("current")

bcnTftpNotificationDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 2, 3)
)
bcnTftpNotificationDataGroup.setObjects(
      *(("BCN-TFTP-MIB", "bcnTftpAlarmSeverity"),
        ("BCN-TFTP-MIB", "bcnTftpAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnTftpNotificationDataGroup.setStatus("current")


# Notification objects

bcnTftpAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 0, 1)
)
bcnTftpAlarmNotif.setObjects(
      *(("BCN-TFTP-MIB", "bcnTftpSerOperState"),
        ("BCN-TFTP-MIB", "bcnTftpAlarmSeverity"),
        ("BCN-TFTP-MIB", "bcnTftpAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnTftpAlarmNotif.setStatus(
        "current"
    )


# Notifications groups

bcnTftpNotificationEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 2, 2)
)
bcnTftpNotificationEventGroup.setObjects(
    ("BCN-TFTP-MIB", "bcnTftpAlarmNotif")
)
if mibBuilder.loadTexts:
    bcnTftpNotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcnTftpStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 1, 1)
)
bcnTftpStatusCompliance.setObjects(
      *(("BCN-TFTP-MIB", "bcnTftpServiceStatusGroup"),
        ("BCN-TFTP-MIB", "bcnTftpNotificationEventGroup"),
        ("BCN-TFTP-MIB", "bcnTftpNotificationDataGroup"))
)
if mibBuilder.loadTexts:
    bcnTftpStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-TFTP-MIB",
    **{"bcnTftp": bcnTftp,
       "bcnTftpMIB": bcnTftpMIB,
       "bcnTftpObjects": bcnTftpObjects,
       "bcnTftpServiceStatus": bcnTftpServiceStatus,
       "bcnTftpSerOperState": bcnTftpSerOperState,
       "bcnTftpServiceStatistics": bcnTftpServiceStatistics,
       "bcnTftpSerDirs": bcnTftpSerDirs,
       "bcnTftpSerFiles": bcnTftpSerFiles,
       "bcnTftpSerFilesSize": bcnTftpSerFilesSize,
       "bcnTftpSerPartialList": bcnTftpSerPartialList,
       "bcnTftpNotification": bcnTftpNotification,
       "bcnTftpNotificationEvents": bcnTftpNotificationEvents,
       "bcnTftpAlarmNotif": bcnTftpAlarmNotif,
       "bcnTftpNotificationData": bcnTftpNotificationData,
       "bcnTftpAlarmSeverity": bcnTftpAlarmSeverity,
       "bcnTftpAlarmInfo": bcnTftpAlarmInfo,
       "bcnTftpConformance": bcnTftpConformance,
       "bcnTftpServiceCompliances": bcnTftpServiceCompliances,
       "bcnTftpStatusCompliance": bcnTftpStatusCompliance,
       "bcnTftpServiceGroups": bcnTftpServiceGroups,
       "bcnTftpServiceStatusGroup": bcnTftpServiceStatusGroup,
       "bcnTftpNotificationEventGroup": bcnTftpNotificationEventGroup,
       "bcnTftpNotificationDataGroup": bcnTftpNotificationDataGroup}
)
