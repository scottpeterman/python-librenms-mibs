# SNMP MIB module (CIENA-WS-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-SERVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:15 2025
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
 EnabledDisabledEnum,
 PortId,
 ServiceDomainIdx,
 ServiceIdx) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "DescriptionString",
    "EnabledDisabledEnum",
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

cienaWsServiceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cienaWsServiceMIB.setRevisions(
        ("2017-07-18 00:00",
         "2017-03-02 00:00",
         "2016-12-12 00:00",
         "2016-06-17 00:00",
         "2015-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ServiceId(TextualConvention, Unsigned32):
    status = "current"


class ServiceMaxPort(TextualConvention, Unsigned32):
    status = "current"


class ServiceNameStr(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsServiceObjects_ObjectIdentity = ObjectIdentity
cienaWsServiceObjects = _CienaWsServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 1)
)
_CienaWsServiceConformance_ObjectIdentity = ObjectIdentity
cienaWsServiceConformance = _CienaWsServiceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2)
)
_CienaWsServiceGroups_ObjectIdentity = ObjectIdentity
cienaWsServiceGroups = _CienaWsServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2, 1)
)
_CienaWsServiceCompliances_ObjectIdentity = ObjectIdentity
cienaWsServiceCompliances = _CienaWsServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2, 2)
)
_CwsServiceServicesTable_Object = MibTable
cwsServiceServicesTable = _CwsServiceServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    cwsServiceServicesTable.setStatus("current")
_CwsServiceServicesEntry_Object = MibTableRow
cwsServiceServicesEntry = _CwsServiceServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 3, 1)
)
cwsServiceServicesEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"),
)
if mibBuilder.loadTexts:
    cwsServiceServicesEntry.setStatus("current")


class _CwsServiceServicesServiceIndex_Type(Integer32):
    """Custom type cwsServiceServicesServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServiceServicesServiceIndex_Type.__name__ = "Integer32"
_CwsServiceServicesServiceIndex_Object = MibTableColumn
cwsServiceServicesServiceIndex = _CwsServiceServicesServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 3, 1, 1),
    _CwsServiceServicesServiceIndex_Type()
)
cwsServiceServicesServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsServiceServicesServiceIndex.setStatus("current")
_CwsServiceIdTable_Object = MibTable
cwsServiceIdTable = _CwsServiceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4)
)
if mibBuilder.loadTexts:
    cwsServiceIdTable.setStatus("current")
_CwsServiceIdEntry_Object = MibTableRow
cwsServiceIdEntry = _CwsServiceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1)
)
cwsServiceIdEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"),
    (0, "CIENA-WS-SERVICE-MIB", "cwsServiceIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsServiceIdEntry.setStatus("current")


class _CwsServiceIdTableSnmpKey_Type(Integer32):
    """Custom type cwsServiceIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServiceIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsServiceIdTableSnmpKey_Object = MibTableColumn
cwsServiceIdTableSnmpKey = _CwsServiceIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1, 1),
    _CwsServiceIdTableSnmpKey_Type()
)
cwsServiceIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsServiceIdTableSnmpKey.setStatus("current")
_CwsServiceIdServiceId_Type = ServiceId
_CwsServiceIdServiceId_Object = MibTableColumn
cwsServiceIdServiceId = _CwsServiceIdServiceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1, 2),
    _CwsServiceIdServiceId_Type()
)
cwsServiceIdServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServiceIdServiceId.setStatus("current")
_CwsServiceIdName_Type = ServiceNameStr
_CwsServiceIdName_Object = MibTableColumn
cwsServiceIdName = _CwsServiceIdName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1, 3),
    _CwsServiceIdName_Type()
)
cwsServiceIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServiceIdName.setStatus("current")
_CwsServiceIdDescription_Type = DescriptionString
_CwsServiceIdDescription_Object = MibTableColumn
cwsServiceIdDescription = _CwsServiceIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1, 4),
    _CwsServiceIdDescription_Type()
)
cwsServiceIdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServiceIdDescription.setStatus("current")
_CwsServiceStateTable_Object = MibTable
cwsServiceStateTable = _CwsServiceStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 5)
)
if mibBuilder.loadTexts:
    cwsServiceStateTable.setStatus("current")
