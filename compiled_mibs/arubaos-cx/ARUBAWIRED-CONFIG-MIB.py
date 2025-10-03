# SNMP MIB module (ARUBAWIRED-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:05 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

arubaWiredConfigurationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20)
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationMIB.setRevisions(
        ("2021-08-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigurationEventMedium(TextualConvention, Integer32):
    status = "current"
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
        *(("checkpoint", 1),
          ("cli", 2),
          ("internal", 3),
          ("rest", 4),
          ("snmp", 5),
          ("ztp", 6))
    )



class ConfigurationCopyProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scp", 1),
          ("sftp", 2),
          ("tftp", 3))
    )



class ConfigurationCopyState(TextualConvention, Integer32):
    status = "current"
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
        *(("waiting", 1),
          ("running", 2),
          ("successful", 3),
          ("failed", 4))
    )



class ConfigurationCopyFailureCause(TextualConvention, Integer32):
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
        *(("authenticationFailed", 1),
          ("badFilename", 2),
          ("busy", 3),
          ("invalidConfiguration", 4),
          ("invalidURL", 5),
          ("systemNotReady", 6),
          ("timeout", 7),
          ("unknown", 8))
    )



class ConfigurationFileType(TextualConvention, Integer32):
    status = "current"
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
        *(("externalFile", 1),
          ("startupConfiguration", 2),
          ("runningConfiguration", 3),
          ("checkpoint", 4))
    )



class ConfigurationFileFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cli", 1),
          ("json", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ArubaWiredConfigurationNotifications_ObjectIdentity = ObjectIdentity
arubaWiredConfigurationNotifications = _ArubaWiredConfigurationNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 0)
)
_ArubaWiredConfigurationObjects_ObjectIdentity = ObjectIdentity
arubaWiredConfigurationObjects = _ArubaWiredConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1)
)
_ArubaWiredConfigurationCopy_ObjectIdentity = ObjectIdentity
arubaWiredConfigurationCopy = _ArubaWiredConfigurationCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0)
)
_ArubaWiredConfigurationCopyTable_Object = MibTable
arubaWiredConfigurationCopyTable = _ArubaWiredConfigurationCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1)
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyTable.setStatus("current")
_ArubaWiredConfigurationCopyEntry_Object = MibTableRow
arubaWiredConfigurationCopyEntry = _ArubaWiredConfigurationCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1)
)
arubaWiredConfigurationCopyEntry.setIndexNames(
    (0, "ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyEntry.setStatus("current")
_ArubaWiredConfigurationCopyIndex_Type = Unsigned32
_ArubaWiredConfigurationCopyIndex_Object = MibTableColumn
arubaWiredConfigurationCopyIndex = _ArubaWiredConfigurationCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 1),
    _ArubaWiredConfigurationCopyIndex_Type()
)
arubaWiredConfigurationCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyIndex.setStatus("current")
_ArubaWiredConfigurationCopySourceFileType_Type = ConfigurationFileType
_ArubaWiredConfigurationCopySourceFileType_Object = MibTableColumn
arubaWiredConfigurationCopySourceFileType = _ArubaWiredConfigurationCopySourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 2),
    _ArubaWiredConfigurationCopySourceFileType_Type()
)
arubaWiredConfigurationCopySourceFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopySourceFileType.setStatus("current")
_ArubaWiredConfigurationCopyDestFileType_Type = ConfigurationFileType
_ArubaWiredConfigurationCopyDestFileType_Object = MibTableColumn
arubaWiredConfigurationCopyDestFileType = _ArubaWiredConfigurationCopyDestFileType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 3),
    _ArubaWiredConfigurationCopyDestFileType_Type()
)
arubaWiredConfigurationCopyDestFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyDestFileType.setStatus("current")
_ArubaWiredConfigurationCopyProtocol_Type = ConfigurationCopyProtocol
_ArubaWiredConfigurationCopyProtocol_Object = MibTableColumn
arubaWiredConfigurationCopyProtocol = _ArubaWiredConfigurationCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 4),
    _ArubaWiredConfigurationCopyProtocol_Type()
)
arubaWiredConfigurationCopyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyProtocol.setStatus("current")
_ArubaWiredConfigurationCheckpointName_Type = DisplayString
_ArubaWiredConfigurationCheckpointName_Object = MibTableColumn
arubaWiredConfigurationCheckpointName = _ArubaWiredConfigurationCheckpointName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 5),
    _ArubaWiredConfigurationCheckpointName_Type()
)
arubaWiredConfigurationCheckpointName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCheckpointName.setStatus("current")
_ArubaWiredConfigurationCopyFileFormat_Type = ConfigurationFileFormat
_ArubaWiredConfigurationCopyFileFormat_Object = MibTableColumn
arubaWiredConfigurationCopyFileFormat = _ArubaWiredConfigurationCopyFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 6),
    _ArubaWiredConfigurationCopyFileFormat_Type()
)
arubaWiredConfigurationCopyFileFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyFileFormat.setStatus("current")
_ArubaWiredConfigurationCopyFileName_Type = DisplayString
_ArubaWiredConfigurationCopyFileName_Object = MibTableColumn
arubaWiredConfigurationCopyFileName = _ArubaWiredConfigurationCopyFileName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 7),
    _ArubaWiredConfigurationCopyFileName_Type()
)
arubaWiredConfigurationCopyFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyFileName.setStatus("current")
_ArubaWiredConfigurationCopyServerAddressType_Type = InetAddressType
_ArubaWiredConfigurationCopyServerAddressType_Object = MibTableColumn
arubaWiredConfigurationCopyServerAddressType = _ArubaWiredConfigurationCopyServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 8),
    _ArubaWiredConfigurationCopyServerAddressType_Type()
)
arubaWiredConfigurationCopyServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyServerAddressType.setStatus("current")
_ArubaWiredConfigurationCopyServerAddress_Type = InetAddress
_ArubaWiredConfigurationCopyServerAddress_Object = MibTableColumn
arubaWiredConfigurationCopyServerAddress = _ArubaWiredConfigurationCopyServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 9),
    _ArubaWiredConfigurationCopyServerAddress_Type()
)
arubaWiredConfigurationCopyServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyServerAddress.setStatus("current")


