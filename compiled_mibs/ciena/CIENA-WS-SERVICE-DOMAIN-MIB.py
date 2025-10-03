# SNMP MIB module (CIENA-WS-SERVICE-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-SERVICE-DOMAIN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:14 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(DescriptionString,
 NameString,
 PortId,
 ServiceDomainIdx,
 ServiceIdx) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "DescriptionString",
    "NameString",
    "PortId",
    "ServiceDomainIdx",
    "ServiceIdx")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaWsServiceDomainMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11)
)
if mibBuilder.loadTexts:
    cienaWsServiceDomainMIB.setRevisions(
        ("2017-03-02 00:00",
         "2016-12-12 00:00",
         "2015-06-17 00:00",
         "2015-04-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaWsServiceDomainObjects_ObjectIdentity = ObjectIdentity
cienaWsServiceDomainObjects = _CienaWsServiceDomainObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 1)
)
_CienaWsServiceDomainConformance_ObjectIdentity = ObjectIdentity
cienaWsServiceDomainConformance = _CienaWsServiceDomainConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 2)
)
_CienaWsServiceDomainGroups_ObjectIdentity = ObjectIdentity
cienaWsServiceDomainGroups = _CienaWsServiceDomainGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 2, 1)
)
_CienaWsServiceDomainCompliances_ObjectIdentity = ObjectIdentity
cienaWsServiceDomainCompliances = _CienaWsServiceDomainCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 2, 2)
)
_CwsServiceDomainServiceDomainsTable_Object = MibTable
cwsServiceDomainServiceDomainsTable = _CwsServiceDomainServiceDomainsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 3)
)
if mibBuilder.loadTexts:
    cwsServiceDomainServiceDomainsTable.setStatus("current")
_CwsServiceDomainServiceDomainsEntry_Object = MibTableRow
cwsServiceDomainServiceDomainsEntry = _CwsServiceDomainServiceDomainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 3, 1)
)
cwsServiceDomainServiceDomainsEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceDomainsServiceDomainIndex"),
)
if mibBuilder.loadTexts:
    cwsServiceDomainServiceDomainsEntry.setStatus("current")


class _CwsServiceDomainServiceDomainsServiceDomainIndex_Type(Integer32):
    """Custom type cwsServiceDomainServiceDomainsServiceDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServiceDomainServiceDomainsServiceDomainIndex_Type.__name__ = "Integer32"
_CwsServiceDomainServiceDomainsServiceDomainIndex_Object = MibTableColumn
cwsServiceDomainServiceDomainsServiceDomainIndex = _CwsServiceDomainServiceDomainsServiceDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 3, 1, 1),
    _CwsServiceDomainServiceDomainsServiceDomainIndex_Type()
)
cwsServiceDomainServiceDomainsServiceDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsServiceDomainServiceDomainsServiceDomainIndex.setStatus("current")
_CwsServiceDomainServiceDomainIdTable_Object = MibTable
cwsServiceDomainServiceDomainIdTable = _CwsServiceDomainServiceDomainIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 4)
)
if mibBuilder.loadTexts:
    cwsServiceDomainServiceDomainIdTable.setStatus("current")
_CwsServiceDomainServiceDomainIdEntry_Object = MibTableRow
cwsServiceDomainServiceDomainIdEntry = _CwsServiceDomainServiceDomainIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 4, 1)
)
cwsServiceDomainServiceDomainIdEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceDomainsServiceDomainIndex"),
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceDomainIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsServiceDomainServiceDomainIdEntry.setStatus("current")


class _CwsServiceDomainServiceDomainIdTableSnmpKey_Type(Integer32):
    """Custom type cwsServiceDomainServiceDomainIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServiceDomainServiceDomainIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsServiceDomainServiceDomainIdTableSnmpKey_Object = MibTableColumn
