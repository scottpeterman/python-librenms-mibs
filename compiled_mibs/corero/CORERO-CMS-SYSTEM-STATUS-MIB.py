# SNMP MIB module (CORERO-CMS-SYSTEM-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\corero\CORERO-CMS-SYSTEM-STATUS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:34 2025
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

(coreroCMSMIBObjects,) = mibBuilder.importSymbols(
    "CORERO-CMS-MIB",
    "coreroCMSMIBObjects")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

systemStatus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6)
)
if mibBuilder.loadTexts:
    systemStatus.setRevisions(
        ("2020-01-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Protection_Type(Integer32):
    """Custom type protection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1),
          ("error", 2))
    )


_Protection_Type.__name__ = "Integer32"
_Protection_Object = MibScalar
protection = _Protection_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 1),
    _Protection_Type()
)
protection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protection.setStatus("current")


class _Device_Type(Integer32):
    """Custom type device based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1),
          ("error", 2))
    )


_Device_Type.__name__ = "Integer32"
_Device_Object = MibScalar
device = _Device_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 2),
    _Device_Type()
)
device.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device.setStatus("current")


class _Network_Type(Integer32):
    """Custom type network based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1),
          ("error", 2))
    )


_Network_Type.__name__ = "Integer32"
_Network_Object = MibScalar
network = _Network_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 3),
    _Network_Type()
)
network.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    network.setStatus("current")
_IssueTable_Object = MibTable
issueTable = _IssueTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 4)
)
if mibBuilder.loadTexts:
    issueTable.setStatus("current")
_IssueEntry_Object = MibTableRow
issueEntry = _IssueEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 4, 1)
)
issueEntry.setIndexNames(
    (0, "CORERO-CMS-SYSTEM-STATUS-MIB", "issueIndex"),
)
if mibBuilder.loadTexts:
    issueEntry.setStatus("current")


class _IssueIndex_Type(Integer32):
    """Custom type issueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IssueIndex_Type.__name__ = "Integer32"
_IssueIndex_Object = MibTableColumn
issueIndex = _IssueIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 4, 1, 1),
    _IssueIndex_Type()
)
issueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issueIndex.setStatus("current")


class _IssueType_Type(Integer32):
    """Custom type issueType based on Integer32"""
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
        *(("protection", 0),
          ("devices", 1),
          ("network", 2),
          ("analytics", 3))
    )


_IssueType_Type.__name__ = "Integer32"
_IssueType_Object = MibTableColumn
issueType = _IssueType_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 4, 1, 2),
    _IssueType_Type()
)
issueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issueType.setStatus("current")
_IssueDevice_Type = OctetString
_IssueDevice_Object = MibTableColumn
issueDevice = _IssueDevice_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 4, 1, 3),
    _IssueDevice_Type()
)
issueDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issueDevice.setStatus("current")
_IssueSegment_Type = OctetString
_IssueSegment_Object = MibTableColumn
issueSegment = _IssueSegment_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 4, 1, 4),
    _IssueSegment_Type()
)
issueSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issueSegment.setStatus("current")
_IssueDescription_Type = OctetString
_IssueDescription_Object = MibTableColumn
issueDescription = _IssueDescription_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 4, 1, 5),
    _IssueDescription_Type()
)
issueDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issueDescription.setStatus("current")


class _IssueSeverity_Type(Integer32):
    """Custom type issueSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1),
          ("error", 2))
    )


_IssueSeverity_Type.__name__ = "Integer32"
_IssueSeverity_Object = MibTableColumn
issueSeverity = _IssueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 4, 1, 6),
    _IssueSeverity_Type()
)
issueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issueSeverity.setStatus("current")


class _Analytics_Type(Integer32):
    """Custom type analytics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1),
          ("error", 2))
    )


_Analytics_Type.__name__ = "Integer32"
_Analytics_Object = MibScalar
analytics = _Analytics_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 6, 5),
    _Analytics_Type()
)
analytics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analytics.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORERO-CMS-SYSTEM-STATUS-MIB",
    **{"systemStatus": systemStatus,
       "protection": protection,
       "device": device,
       "network": network,
       "issueTable": issueTable,
       "issueEntry": issueEntry,
       "issueIndex": issueIndex,
       "issueType": issueType,
       "issueDevice": issueDevice,
       "issueSegment": issueSegment,
       "issueDescription": issueDescription,
       "issueSeverity": issueSeverity,
       "analytics": analytics}
)