class _ArubaWiredConfigurationCopyUserName_Type(DisplayString):
    """Custom type arubaWiredConfigurationCopyUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ArubaWiredConfigurationCopyUserName_Type.__name__ = "DisplayString"
_ArubaWiredConfigurationCopyUserName_Object = MibTableColumn
arubaWiredConfigurationCopyUserName = _ArubaWiredConfigurationCopyUserName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 10),
    _ArubaWiredConfigurationCopyUserName_Type()
)
arubaWiredConfigurationCopyUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyUserName.setStatus("current")


class _ArubaWiredConfigurationCopyUserPassword_Type(DisplayString):
    """Custom type arubaWiredConfigurationCopyUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ArubaWiredConfigurationCopyUserPassword_Type.__name__ = "DisplayString"
_ArubaWiredConfigurationCopyUserPassword_Object = MibTableColumn
arubaWiredConfigurationCopyUserPassword = _ArubaWiredConfigurationCopyUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 11),
    _ArubaWiredConfigurationCopyUserPassword_Type()
)
arubaWiredConfigurationCopyUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyUserPassword.setStatus("current")
_ArubaWiredConfigurationCopyVRFName_Type = DisplayString
_ArubaWiredConfigurationCopyVRFName_Object = MibTableColumn
arubaWiredConfigurationCopyVRFName = _ArubaWiredConfigurationCopyVRFName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 12),
    _ArubaWiredConfigurationCopyVRFName_Type()
)
arubaWiredConfigurationCopyVRFName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyVRFName.setStatus("current")


class _ArubaWiredConfigurationCopyNotificationOnCompletion_Type(TruthValue):
    """Custom type arubaWiredConfigurationCopyNotificationOnCompletion based on TruthValue"""
    defaultValue = 2


