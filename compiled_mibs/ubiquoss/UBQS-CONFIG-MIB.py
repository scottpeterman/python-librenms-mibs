# SNMP MIB module (UBQS-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:13 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

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

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigMethodType(TextualConvention, Integer32):
    status = "current"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("noMethod", 0),
          ("startupConfig", 1),
          ("runningConfig", 2),
          ("ftp", 3),
          ("tftp", 4),
          ("flash", 5),
          ("usbFlash", 6),
          ("configFile", 7))
    )



# MIB Managed Objects in the order of their OIDs

_UbiConfigMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiConfigMIBNotificationPrefix = _UbiConfigMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 0)
)
_UbiConfigMIBObjects_ObjectIdentity = ObjectIdentity
ubiConfigMIBObjects = _UbiConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1)
)
_UbiConfigInfoTable_Object = MibTable
ubiConfigInfoTable = _UbiConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 1)
)
if mibBuilder.loadTexts:
    ubiConfigInfoTable.setStatus("current")
_UbiConfigInfoEntry_Object = MibTableRow
ubiConfigInfoEntry = _UbiConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 1, 1)
)
ubiConfigInfoEntry.setIndexNames(
    (0, "UBQS-CONFIG-MIB", "ubiConfigName"),
)
if mibBuilder.loadTexts:
    ubiConfigInfoEntry.setStatus("current")
_UbiConfigName_Type = DisplayString
_UbiConfigName_Object = MibTableColumn
ubiConfigName = _UbiConfigName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 1, 1, 1),
    _UbiConfigName_Type()
)
ubiConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiConfigName.setStatus("current")


class _UbiConfigType_Type(Integer32):
    """Custom type ubiConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("config", 1),
          ("image", 2))
    )


_UbiConfigType_Type.__name__ = "Integer32"
_UbiConfigType_Object = MibTableColumn
ubiConfigType = _UbiConfigType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 1, 1, 2),
    _UbiConfigType_Type()
)
ubiConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiConfigType.setStatus("current")


class _UbiConfigCurrentStatus_Type(Integer32):
    """Custom type ubiConfigCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noCurrent", 0),
          ("currentConfig", 1))
    )


_UbiConfigCurrentStatus_Type.__name__ = "Integer32"
_UbiConfigCurrentStatus_Object = MibTableColumn
ubiConfigCurrentStatus = _UbiConfigCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 1, 1, 3),
    _UbiConfigCurrentStatus_Type()
)
ubiConfigCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiConfigCurrentStatus.setStatus("current")


class _UbiConfigNextStatus_Type(Integer32):
    """Custom type ubiConfigNextStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noNext", 0),
          ("nextConfig", 1))
    )


_UbiConfigNextStatus_Type.__name__ = "Integer32"
_UbiConfigNextStatus_Object = MibTableColumn
ubiConfigNextStatus = _UbiConfigNextStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 1, 1, 4),
    _UbiConfigNextStatus_Type()
)
ubiConfigNextStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigNextStatus.setStatus("current")
_UbiConfigErase_ObjectIdentity = ObjectIdentity
ubiConfigErase = _UbiConfigErase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 2)
)


class _UbiConfigEraseMode_Type(Integer32):
    """Custom type ubiConfigEraseMode based on Integer32"""
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
        *(("noMode", 0),
          ("startupConfig", 1),
          ("fileInFlash", 2),
          ("fileInUsbFlash", 3))
    )


_UbiConfigEraseMode_Type.__name__ = "Integer32"
_UbiConfigEraseMode_Object = MibScalar
ubiConfigEraseMode = _UbiConfigEraseMode_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 2, 1),
    _UbiConfigEraseMode_Type()
)
ubiConfigEraseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigEraseMode.setStatus("current")
_UbiConfigEraseFileName_Type = DisplayString
_UbiConfigEraseFileName_Object = MibScalar
ubiConfigEraseFileName = _UbiConfigEraseFileName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 2, 2),
    _UbiConfigEraseFileName_Type()
)
ubiConfigEraseFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigEraseFileName.setStatus("current")


class _UbiConfigEraseOperate_Type(Integer32):
    """Custom type ubiConfigEraseOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("excute", 1))
    )


_UbiConfigEraseOperate_Type.__name__ = "Integer32"
_UbiConfigEraseOperate_Object = MibScalar
ubiConfigEraseOperate = _UbiConfigEraseOperate_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 2, 3),
    _UbiConfigEraseOperate_Type()
)
ubiConfigEraseOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigEraseOperate.setStatus("current")