cwsServiceDomainServiceDomainIdTableSnmpKey = _CwsServiceDomainServiceDomainIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 4, 1, 1),
    _CwsServiceDomainServiceDomainIdTableSnmpKey_Type()
)
cwsServiceDomainServiceDomainIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsServiceDomainServiceDomainIdTableSnmpKey.setStatus("current")
_CwsServiceDomainServiceDomainIdName_Type = NameString
_CwsServiceDomainServiceDomainIdName_Object = MibTableColumn
cwsServiceDomainServiceDomainIdName = _CwsServiceDomainServiceDomainIdName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 4, 1, 2),
    _CwsServiceDomainServiceDomainIdName_Type()
)
cwsServiceDomainServiceDomainIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServiceDomainServiceDomainIdName.setStatus("current")
_CwsServiceDomainServiceDomainIdDescription_Type = DescriptionString
_CwsServiceDomainServiceDomainIdDescription_Object = MibTableColumn
cwsServiceDomainServiceDomainIdDescription = _CwsServiceDomainServiceDomainIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 4, 1, 3),
    _CwsServiceDomainServiceDomainIdDescription_Type()
)
cwsServiceDomainServiceDomainIdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServiceDomainServiceDomainIdDescription.setStatus("current")
_CwsServiceDomainPortMembersTable_Object = MibTable
cwsServiceDomainPortMembersTable = _CwsServiceDomainPortMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 5)
)
if mibBuilder.loadTexts:
    cwsServiceDomainPortMembersTable.setStatus("current")
_CwsServiceDomainPortMembersEntry_Object = MibTableRow
cwsServiceDomainPortMembersEntry = _CwsServiceDomainPortMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 5, 1)
)
cwsServiceDomainPortMembersEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceDomainsServiceDomainIndex"),
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainLinkedReferencesTableSnmpKey"),
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainPortMembersTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsServiceDomainPortMembersEntry.setStatus("current")


class _CwsServiceDomainPortMembersTableSnmpKey_Type(Integer32):
    """Custom type cwsServiceDomainPortMembersTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServiceDomainPortMembersTableSnmpKey_Type.__name__ = "Integer32"
_CwsServiceDomainPortMembersTableSnmpKey_Object = MibTableColumn
cwsServiceDomainPortMembersTableSnmpKey = _CwsServiceDomainPortMembersTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 5, 1, 1),
    _CwsServiceDomainPortMembersTableSnmpKey_Type()
)
cwsServiceDomainPortMembersTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsServiceDomainPortMembersTableSnmpKey.setStatus("current")
_CwsServiceDomainPortMembers_Type = PortId
_CwsServiceDomainPortMembers_Object = MibTableColumn
cwsServiceDomainPortMembers = _CwsServiceDomainPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 5, 1, 2),
    _CwsServiceDomainPortMembers_Type()
)
cwsServiceDomainPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsServiceDomainPortMembers.setStatus("current")
_CwsServiceDomainLinkedReferencesTable_Object = MibTable
cwsServiceDomainLinkedReferencesTable = _CwsServiceDomainLinkedReferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 6)
)
if mibBuilder.loadTexts:
    cwsServiceDomainLinkedReferencesTable.setStatus("current")
_CwsServiceDomainLinkedReferencesEntry_Object = MibTableRow
cwsServiceDomainLinkedReferencesEntry = _CwsServiceDomainLinkedReferencesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 6, 1)
)
cwsServiceDomainLinkedReferencesEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainLinkedReferencesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsServiceDomainLinkedReferencesEntry.setStatus("current")


class _CwsServiceDomainLinkedReferencesTableSnmpKey_Type(Integer32):
    """Custom type cwsServiceDomainLinkedReferencesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServiceDomainLinkedReferencesTableSnmpKey_Type.__name__ = "Integer32"
_CwsServiceDomainLinkedReferencesTableSnmpKey_Object = MibTableColumn
cwsServiceDomainLinkedReferencesTableSnmpKey = _CwsServiceDomainLinkedReferencesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 6, 1, 1),
    _CwsServiceDomainLinkedReferencesTableSnmpKey_Type()
)
cwsServiceDomainLinkedReferencesTableSnmpKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsServiceDomainLinkedReferencesTableSnmpKey.setStatus("current")
_CwsServiceDomainServiceMembersTable_Object = MibTable
cwsServiceDomainServiceMembersTable = _CwsServiceDomainServiceMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 7)
)
if mibBuilder.loadTexts:
    cwsServiceDomainServiceMembersTable.setStatus("current")