_ArubaWiredConfigurationCopyNotificationOnCompletion_Type.__name__ = "TruthValue"
_ArubaWiredConfigurationCopyNotificationOnCompletion_Object = MibTableColumn
arubaWiredConfigurationCopyNotificationOnCompletion = _ArubaWiredConfigurationCopyNotificationOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 13),
    _ArubaWiredConfigurationCopyNotificationOnCompletion_Type()
)
arubaWiredConfigurationCopyNotificationOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyNotificationOnCompletion.setStatus("current")
_ArubaWiredConfigurationCopyState_Type = ConfigurationCopyState
_ArubaWiredConfigurationCopyState_Object = MibTableColumn
arubaWiredConfigurationCopyState = _ArubaWiredConfigurationCopyState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 14),
    _ArubaWiredConfigurationCopyState_Type()
)
arubaWiredConfigurationCopyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyState.setStatus("current")
_ArubaWiredConfigurationCopyTimeStarted_Type = TimeStamp
_ArubaWiredConfigurationCopyTimeStarted_Object = MibTableColumn
arubaWiredConfigurationCopyTimeStarted = _ArubaWiredConfigurationCopyTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 15),
    _ArubaWiredConfigurationCopyTimeStarted_Type()
)
arubaWiredConfigurationCopyTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyTimeStarted.setStatus("current")
_ArubaWiredConfigurationCopyTimeCompleted_Type = TimeStamp
_ArubaWiredConfigurationCopyTimeCompleted_Object = MibTableColumn
arubaWiredConfigurationCopyTimeCompleted = _ArubaWiredConfigurationCopyTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 16),
    _ArubaWiredConfigurationCopyTimeCompleted_Type()
)
arubaWiredConfigurationCopyTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyTimeCompleted.setStatus("current")
_ArubaWiredConfigurationCopyFailureCause_Type = ConfigurationCopyFailureCause
_ArubaWiredConfigurationCopyFailureCause_Object = MibTableColumn
arubaWiredConfigurationCopyFailureCause = _ArubaWiredConfigurationCopyFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 17),
    _ArubaWiredConfigurationCopyFailureCause_Type()
)
arubaWiredConfigurationCopyFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyFailureCause.setStatus("current")
_ArubaWiredConfigurationCopyEntryRowStatus_Type = RowStatus
_ArubaWiredConfigurationCopyEntryRowStatus_Object = MibTableColumn
arubaWiredConfigurationCopyEntryRowStatus = _ArubaWiredConfigurationCopyEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 18),
    _ArubaWiredConfigurationCopyEntryRowStatus_Type()
)
arubaWiredConfigurationCopyEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredConfigurationCopyEntryRowStatus.setStatus("current")
_ArubaWiredConfigurationChange_ObjectIdentity = ObjectIdentity
arubaWiredConfigurationChange = _ArubaWiredConfigurationChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 1)
)


class _ArubaWiredConfigurationChangeNotificationEnable_Type(TruthValue):
    """Custom type arubaWiredConfigurationChangeNotificationEnable based on TruthValue"""
    defaultValue = 2


_ArubaWiredConfigurationChangeNotificationEnable_Type.__name__ = "TruthValue"
_ArubaWiredConfigurationChangeNotificationEnable_Object = MibScalar
arubaWiredConfigurationChangeNotificationEnable = _ArubaWiredConfigurationChangeNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 1, 1),
    _ArubaWiredConfigurationChangeNotificationEnable_Type()
)
arubaWiredConfigurationChangeNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredConfigurationChangeNotificationEnable.setStatus("current")
_ArubaWiredConfigurationChangeSource_Type = ConfigurationEventMedium
_ArubaWiredConfigurationChangeSource_Object = MibScalar
arubaWiredConfigurationChangeSource = _ArubaWiredConfigurationChangeSource_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 1, 2),
    _ArubaWiredConfigurationChangeSource_Type()
)
arubaWiredConfigurationChangeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredConfigurationChangeSource.setStatus("current")
_ArubaWiredConfigurationChangeTimestamp_Type = TimeTicks
_ArubaWiredConfigurationChangeTimestamp_Object = MibScalar
arubaWiredConfigurationChangeTimestamp = _ArubaWiredConfigurationChangeTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 1, 3),
    _ArubaWiredConfigurationChangeTimestamp_Type()
)
arubaWiredConfigurationChangeTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredConfigurationChangeTimestamp.setStatus("current")
_ArubaWiredConfigurationConformance_ObjectIdentity = ObjectIdentity
arubaWiredConfigurationConformance = _ArubaWiredConfigurationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2)
)
_ArubaWiredConfigurationCompliances_ObjectIdentity = ObjectIdentity
arubaWiredConfigurationCompliances = _ArubaWiredConfigurationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 1)
)
_ArubaWiredConfigurationGroups_ObjectIdentity = ObjectIdentity
arubaWiredConfigurationGroups = _ArubaWiredConfigurationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 2)
)

# Managed Objects groups

arubaWiredConfigurationScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 2, 1)
)
arubaWiredConfigurationScalarGroup.setObjects(
      *(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeNotificationEnable"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeSource"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeTimestamp"))
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationScalarGroup.setStatus("current")

arubaWiredConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 2, 2)
)
arubaWiredConfigurationGroup.setObjects(
      *(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyProtocol"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopySourceFileType"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyDestFileType"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCheckpointName"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFileFormat"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFileName"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyServerAddressType"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyServerAddress"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyUserName"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyUserPassword"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyVRFName"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyNotificationOnCompletion"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyState"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyTimeStarted"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyTimeCompleted"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFailureCause"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyEntryRowStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationGroup.setStatus("current")


# Notification objects

arubaWiredConfigurationChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 0, 1)
)
arubaWiredConfigurationChangeNotification.setObjects(
      *(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeSource"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeTimestamp"))
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationChangeNotification.setStatus(
        "current"
    )

arubaWiredConfigurationNotificationOnCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 0, 2)
)
arubaWiredConfigurationNotificationOnCompletion.setObjects(
      *(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyServerAddress"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFileName"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyState"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyTimeStarted"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyTimeCompleted"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFailureCause"))
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationNotificationOnCompletion.setStatus(
        "current"
    )