class _UbiConfigEraseUsbPartNum_Type(Integer32):
    """Custom type ubiConfigEraseUsbPartNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_UbiConfigEraseUsbPartNum_Type.__name__ = "Integer32"
_UbiConfigEraseUsbPartNum_Object = MibScalar
ubiConfigEraseUsbPartNum = _UbiConfigEraseUsbPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 2, 4),
    _UbiConfigEraseUsbPartNum_Type()
)
ubiConfigEraseUsbPartNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigEraseUsbPartNum.setStatus("current")
_UbiConfigCopy_ObjectIdentity = ObjectIdentity
ubiConfigCopy = _UbiConfigCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3)
)
_UbiConfigSourceMethod_Type = ConfigMethodType
_UbiConfigSourceMethod_Object = MibScalar
ubiConfigSourceMethod = _UbiConfigSourceMethod_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 1),
    _UbiConfigSourceMethod_Type()
)
ubiConfigSourceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigSourceMethod.setStatus("current")
_UbiConfigSourceFileName_Type = DisplayString
_UbiConfigSourceFileName_Object = MibScalar
ubiConfigSourceFileName = _UbiConfigSourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 2),
    _UbiConfigSourceFileName_Type()
)
ubiConfigSourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigSourceFileName.setStatus("current")
_UbiConfigSourceIpAddress_Type = DisplayString
_UbiConfigSourceIpAddress_Object = MibScalar
ubiConfigSourceIpAddress = _UbiConfigSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 3),
    _UbiConfigSourceIpAddress_Type()
)
ubiConfigSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigSourceIpAddress.setStatus("current")
_UbiConfigSouceUserId_Type = DisplayString
_UbiConfigSouceUserId_Object = MibScalar
ubiConfigSouceUserId = _UbiConfigSouceUserId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 4),
    _UbiConfigSouceUserId_Type()
)
ubiConfigSouceUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigSouceUserId.setStatus("current")
_UbiConfigSourceUserPassword_Type = DisplayString
_UbiConfigSourceUserPassword_Object = MibScalar
ubiConfigSourceUserPassword = _UbiConfigSourceUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 5),
    _UbiConfigSourceUserPassword_Type()
)
ubiConfigSourceUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigSourceUserPassword.setStatus("current")
_UbiConfigSourcePartNum_Type = DisplayString
_UbiConfigSourcePartNum_Object = MibScalar
ubiConfigSourcePartNum = _UbiConfigSourcePartNum_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 6),
    _UbiConfigSourcePartNum_Type()
)
ubiConfigSourcePartNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigSourcePartNum.setStatus("current")
_UbiConfigDestinationMethod_Type = ConfigMethodType
_UbiConfigDestinationMethod_Object = MibScalar
ubiConfigDestinationMethod = _UbiConfigDestinationMethod_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 7),
    _UbiConfigDestinationMethod_Type()
)
ubiConfigDestinationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigDestinationMethod.setStatus("current")
_UbiConfigDestinationFileName_Type = DisplayString
_UbiConfigDestinationFileName_Object = MibScalar
ubiConfigDestinationFileName = _UbiConfigDestinationFileName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 8),
    _UbiConfigDestinationFileName_Type()
)
ubiConfigDestinationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigDestinationFileName.setStatus("current")
_UbiConfigDestinationIpAddress_Type = DisplayString
_UbiConfigDestinationIpAddress_Object = MibScalar
ubiConfigDestinationIpAddress = _UbiConfigDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 9),
    _UbiConfigDestinationIpAddress_Type()
)
ubiConfigDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigDestinationIpAddress.setStatus("current")
_UbiConfigDestinationUserId_Type = DisplayString
_UbiConfigDestinationUserId_Object = MibScalar
ubiConfigDestinationUserId = _UbiConfigDestinationUserId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 10),
    _UbiConfigDestinationUserId_Type()
)
ubiConfigDestinationUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigDestinationUserId.setStatus("current")
_UbiConfigDestinationUserPassword_Type = DisplayString
_UbiConfigDestinationUserPassword_Object = MibScalar
ubiConfigDestinationUserPassword = _UbiConfigDestinationUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 11),
    _UbiConfigDestinationUserPassword_Type()
)
ubiConfigDestinationUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigDestinationUserPassword.setStatus("current")
_UbiConfigDestinationPartNum_Type = DisplayString
_UbiConfigDestinationPartNum_Object = MibScalar
ubiConfigDestinationPartNum = _UbiConfigDestinationPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 12),
    _UbiConfigDestinationPartNum_Type()
)
ubiConfigDestinationPartNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigDestinationPartNum.setStatus("current")


class _UbiConfigCopyOperate_Type(Integer32):
    """Custom type ubiConfigCopyOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("excute", 1))
    )


