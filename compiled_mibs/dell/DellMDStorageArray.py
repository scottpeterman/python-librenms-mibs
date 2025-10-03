# SNMP MIB module (DellMDStorageArray) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELLMDSTORAGEARRAY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:59 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dellMDStorageArrayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 0)
)
if mibBuilder.loadTexts:
    dellMDStorageArrayMIB.setRevisions(
        ("2009-11-16 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2)
)
_MdStorageManager_ObjectIdentity = ObjectIdentity
mdStorageManager = _MdStorageManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30)
)
_InfoTable_Object = MibTable
infoTable = _InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1)
)
if mibBuilder.loadTexts:
    infoTable.setStatus("current")
_InfoEntry_Object = MibTableRow
infoEntry = _InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1)
)
infoEntry.setIndexNames(
    (0, "DellMDStorageArray", "deviceHostIPType"),
)
if mibBuilder.loadTexts:
    infoEntry.setStatus("current")
_DeviceHostIPType_Type = InetAddressType
_DeviceHostIPType_Object = MibTableColumn
deviceHostIPType = _DeviceHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 1),
    _DeviceHostIPType_Type()
)
deviceHostIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHostIPType.setStatus("current")
_DeviceHostIPAddr_Type = InetAddress
_DeviceHostIPAddr_Object = MibTableColumn
deviceHostIPAddr = _DeviceHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 2),
    _DeviceHostIPAddr_Type()
)
deviceHostIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHostIPAddr.setStatus("current")


class _DeviceHostName_Type(DisplayString):
    """Custom type deviceHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DeviceHostName_Type.__name__ = "DisplayString"
_DeviceHostName_Object = MibTableColumn
deviceHostName = _DeviceHostName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 3),
    _DeviceHostName_Type()
)
deviceHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHostName.setStatus("current")


class _DeviceUserLabel_Type(DisplayString):
    """Custom type deviceUserLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DeviceUserLabel_Type.__name__ = "DisplayString"
_DeviceUserLabel_Object = MibTableColumn
deviceUserLabel = _DeviceUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 4),
    _DeviceUserLabel_Type()
)
deviceUserLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUserLabel.setStatus("current")


class _DeviceErrorCode_Type(DisplayString):
    """Custom type deviceErrorCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_DeviceErrorCode_Type.__name__ = "DisplayString"
_DeviceErrorCode_Object = MibTableColumn
deviceErrorCode = _DeviceErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 5),
    _DeviceErrorCode_Type()
)
deviceErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceErrorCode.setStatus("current")


class _EventTime_Type(DisplayString):
    """Custom type eventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_EventTime_Type.__name__ = "DisplayString"
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 6),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 69),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibTableColumn
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 7),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("current")


class _ComponentType_Type(DisplayString):
    """Custom type componentType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_ComponentType_Type.__name__ = "DisplayString"
_ComponentType_Object = MibTableColumn
componentType = _ComponentType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 8),
    _ComponentType_Type()
)
componentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentType.setStatus("current")


class _ComponentLocation_Type(DisplayString):
    """Custom type componentLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_ComponentLocation_Type.__name__ = "DisplayString"
_ComponentLocation_Object = MibTableColumn
componentLocation = _ComponentLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 1, 1, 9),
    _ComponentLocation_Type()
)
componentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLocation.setStatus("current")

# Managed Objects groups


# Notification objects

storageArrayCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 0, 1)
)
storageArrayCritical.setObjects(
      *(("DellMDStorageArray", "deviceHostIP"),
        ("DellMDStorageArray", "deviceHostName"),
        ("DellMDStorageArray", "deviceUserLabel"),
        ("DellMDStorageArray", "deviceErrorCode"),
        ("DellMDStorageArray", "eventTime"),
        ("DellMDStorageArray", "trapDescription"),
        ("DellMDStorageArray", "componentType"),
        ("DellMDStorageArray", "componentLocation"))
)
if mibBuilder.loadTexts:
    storageArrayCritical.setStatus(
        ""
    )

storageArrayWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 0, 2)
)
storageArrayWarning.setObjects(
      *(("DellMDStorageArray", "deviceHostIP"),
        ("DellMDStorageArray", "deviceHostName"),
        ("DellMDStorageArray", "deviceUserLabel"),
        ("DellMDStorageArray", "deviceErrorCode"),
        ("DellMDStorageArray", "eventTime"),
        ("DellMDStorageArray", "trapDescription"),
        ("DellMDStorageArray", "componentType"),
        ("DellMDStorageArray", "componentLocation"))
)
if mibBuilder.loadTexts:
    storageArrayWarning.setStatus(
        ""
    )

storageArrayInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 0, 3)
)
storageArrayInformational.setObjects(
      *(("DellMDStorageArray", "deviceHostIP"),
        ("DellMDStorageArray", "deviceHostName"),
        ("DellMDStorageArray", "deviceUserLabel"),
        ("DellMDStorageArray", "deviceErrorCode"),
        ("DellMDStorageArray", "eventTime"),
        ("DellMDStorageArray", "trapDescription"),
        ("DellMDStorageArray", "componentType"),
        ("DellMDStorageArray", "componentLocation"))
)
if mibBuilder.loadTexts:
    storageArrayInformational.setStatus(
        ""
    )

storageArrayDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 30, 0, 4)
)
storageArrayDebug.setObjects(
      *(("DellMDStorageArray", "deviceHostIP"),
        ("DellMDStorageArray", "deviceHostName"),
        ("DellMDStorageArray", "deviceUserLabel"),
        ("DellMDStorageArray", "deviceErrorCode"),
        ("DellMDStorageArray", "eventTime"),
        ("DellMDStorageArray", "trapDescription"),
        ("DellMDStorageArray", "componentType"),
        ("DellMDStorageArray", "componentLocation"))
)
if mibBuilder.loadTexts:
    storageArrayDebug.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DellMDStorageArray",
    **{"dell": dell,
       "storage": storage,
       "hardware": hardware,
       "mdStorageManager": mdStorageManager,
       "dellMDStorageArrayMIB": dellMDStorageArrayMIB,
       "storageArrayCritical": storageArrayCritical,
       "storageArrayWarning": storageArrayWarning,
       "storageArrayInformational": storageArrayInformational,
       "storageArrayDebug": storageArrayDebug,
       "infoTable": infoTable,
       "infoEntry": infoEntry,
       "deviceHostIPType": deviceHostIPType,
       "deviceHostIPAddr": deviceHostIPAddr,
       "deviceHostName": deviceHostName,
       "deviceUserLabel": deviceUserLabel,
       "deviceErrorCode": deviceErrorCode,
       "eventTime": eventTime,
       "trapDescription": trapDescription,
       "componentType": componentType,
       "componentLocation": componentLocation}
)