# Notifications groups

arubaWiredConfigurationNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 2, 3)
)
arubaWiredConfigurationNotificationsGroup.setObjects(
      *(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeNotification"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationNotificationOnCompletion"))
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredConfigurationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 1, 1)
)
arubaWiredConfigurationCompliance.setObjects(
      *(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationScalarGroup"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationGroup"),
        ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationNotificationsGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredConfigurationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-CONFIG-MIB",
    **{"ConfigurationEventMedium": ConfigurationEventMedium,
       "ConfigurationCopyProtocol": ConfigurationCopyProtocol,
       "ConfigurationCopyState": ConfigurationCopyState,
       "ConfigurationCopyFailureCause": ConfigurationCopyFailureCause,
       "ConfigurationFileType": ConfigurationFileType,
       "ConfigurationFileFormat": ConfigurationFileFormat,
       "arubaWiredConfigurationMIB": arubaWiredConfigurationMIB,
       "arubaWiredConfigurationNotifications": arubaWiredConfigurationNotifications,
       "arubaWiredConfigurationChangeNotification": arubaWiredConfigurationChangeNotification,
       "arubaWiredConfigurationNotificationOnCompletion": arubaWiredConfigurationNotificationOnCompletion,
       "arubaWiredConfigurationObjects": arubaWiredConfigurationObjects,
       "arubaWiredConfigurationCopy": arubaWiredConfigurationCopy,
       "arubaWiredConfigurationCopyTable": arubaWiredConfigurationCopyTable,
       "arubaWiredConfigurationCopyEntry": arubaWiredConfigurationCopyEntry,
       "arubaWiredConfigurationCopyIndex": arubaWiredConfigurationCopyIndex,
       "arubaWiredConfigurationCopySourceFileType": arubaWiredConfigurationCopySourceFileType,
       "arubaWiredConfigurationCopyDestFileType": arubaWiredConfigurationCopyDestFileType,
       "arubaWiredConfigurationCopyProtocol": arubaWiredConfigurationCopyProtocol,
       "arubaWiredConfigurationCheckpointName": arubaWiredConfigurationCheckpointName,
       "arubaWiredConfigurationCopyFileFormat": arubaWiredConfigurationCopyFileFormat,
       "arubaWiredConfigurationCopyFileName": arubaWiredConfigurationCopyFileName,
       "arubaWiredConfigurationCopyServerAddressType": arubaWiredConfigurationCopyServerAddressType,
       "arubaWiredConfigurationCopyServerAddress": arubaWiredConfigurationCopyServerAddress,
       "arubaWiredConfigurationCopyUserName": arubaWiredConfigurationCopyUserName,
       "arubaWiredConfigurationCopyUserPassword": arubaWiredConfigurationCopyUserPassword,
       "arubaWiredConfigurationCopyVRFName": arubaWiredConfigurationCopyVRFName,
       "arubaWiredConfigurationCopyNotificationOnCompletion": arubaWiredConfigurationCopyNotificationOnCompletion,
       "arubaWiredConfigurationCopyState": arubaWiredConfigurationCopyState,
       "arubaWiredConfigurationCopyTimeStarted": arubaWiredConfigurationCopyTimeStarted,
       "arubaWiredConfigurationCopyTimeCompleted": arubaWiredConfigurationCopyTimeCompleted,
       "arubaWiredConfigurationCopyFailureCause": arubaWiredConfigurationCopyFailureCause,
       "arubaWiredConfigurationCopyEntryRowStatus": arubaWiredConfigurationCopyEntryRowStatus,
       "arubaWiredConfigurationChange": arubaWiredConfigurationChange,
       "arubaWiredConfigurationChangeNotificationEnable": arubaWiredConfigurationChangeNotificationEnable,
       "arubaWiredConfigurationChangeSource": arubaWiredConfigurationChangeSource,
       "arubaWiredConfigurationChangeTimestamp": arubaWiredConfigurationChangeTimestamp,
       "arubaWiredConfigurationConformance": arubaWiredConfigurationConformance,
       "arubaWiredConfigurationCompliances": arubaWiredConfigurationCompliances,
       "arubaWiredConfigurationCompliance": arubaWiredConfigurationCompliance,
       "arubaWiredConfigurationGroups": arubaWiredConfigurationGroups,
       "arubaWiredConfigurationScalarGroup": arubaWiredConfigurationScalarGroup,
       "arubaWiredConfigurationGroup": arubaWiredConfigurationGroup,
       "arubaWiredConfigurationNotificationsGroup": arubaWiredConfigurationNotificationsGroup}
)