_CwsServiceStateEntry_Object = MibTableRow
cwsServiceStateEntry = _CwsServiceStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 5, 1)
)
cwsServiceStateEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"),
    (0, "CIENA-WS-SERVICE-MIB", "cwsServiceStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsServiceStateEntry.setStatus("current")


class _CwsServiceStateTableSnmpKey_Type(Integer32):
    """Custom type cwsServiceStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServiceStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsServiceStateTableSnmpKey_Object = MibTableColumn
cwsServiceStateTableSnmpKey = _CwsServiceStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 5, 1, 1),
    _CwsServiceStateTableSnmpKey_Type()
)
cwsServiceStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsServiceStateTableSnmpKey.setStatus("current")
_CwsServiceStateAdminState_Type = EnabledDisabledEnum
_CwsServiceStateAdminState_Object = MibTableColumn
cwsServiceStateAdminState = _CwsServiceStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 5, 1, 2),
    _CwsServiceStateAdminState_Type()
)
cwsServiceStateAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsServiceStateAdminState.setStatus("current")
_CwsServicePropertiesTable_Object = MibTable
cwsServicePropertiesTable = _CwsServicePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6)
)
if mibBuilder.loadTexts:
    cwsServicePropertiesTable.setStatus("current")
_CwsServicePropertiesEntry_Object = MibTableRow
cwsServicePropertiesEntry = _CwsServicePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1)
)
cwsServicePropertiesEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"),
    (0, "CIENA-WS-SERVICE-MIB", "cwsServicePropertiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsServicePropertiesEntry.setStatus("current")


class _CwsServicePropertiesTableSnmpKey_Type(Integer32):
    """Custom type cwsServicePropertiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServicePropertiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsServicePropertiesTableSnmpKey_Object = MibTableColumn
cwsServicePropertiesTableSnmpKey = _CwsServicePropertiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 1),
    _CwsServicePropertiesTableSnmpKey_Type()
)
cwsServicePropertiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsServicePropertiesTableSnmpKey.setStatus("current")


class _CwsServicePropertiesType_Type(Integer32):
    """Custom type cwsServicePropertiesType based on Integer32"""
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
        *(("epl", 0),
          ("evpl", 1),
          ("etree", 2),
          ("elan", 3),
          ("eepl", 4))
    )


_CwsServicePropertiesType_Type.__name__ = "Integer32"
_CwsServicePropertiesType_Object = MibTableColumn
cwsServicePropertiesType = _CwsServicePropertiesType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 2),
    _CwsServicePropertiesType_Type()
)
cwsServicePropertiesType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServicePropertiesType.setStatus("current")
_CwsServicePropertiesMaxNumberOfPort_Type = ServiceMaxPort
_CwsServicePropertiesMaxNumberOfPort_Object = MibTableColumn
cwsServicePropertiesMaxNumberOfPort = _CwsServicePropertiesMaxNumberOfPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 3),
    _CwsServicePropertiesMaxNumberOfPort_Type()
)
cwsServicePropertiesMaxNumberOfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsServicePropertiesMaxNumberOfPort.setStatus("current")


class _CwsServicePropertiesProtectionState_Type(Integer32):
    """Custom type cwsServicePropertiesProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 0),
          ("unprotected", 1))
    )


_CwsServicePropertiesProtectionState_Type.__name__ = "Integer32"
_CwsServicePropertiesProtectionState_Object = MibTableColumn
cwsServicePropertiesProtectionState = _CwsServicePropertiesProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 4),
    _CwsServicePropertiesProtectionState_Type()
)
cwsServicePropertiesProtectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServicePropertiesProtectionState.setStatus("current")
_CwsServicePropertiesLinkStateForwarding_Type = EnabledDisabledEnum
_CwsServicePropertiesLinkStateForwarding_Object = MibTableColumn
cwsServicePropertiesLinkStateForwarding = _CwsServicePropertiesLinkStateForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 5),
    _CwsServicePropertiesLinkStateForwarding_Type()
)
cwsServicePropertiesLinkStateForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServicePropertiesLinkStateForwarding.setStatus("current")
_CwsServicePropertiesMacLearning_Type = EnabledDisabledEnum
_CwsServicePropertiesMacLearning_Object = MibTableColumn
cwsServicePropertiesMacLearning = _CwsServicePropertiesMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 6),
    _CwsServicePropertiesMacLearning_Type()
)
cwsServicePropertiesMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServicePropertiesMacLearning.setStatus("current")
_CwsServicePropertiesParentSvcDomainIdxReference_Type = ServiceDomainIdx
_CwsServicePropertiesParentSvcDomainIdxReference_Object = MibTableColumn
cwsServicePropertiesParentSvcDomainIdxReference = _CwsServicePropertiesParentSvcDomainIdxReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 7),
    _CwsServicePropertiesParentSvcDomainIdxReference_Type()
)
cwsServicePropertiesParentSvcDomainIdxReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsServicePropertiesParentSvcDomainIdxReference.setStatus("current")
_CwsServicePortMembersReferenceTable_Object = MibTable
cwsServicePortMembersReferenceTable = _CwsServicePortMembersReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 7)
)
if mibBuilder.loadTexts:
    cwsServicePortMembersReferenceTable.setStatus("current")
_CwsServicePortMembersReferenceEntry_Object = MibTableRow
cwsServicePortMembersReferenceEntry = _CwsServicePortMembersReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 7, 1)
)
cwsServicePortMembersReferenceEntry.setIndexNames(
    (0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"),
    (0, "CIENA-WS-SERVICE-MIB", "cwsServicePropertiesTableSnmpKey"),
    (0, "CIENA-WS-SERVICE-MIB", "cwsServicePortMembersReferenceTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsServicePortMembersReferenceEntry.setStatus("current")


class _CwsServicePortMembersReferenceTableSnmpKey_Type(Integer32):
    """Custom type cwsServicePortMembersReferenceTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsServicePortMembersReferenceTableSnmpKey_Type.__name__ = "Integer32"