_UbiConfigCopyOperate_Type.__name__ = "Integer32"
_UbiConfigCopyOperate_Object = MibScalar
ubiConfigCopyOperate = _UbiConfigCopyOperate_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 3, 13),
    _UbiConfigCopyOperate_Type()
)
ubiConfigCopyOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiConfigCopyOperate.setStatus("current")
_UbiUsbConfigInfoTable_Object = MibTable
ubiUsbConfigInfoTable = _UbiUsbConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 4)
)
if mibBuilder.loadTexts:
    ubiUsbConfigInfoTable.setStatus("current")
_UbiUsbConfigInfoEntry_Object = MibTableRow
ubiUsbConfigInfoEntry = _UbiUsbConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 4, 1)
)
ubiUsbConfigInfoEntry.setIndexNames(
    (0, "UBQS-CONFIG-MIB", "ubiUsbPartNum"),
    (0, "UBQS-CONFIG-MIB", "ubiUsbConfigName"),
)
if mibBuilder.loadTexts:
    ubiUsbConfigInfoEntry.setStatus("current")


class _UbiUsbPartNum_Type(Integer32):
    """Custom type ubiUsbPartNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_UbiUsbPartNum_Type.__name__ = "Integer32"
_UbiUsbPartNum_Object = MibTableColumn
ubiUsbPartNum = _UbiUsbPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 4, 1, 1),
    _UbiUsbPartNum_Type()
)
ubiUsbPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiUsbPartNum.setStatus("current")
_UbiUsbConfigName_Type = DisplayString
_UbiUsbConfigName_Object = MibTableColumn
ubiUsbConfigName = _UbiUsbConfigName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 4, 1, 2),
    _UbiUsbConfigName_Type()
)
ubiUsbConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiUsbConfigName.setStatus("current")


class _UbiUsbConfigType_Type(Integer32):
    """Custom type ubiUsbConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("config", 1),
          ("image", 2))
    )


_UbiUsbConfigType_Type.__name__ = "Integer32"
_UbiUsbConfigType_Object = MibTableColumn
ubiUsbConfigType = _UbiUsbConfigType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 4, 1, 3),
    _UbiUsbConfigType_Type()
)
ubiUsbConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiUsbConfigType.setStatus("current")


class _UbiUsbConfigCurrentStatus_Type(Integer32):
    """Custom type ubiUsbConfigCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noCurrent", 0),
          ("currentConfig", 1))
    )


_UbiUsbConfigCurrentStatus_Type.__name__ = "Integer32"
_UbiUsbConfigCurrentStatus_Object = MibTableColumn
ubiUsbConfigCurrentStatus = _UbiUsbConfigCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 4, 1, 4),
    _UbiUsbConfigCurrentStatus_Type()
)
ubiUsbConfigCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiUsbConfigCurrentStatus.setStatus("current")


class _UbiUsbConfigNextStatus_Type(Integer32):
    """Custom type ubiUsbConfigNextStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noNext", 0),
          ("nextConfig", 1))
    )


_UbiUsbConfigNextStatus_Type.__name__ = "Integer32"
_UbiUsbConfigNextStatus_Object = MibTableColumn
ubiUsbConfigNextStatus = _UbiUsbConfigNextStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 1, 4, 1, 5),
    _UbiUsbConfigNextStatus_Type()
)
ubiUsbConfigNextStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiUsbConfigNextStatus.setStatus("current")
_UbiConfigMIBConformance_ObjectIdentity = ObjectIdentity
ubiConfigMIBConformance = _UbiConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 2)
)
_UbiConfigMIBCompliances_ObjectIdentity = ObjectIdentity
ubiConfigMIBCompliances = _UbiConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 2, 1)
)
_UbiConfigMonMIBGroups_ObjectIdentity = ObjectIdentity
ubiConfigMonMIBGroups = _UbiConfigMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 2, 2)
)

# Managed Objects groups

ubiConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 2, 2, 1)
)
ubiConfigMIBGroup.setObjects(
      *(("UBQS-CONFIG-MIB", "ubiConfigName"),
        ("UBQS-CONFIG-MIB", "ubiConfigType"),
        ("UBQS-CONFIG-MIB", "ubiConfigCurrentStatus"),
        ("UBQS-CONFIG-MIB", "ubiConfigNextStatus"),
        ("UBQS-CONFIG-MIB", "ubiConfigEraseMode"),
        ("UBQS-CONFIG-MIB", "ubiConfigEraseFileName"),
        ("UBQS-CONFIG-MIB", "ubiConfigEraseOperate"),
        ("UBQS-CONFIG-MIB", "ubiConfigSourceMethod"),
        ("UBQS-CONFIG-MIB", "ubiConfigSourceFileName"),
        ("UBQS-CONFIG-MIB", "ubiConfigSourceIpAddress"),
        ("UBQS-CONFIG-MIB", "ubiConfigSourceUserId"),
        ("UBQS-CONFIG-MIB", "ubiConfigSourceUserPassword"),
        ("UBQS-CONFIG-MIB", "ubiConfigSourcePartNum"),
        ("UBQS-CONFIG-MIB", "ubiConfigDestinationMethod"),
        ("UBQS-CONFIG-MIB", "ubiConfigDestinationFileName"),
        ("UBQS-CONFIG-MIB", "ubiConfigDestinationIpAddress"),
        ("UBQS-CONFIG-MIB", "ubiConfigDestinationUserId"),
        ("UBQS-CONFIG-MIB", "ubiConfigDestinationUserPassword"),
        ("UBQS-CONFIG-MIB", "ubiConfigDestinationPartNum"),
        ("UBQS-CONFIG-MIB", "ubiConfigCopyOperate"))
)
if mibBuilder.loadTexts:
    ubiConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups

ubiConfigMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 2, 2, 2)
)
ubiConfigMIBNotifGroup.setObjects(
    ("UBQS-CONFIG-MIB", "ubiConfigRemoveNotification")
)
if mibBuilder.loadTexts:
    ubiConfigMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ubiConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 18, 2, 1, 1)
)
ubiConfigMIBCompliance.setObjects(
      *(("UBQS-CONFIG-MIB", "ubiConfigMIBGroup"),
        ("UBQS-CONFIG-MIB", "ubiConfigMIBNotifGroup"),
        ("UBQS-CONFIG-MIB", "ubiConfigMIBGroup"),
        ("UBQS-CONFIG-MIB", "ubiConfigMIBNotifGroup"))
)
if mibBuilder.loadTexts:
    ubiConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-CONFIG-MIB",
    **{"ConfigMethodType": ConfigMethodType,
       "ubiConfigMIB": ubiConfigMIB,
       "ubiConfigMIBNotificationPrefix": ubiConfigMIBNotificationPrefix,
       "ubiConfigMIBObjects": ubiConfigMIBObjects,
       "ubiConfigInfoTable": ubiConfigInfoTable,
       "ubiConfigInfoEntry": ubiConfigInfoEntry,
       "ubiConfigName": ubiConfigName,
       "ubiConfigType": ubiConfigType,
       "ubiConfigCurrentStatus": ubiConfigCurrentStatus,
       "ubiConfigNextStatus": ubiConfigNextStatus,
       "ubiConfigErase": ubiConfigErase,
       "ubiConfigEraseMode": ubiConfigEraseMode,
       "ubiConfigEraseFileName": ubiConfigEraseFileName,
       "ubiConfigEraseOperate": ubiConfigEraseOperate,
       "ubiConfigEraseUsbPartNum": ubiConfigEraseUsbPartNum,
       "ubiConfigCopy": ubiConfigCopy,
       "ubiConfigSourceMethod": ubiConfigSourceMethod,
       "ubiConfigSourceFileName": ubiConfigSourceFileName,
       "ubiConfigSourceIpAddress": ubiConfigSourceIpAddress,
       "ubiConfigSouceUserId": ubiConfigSouceUserId,
       "ubiConfigSourceUserPassword": ubiConfigSourceUserPassword,
       "ubiConfigSourcePartNum": ubiConfigSourcePartNum,
       "ubiConfigDestinationMethod": ubiConfigDestinationMethod,
       "ubiConfigDestinationFileName": ubiConfigDestinationFileName,
       "ubiConfigDestinationIpAddress": ubiConfigDestinationIpAddress,
       "ubiConfigDestinationUserId": ubiConfigDestinationUserId,
       "ubiConfigDestinationUserPassword": ubiConfigDestinationUserPassword,
       "ubiConfigDestinationPartNum": ubiConfigDestinationPartNum,
       "ubiConfigCopyOperate": ubiConfigCopyOperate,
       "ubiUsbConfigInfoTable": ubiUsbConfigInfoTable,
       "ubiUsbConfigInfoEntry": ubiUsbConfigInfoEntry,
       "ubiUsbPartNum": ubiUsbPartNum,
       "ubiUsbConfigName": ubiUsbConfigName,
       "ubiUsbConfigType": ubiUsbConfigType,
       "ubiUsbConfigCurrentStatus": ubiUsbConfigCurrentStatus,
       "ubiUsbConfigNextStatus": ubiUsbConfigNextStatus,
       "ubiConfigMIBConformance": ubiConfigMIBConformance,
       "ubiConfigMIBCompliances": ubiConfigMIBCompliances,
       "ubiConfigMIBCompliance": ubiConfigMIBCompliance,
       "ubiConfigMonMIBGroups": ubiConfigMonMIBGroups,
       "ubiConfigMIBGroup": ubiConfigMIBGroup,
       "ubiConfigMIBNotifGroup": ubiConfigMIBNotifGroup}
)