_CwsServiceDomainServiceMembersEntry_Object = MibTableRow
cwsServiceDomainServiceMembersEntry = _CwsServiceDomainServiceMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 7, 1)
)
cwsServiceDomainServiceMembersEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceDomainsServiceDomainIndex"),
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainLinkedReferencesTableSnmpKey"),
    (0, "CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceMembersTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsServiceDomainServiceMembersEntry.setStatus("current")


class _CwsServiceDomainServiceMembersTableSnmpKey_Type(Integer32):
    """Custom type cwsServiceDomainServiceMembersTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServiceDomainServiceMembersTableSnmpKey_Type.__name__ = "Integer32"
_CwsServiceDomainServiceMembersTableSnmpKey_Object = MibTableColumn
cwsServiceDomainServiceMembersTableSnmpKey = _CwsServiceDomainServiceMembersTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 7, 1, 1),
    _CwsServiceDomainServiceMembersTableSnmpKey_Type()
)
cwsServiceDomainServiceMembersTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsServiceDomainServiceMembersTableSnmpKey.setStatus("current")
_CwsServiceDomainServiceMembers_Type = ServiceIdx
_CwsServiceDomainServiceMembers_Object = MibTableColumn
cwsServiceDomainServiceMembers = _CwsServiceDomainServiceMembers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 7, 1, 2),
    _CwsServiceDomainServiceMembers_Type()
)
cwsServiceDomainServiceMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsServiceDomainServiceMembers.setStatus("current")

# Managed Objects groups

cienaWsServiceDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 2, 1, 1)
)
cienaWsServiceDomainGroup.setObjects(
      *(("CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceDomainsServiceDomainIndex"),
        ("CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceDomainIdName"),
        ("CIENA-WS-SERVICE-DOMAIN-MIB", "cwsServiceDomainServiceDomainIdDescription"))
)
if mibBuilder.loadTexts:
    cienaWsServiceDomainGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsServiceDomainCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 11, 2, 2, 1)
)
cienaWsServiceDomainCompliance.setObjects(
    ("CIENA-WS-SERVICE-DOMAIN-MIB", "cienaWsServiceDomainGroup")
)
if mibBuilder.loadTexts:
    cienaWsServiceDomainCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-SERVICE-DOMAIN-MIB",
    **{"cienaWsServiceDomainMIB": cienaWsServiceDomainMIB,
       "cienaWsServiceDomainObjects": cienaWsServiceDomainObjects,
       "cienaWsServiceDomainConformance": cienaWsServiceDomainConformance,
       "cienaWsServiceDomainGroups": cienaWsServiceDomainGroups,
       "cienaWsServiceDomainGroup": cienaWsServiceDomainGroup,
       "cienaWsServiceDomainCompliances": cienaWsServiceDomainCompliances,
       "cienaWsServiceDomainCompliance": cienaWsServiceDomainCompliance,
       "cwsServiceDomainServiceDomainsTable": cwsServiceDomainServiceDomainsTable,
       "cwsServiceDomainServiceDomainsEntry": cwsServiceDomainServiceDomainsEntry,
       "cwsServiceDomainServiceDomainsServiceDomainIndex": cwsServiceDomainServiceDomainsServiceDomainIndex,
       "cwsServiceDomainServiceDomainIdTable": cwsServiceDomainServiceDomainIdTable,
       "cwsServiceDomainServiceDomainIdEntry": cwsServiceDomainServiceDomainIdEntry,
       "cwsServiceDomainServiceDomainIdTableSnmpKey": cwsServiceDomainServiceDomainIdTableSnmpKey,
       "cwsServiceDomainServiceDomainIdName": cwsServiceDomainServiceDomainIdName,
       "cwsServiceDomainServiceDomainIdDescription": cwsServiceDomainServiceDomainIdDescription,
       "cwsServiceDomainPortMembersTable": cwsServiceDomainPortMembersTable,
       "cwsServiceDomainPortMembersEntry": cwsServiceDomainPortMembersEntry,
       "cwsServiceDomainPortMembersTableSnmpKey": cwsServiceDomainPortMembersTableSnmpKey,
       "cwsServiceDomainPortMembers": cwsServiceDomainPortMembers,
       "cwsServiceDomainLinkedReferencesTable": cwsServiceDomainLinkedReferencesTable,
       "cwsServiceDomainLinkedReferencesEntry": cwsServiceDomainLinkedReferencesEntry,
       "cwsServiceDomainLinkedReferencesTableSnmpKey": cwsServiceDomainLinkedReferencesTableSnmpKey,
       "cwsServiceDomainServiceMembersTable": cwsServiceDomainServiceMembersTable,
       "cwsServiceDomainServiceMembersEntry": cwsServiceDomainServiceMembersEntry,
       "cwsServiceDomainServiceMembersTableSnmpKey": cwsServiceDomainServiceMembersTableSnmpKey,
       "cwsServiceDomainServiceMembers": cwsServiceDomainServiceMembers}
)
