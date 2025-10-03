# SNMP MIB module (BLUECOAT-SG-DISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecoat\BLUECOAT-SG-DISK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:38 2025
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

deviceDiskMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2)
)
if mibBuilder.loadTexts:
    deviceDiskMIB.setRevisions(
        ("2013-07-11 03:00",
         "2007-11-05 03:00",
         "2002-11-06 03:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DiskStatus(TextualConvention, Integer32):
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("initializing", 2),
          ("inserted", 3),
          ("offline", 4),
          ("removed", 5),
          ("notpresent", 6),
          ("empty", 7),
          ("ioerror", 8),
          ("unusable", 9),
          ("unknown", 10))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceDiskMIBObjects_ObjectIdentity = ObjectIdentity
deviceDiskMIBObjects = _DeviceDiskMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1)
)
_DeviceDiskValues_ObjectIdentity = ObjectIdentity
deviceDiskValues = _DeviceDiskValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1)
)
_DeviceDiskValueTable_Object = MibTable
deviceDiskValueTable = _DeviceDiskValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceDiskValueTable.setStatus("current")
_DeviceDiskValueEntry_Object = MibTableRow
deviceDiskValueEntry = _DeviceDiskValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1)
)
deviceDiskValueEntry.setIndexNames(
    (0, "BLUECOAT-SG-DISK-MIB", "deviceDiskIndex"),
)
if mibBuilder.loadTexts:
    deviceDiskValueEntry.setStatus("current")


class _DeviceDiskIndex_Type(Integer32):
    """Custom type deviceDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceDiskIndex_Type.__name__ = "Integer32"
_DeviceDiskIndex_Object = MibTableColumn
deviceDiskIndex = _DeviceDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 1),
    _DeviceDiskIndex_Type()
)
deviceDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceDiskIndex.setStatus("current")
_DeviceDiskTrapEnabled_Type = TruthValue
_DeviceDiskTrapEnabled_Object = MibTableColumn
deviceDiskTrapEnabled = _DeviceDiskTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 2),
    _DeviceDiskTrapEnabled_Type()
)
deviceDiskTrapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskTrapEnabled.setStatus("current")
_DeviceDiskStatus_Type = DiskStatus
_DeviceDiskStatus_Object = MibTableColumn
deviceDiskStatus = _DeviceDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 3),
    _DeviceDiskStatus_Type()
)
deviceDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskStatus.setStatus("current")
_DeviceDiskTimeStamp_Type = TimeStamp
_DeviceDiskTimeStamp_Object = MibTableColumn
deviceDiskTimeStamp = _DeviceDiskTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 4),
    _DeviceDiskTimeStamp_Type()
)
deviceDiskTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    deviceDiskTimeStamp.setUnits("Hundredths of seconds")
_DeviceDiskVendor_Type = DisplayString
_DeviceDiskVendor_Object = MibTableColumn
deviceDiskVendor = _DeviceDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 5),
    _DeviceDiskVendor_Type()
)
deviceDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskVendor.setStatus("current")
_DeviceDiskProduct_Type = DisplayString
_DeviceDiskProduct_Object = MibTableColumn
deviceDiskProduct = _DeviceDiskProduct_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 6),
    _DeviceDiskProduct_Type()
)
deviceDiskProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskProduct.setStatus("current")
_DeviceDiskRevision_Type = DisplayString
_DeviceDiskRevision_Object = MibTableColumn
deviceDiskRevision = _DeviceDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 7),
    _DeviceDiskRevision_Type()
)
deviceDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskRevision.setStatus("current")
_DeviceDiskSerialN_Type = DisplayString
_DeviceDiskSerialN_Object = MibTableColumn
deviceDiskSerialN = _DeviceDiskSerialN_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 8),
    _DeviceDiskSerialN_Type()
)
deviceDiskSerialN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskSerialN.setStatus("current")
_DeviceDiskBlockSize_Type = Counter32
_DeviceDiskBlockSize_Object = MibTableColumn
deviceDiskBlockSize = _DeviceDiskBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 9),
    _DeviceDiskBlockSize_Type()
)
deviceDiskBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    deviceDiskBlockSize.setUnits("Bytes")
_DeviceDiskBlockCount_Type = Counter32
_DeviceDiskBlockCount_Object = MibTableColumn
deviceDiskBlockCount = _DeviceDiskBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 10),
    _DeviceDiskBlockCount_Type()
)
deviceDiskBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskBlockCount.setStatus("current")
_DeviceDiskMIBNotifications_ObjectIdentity = ObjectIdentity
deviceDiskMIBNotifications = _DeviceDiskMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 2)
)
_DeviceDiskMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
deviceDiskMIBNotificationsPrefix = _DeviceDiskMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

deviceDiskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 2, 2, 0, 1)
)
deviceDiskTrap.setObjects(
    ("BLUECOAT-SG-DISK-MIB", "deviceDiskStatus")
)
if mibBuilder.loadTexts:
    deviceDiskTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-DISK-MIB",
    **{"DiskStatus": DiskStatus,
       "deviceDiskMIB": deviceDiskMIB,
       "deviceDiskMIBObjects": deviceDiskMIBObjects,
       "deviceDiskValues": deviceDiskValues,
       "deviceDiskValueTable": deviceDiskValueTable,
       "deviceDiskValueEntry": deviceDiskValueEntry,
       "deviceDiskIndex": deviceDiskIndex,
       "deviceDiskTrapEnabled": deviceDiskTrapEnabled,
       "deviceDiskStatus": deviceDiskStatus,
       "deviceDiskTimeStamp": deviceDiskTimeStamp,
       "deviceDiskVendor": deviceDiskVendor,
       "deviceDiskProduct": deviceDiskProduct,
       "deviceDiskRevision": deviceDiskRevision,
       "deviceDiskSerialN": deviceDiskSerialN,
       "deviceDiskBlockSize": deviceDiskBlockSize,
       "deviceDiskBlockCount": deviceDiskBlockCount,
       "deviceDiskMIBNotifications": deviceDiskMIBNotifications,
       "deviceDiskMIBNotificationsPrefix": deviceDiskMIBNotificationsPrefix,
       "deviceDiskTrap": deviceDiskTrap}
)
