# SNMP MIB module (BLUECOAT-SG-WCCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecoat\BLUECOAT-SG-WCCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:43 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

deviceWccpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5)
)
if mibBuilder.loadTexts:
    deviceWccpMIB.setRevisions(
        ("2008-01-23 03:00",
         "2007-11-05 03:00",
         "2002-08-28 03:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class WccpServiceType(TextualConvention, Integer32):
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
        *(("standard", 1),
          ("dynamic", 2),
          ("unknown", 3))
    )



class WccpVersion(TextualConvention, Integer32):
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
        *(("version1", 1),
          ("version2", 2),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceWccpEnabled_Type = TruthValue
_DeviceWccpEnabled_Object = MibScalar
deviceWccpEnabled = _DeviceWccpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 1),
    _DeviceWccpEnabled_Type()
)
deviceWccpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpEnabled.setStatus("current")
_DeviceWccpMIBObjects_ObjectIdentity = ObjectIdentity
deviceWccpMIBObjects = _DeviceWccpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2)
)
_DeviceWccpValues_ObjectIdentity = ObjectIdentity
deviceWccpValues = _DeviceWccpValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1)
)
_DeviceWccpValueTable_Object = MibTable
deviceWccpValueTable = _DeviceWccpValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    deviceWccpValueTable.setStatus("current")
_DeviceWccpValueEntry_Object = MibTableRow
deviceWccpValueEntry = _DeviceWccpValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1)
)
deviceWccpValueEntry.setIndexNames(
    (0, "BLUECOAT-SG-WCCP-MIB", "deviceWccpIndex"),
)
if mibBuilder.loadTexts:
    deviceWccpValueEntry.setStatus("current")


class _DeviceWccpIndex_Type(Integer32):
    """Custom type deviceWccpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceWccpIndex_Type.__name__ = "Integer32"
_DeviceWccpIndex_Object = MibTableColumn
deviceWccpIndex = _DeviceWccpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 1),
    _DeviceWccpIndex_Type()
)
deviceWccpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceWccpIndex.setStatus("current")
_DeviceWccpServiceID_Type = Integer32
_DeviceWccpServiceID_Object = MibTableColumn
deviceWccpServiceID = _DeviceWccpServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 2),
    _DeviceWccpServiceID_Type()
)
deviceWccpServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpServiceID.setStatus("current")
_DeviceWccpServiceType_Type = WccpServiceType
_DeviceWccpServiceType_Object = MibTableColumn
deviceWccpServiceType = _DeviceWccpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 3),
    _DeviceWccpServiceType_Type()
)
deviceWccpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpServiceType.setStatus("current")
_DeviceWccpServiceVersion_Type = WccpVersion
_DeviceWccpServiceVersion_Object = MibTableColumn
deviceWccpServiceVersion = _DeviceWccpServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 4),
    _DeviceWccpServiceVersion_Type()
)
deviceWccpServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpServiceVersion.setStatus("current")
_DeviceWccpPacketsRedir_Type = Counter64
_DeviceWccpPacketsRedir_Object = MibTableColumn
deviceWccpPacketsRedir = _DeviceWccpPacketsRedir_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 5),
    _DeviceWccpPacketsRedir_Type()
)
deviceWccpPacketsRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpPacketsRedir.setStatus("current")
_DeviceWccpPacketsLowRedir_Type = Counter32
_DeviceWccpPacketsLowRedir_Object = MibTableColumn
deviceWccpPacketsLowRedir = _DeviceWccpPacketsLowRedir_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 6),
    _DeviceWccpPacketsLowRedir_Type()
)
deviceWccpPacketsLowRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpPacketsLowRedir.setStatus("current")
_DeviceWccpBytesRedir_Type = Counter64
_DeviceWccpBytesRedir_Object = MibTableColumn
deviceWccpBytesRedir = _DeviceWccpBytesRedir_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 7),
    _DeviceWccpBytesRedir_Type()
)
deviceWccpBytesRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpBytesRedir.setStatus("current")
if mibBuilder.loadTexts:
    deviceWccpBytesRedir.setUnits("Bytes")
_DeviceWccpBytesLowRedir_Type = Counter32
_DeviceWccpBytesLowRedir_Object = MibTableColumn
deviceWccpBytesLowRedir = _DeviceWccpBytesLowRedir_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 8),
    _DeviceWccpBytesLowRedir_Type()
)
deviceWccpBytesLowRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceWccpBytesLowRedir.setStatus("current")
if mibBuilder.loadTexts:
    deviceWccpBytesLowRedir.setUnits("Bytes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-WCCP-MIB",
    **{"WccpServiceType": WccpServiceType,
       "WccpVersion": WccpVersion,
       "deviceWccpMIB": deviceWccpMIB,
       "deviceWccpEnabled": deviceWccpEnabled,
       "deviceWccpMIBObjects": deviceWccpMIBObjects,
       "deviceWccpValues": deviceWccpValues,
       "deviceWccpValueTable": deviceWccpValueTable,
       "deviceWccpValueEntry": deviceWccpValueEntry,
       "deviceWccpIndex": deviceWccpIndex,
       "deviceWccpServiceID": deviceWccpServiceID,
       "deviceWccpServiceType": deviceWccpServiceType,
       "deviceWccpServiceVersion": deviceWccpServiceVersion,
       "deviceWccpPacketsRedir": deviceWccpPacketsRedir,
       "deviceWccpPacketsLowRedir": deviceWccpPacketsLowRedir,
       "deviceWccpBytesRedir": deviceWccpBytesRedir,
       "deviceWccpBytesLowRedir": deviceWccpBytesLowRedir}
)