_CwsServicePortMembersReferenceTableSnmpKey_Object = MibTableColumn
cwsServicePortMembersReferenceTableSnmpKey = _CwsServicePortMembersReferenceTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 7, 1, 1),
    _CwsServicePortMembersReferenceTableSnmpKey_Type()
)
cwsServicePortMembersReferenceTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsServicePortMembersReferenceTableSnmpKey.setStatus("current")
_CwsServicePortMembersReference_Type = PortId
_CwsServicePortMembersReference_Object = MibTableColumn
cwsServicePortMembersReference = _CwsServicePortMembersReference_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 7, 1, 2),
    _CwsServicePortMembersReference_Type()
)
cwsServicePortMembersReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsServicePortMembersReference.setStatus("current")

# Managed Objects groups

cienaWsServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2, 1, 1)
)
cienaWsServiceGroup.setObjects(
      *(("CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"),
        ("CIENA-WS-SERVICE-MIB", "cwsServiceIdServiceId"),
        ("CIENA-WS-SERVICE-MIB", "cwsServiceIdName"),
        ("CIENA-WS-SERVICE-MIB", "cwsServiceIdDescription"),
        ("CIENA-WS-SERVICE-MIB", "cwsServiceStateAdminState"),
        ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesType"),
        ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesMaxNumberOfPort"),
        ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesProtectionState"),
        ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesLinkStateForwarding"),
        ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesMacLearning"),
        ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesParentSvcDomainIdxReference"))
)
if mibBuilder.loadTexts:
    cienaWsServiceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2, 2, 1)
)
cienaWsServiceCompliance.setObjects(
    ("CIENA-WS-SERVICE-MIB", "cienaWsServiceGroup")
)
if mibBuilder.loadTexts:
    cienaWsServiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-SERVICE-MIB",
    **{"ServiceId": ServiceId,
       "ServiceMaxPort": ServiceMaxPort,
       "ServiceNameStr": ServiceNameStr,
       "cienaWsServiceMIB": cienaWsServiceMIB,
       "cienaWsServiceObjects": cienaWsServiceObjects,
       "cienaWsServiceConformance": cienaWsServiceConformance,
       "cienaWsServiceGroups": cienaWsServiceGroups,
       "cienaWsServiceGroup": cienaWsServiceGroup,
       "cienaWsServiceCompliances": cienaWsServiceCompliances,
       "cienaWsServiceCompliance": cienaWsServiceCompliance,
       "cwsServiceServicesTable": cwsServiceServicesTable,
       "cwsServiceServicesEntry": cwsServiceServicesEntry,
       "cwsServiceServicesServiceIndex": cwsServiceServicesServiceIndex,
       "cwsServiceIdTable": cwsServiceIdTable,
       "cwsServiceIdEntry": cwsServiceIdEntry,
       "cwsServiceIdTableSnmpKey": cwsServiceIdTableSnmpKey,
       "cwsServiceIdServiceId": cwsServiceIdServiceId,
       "cwsServiceIdName": cwsServiceIdName,
       "cwsServiceIdDescription": cwsServiceIdDescription,
       "cwsServiceStateTable": cwsServiceStateTable,
       "cwsServiceStateEntry": cwsServiceStateEntry,
       "cwsServiceStateTableSnmpKey": cwsServiceStateTableSnmpKey,
       "cwsServiceStateAdminState": cwsServiceStateAdminState,
       "cwsServicePropertiesTable": cwsServicePropertiesTable,
       "cwsServicePropertiesEntry": cwsServicePropertiesEntry,
       "cwsServicePropertiesTableSnmpKey": cwsServicePropertiesTableSnmpKey,
       "cwsServicePropertiesType": cwsServicePropertiesType,
       "cwsServicePropertiesMaxNumberOfPort": cwsServicePropertiesMaxNumberOfPort,
       "cwsServicePropertiesProtectionState": cwsServicePropertiesProtectionState,
       "cwsServicePropertiesLinkStateForwarding": cwsServicePropertiesLinkStateForwarding,
       "cwsServicePropertiesMacLearning": cwsServicePropertiesMacLearning,
       "cwsServicePropertiesParentSvcDomainIdxReference": cwsServicePropertiesParentSvcDomainIdxReference,
       "cwsServicePortMembersReferenceTable": cwsServicePortMembersReferenceTable,
       "cwsServicePortMembersReferenceEntry": cwsServicePortMembersReferenceEntry,
       "cwsServicePortMembersReferenceTableSnmpKey": cwsServicePortMembersReferenceTableSnmpKey,
       "cwsServicePortMembersReference": cwsServicePortMembersReference}
)
