# SNMP MIB module (RADIUS-ACC-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\RADIUS-ACC-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:06 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

radiusAccServMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1)
)
if mibBuilder.loadTexts:
    radiusAccServMIB.setRevisions(
        ("1999-06-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusMIB_ObjectIdentity = ObjectIdentity
radiusMIB = _RadiusMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67)
)
if mibBuilder.loadTexts:
    radiusMIB.setStatus("current")
_RadiusAccounting_ObjectIdentity = ObjectIdentity
radiusAccounting = _RadiusAccounting_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2)
)
_RadiusAccServMIBObjects_ObjectIdentity = ObjectIdentity
radiusAccServMIBObjects = _RadiusAccServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1)
)
_RadiusAccServ_ObjectIdentity = ObjectIdentity
radiusAccServ = _RadiusAccServ_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1)
)
_RadiusAccServIdent_Type = SnmpAdminString
_RadiusAccServIdent_Object = MibScalar
radiusAccServIdent = _RadiusAccServIdent_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 1),
    _RadiusAccServIdent_Type()
)
radiusAccServIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServIdent.setStatus("current")
_RadiusAccServUpTime_Type = TimeTicks
_RadiusAccServUpTime_Object = MibScalar
radiusAccServUpTime = _RadiusAccServUpTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 2),
    _RadiusAccServUpTime_Type()
)
radiusAccServUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServUpTime.setStatus("current")
_RadiusAccServResetTime_Type = TimeTicks
_RadiusAccServResetTime_Object = MibScalar
radiusAccServResetTime = _RadiusAccServResetTime_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 3),
    _RadiusAccServResetTime_Type()
)
radiusAccServResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServResetTime.setStatus("current")


class _RadiusAccServConfigReset_Type(Integer32):
    """Custom type radiusAccServConfigReset based on Integer32"""
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
        *(("other", 1),
          ("reset", 2),
          ("initializing", 3),
          ("running", 4))
    )


_RadiusAccServConfigReset_Type.__name__ = "Integer32"
_RadiusAccServConfigReset_Object = MibScalar
radiusAccServConfigReset = _RadiusAccServConfigReset_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 4),
    _RadiusAccServConfigReset_Type()
)
radiusAccServConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccServConfigReset.setStatus("current")
_RadiusAccServTotalRequests_Type = Counter32
_RadiusAccServTotalRequests_Object = MibScalar
radiusAccServTotalRequests = _RadiusAccServTotalRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 5),
    _RadiusAccServTotalRequests_Type()
)
radiusAccServTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalRequests.setStatus("current")
_RadiusAccServTotalInvalidRequests_Type = Counter32
_RadiusAccServTotalInvalidRequests_Object = MibScalar
radiusAccServTotalInvalidRequests = _RadiusAccServTotalInvalidRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 6),
    _RadiusAccServTotalInvalidRequests_Type()
)
radiusAccServTotalInvalidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalInvalidRequests.setStatus("current")
_RadiusAccServTotalDupRequests_Type = Counter32
_RadiusAccServTotalDupRequests_Object = MibScalar
radiusAccServTotalDupRequests = _RadiusAccServTotalDupRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 7),
    _RadiusAccServTotalDupRequests_Type()
)
radiusAccServTotalDupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalDupRequests.setStatus("current")
_RadiusAccServTotalResponses_Type = Counter32
_RadiusAccServTotalResponses_Object = MibScalar
radiusAccServTotalResponses = _RadiusAccServTotalResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 8),
    _RadiusAccServTotalResponses_Type()
)
radiusAccServTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalResponses.setStatus("current")
_RadiusAccServTotalMalformedRequests_Type = Counter32
_RadiusAccServTotalMalformedRequests_Object = MibScalar
radiusAccServTotalMalformedRequests = _RadiusAccServTotalMalformedRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 9),
    _RadiusAccServTotalMalformedRequests_Type()
)
radiusAccServTotalMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalMalformedRequests.setStatus("current")
_RadiusAccServTotalBadAuthenticators_Type = Counter32
_RadiusAccServTotalBadAuthenticators_Object = MibScalar
radiusAccServTotalBadAuthenticators = _RadiusAccServTotalBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 10),
    _RadiusAccServTotalBadAuthenticators_Type()
)
radiusAccServTotalBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalBadAuthenticators.setStatus("current")
_RadiusAccServTotalPacketsDropped_Type = Counter32
_RadiusAccServTotalPacketsDropped_Object = MibScalar
radiusAccServTotalPacketsDropped = _RadiusAccServTotalPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 11),
    _RadiusAccServTotalPacketsDropped_Type()
)
radiusAccServTotalPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalPacketsDropped.setStatus("current")
_RadiusAccServTotalNoRecords_Type = Counter32
_RadiusAccServTotalNoRecords_Object = MibScalar
radiusAccServTotalNoRecords = _RadiusAccServTotalNoRecords_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 12),
    _RadiusAccServTotalNoRecords_Type()
)
radiusAccServTotalNoRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalNoRecords.setStatus("current")
_RadiusAccServTotalUnknownTypes_Type = Counter32
_RadiusAccServTotalUnknownTypes_Object = MibScalar
radiusAccServTotalUnknownTypes = _RadiusAccServTotalUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 13),
    _RadiusAccServTotalUnknownTypes_Type()
)
radiusAccServTotalUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServTotalUnknownTypes.setStatus("current")
_RadiusAccClientTable_Object = MibTable
radiusAccClientTable = _RadiusAccClientTable_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    radiusAccClientTable.setStatus("current")
_RadiusAccClientEntry_Object = MibTableRow
radiusAccClientEntry = _RadiusAccClientEntry_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1)
)
radiusAccClientEntry.setIndexNames(
    (0, "RADIUS-ACC-SERVER-MIB", "radiusAccClientIndex"),
)
if mibBuilder.loadTexts:
    radiusAccClientEntry.setStatus("current")


class _RadiusAccClientIndex_Type(Integer32):
    """Custom type radiusAccClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusAccClientIndex_Type.__name__ = "Integer32"
_RadiusAccClientIndex_Object = MibTableColumn
radiusAccClientIndex = _RadiusAccClientIndex_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 1),
    _RadiusAccClientIndex_Type()
)
radiusAccClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAccClientIndex.setStatus("current")
_RadiusAccClientAddress_Type = IpAddress
_RadiusAccClientAddress_Object = MibTableColumn
radiusAccClientAddress = _RadiusAccClientAddress_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 2),
    _RadiusAccClientAddress_Type()
)
radiusAccClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientAddress.setStatus("current")
_RadiusAccClientID_Type = SnmpAdminString
_RadiusAccClientID_Object = MibTableColumn
radiusAccClientID = _RadiusAccClientID_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 3),
    _RadiusAccClientID_Type()
)
radiusAccClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccClientID.setStatus("current")
_RadiusAccServPacketsDropped_Type = Counter32
_RadiusAccServPacketsDropped_Object = MibTableColumn
radiusAccServPacketsDropped = _RadiusAccServPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 4),
    _RadiusAccServPacketsDropped_Type()
)
radiusAccServPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServPacketsDropped.setStatus("current")
_RadiusAccServRequests_Type = Counter32
_RadiusAccServRequests_Object = MibTableColumn
radiusAccServRequests = _RadiusAccServRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 5),
    _RadiusAccServRequests_Type()
)
radiusAccServRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServRequests.setStatus("current")
_RadiusAccServDupRequests_Type = Counter32
_RadiusAccServDupRequests_Object = MibTableColumn
radiusAccServDupRequests = _RadiusAccServDupRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 6),
    _RadiusAccServDupRequests_Type()
)
radiusAccServDupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServDupRequests.setStatus("current")
_RadiusAccServResponses_Type = Counter32
_RadiusAccServResponses_Object = MibTableColumn
radiusAccServResponses = _RadiusAccServResponses_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 7),
    _RadiusAccServResponses_Type()
)
radiusAccServResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServResponses.setStatus("current")
_RadiusAccServBadAuthenticators_Type = Counter32
_RadiusAccServBadAuthenticators_Object = MibTableColumn
radiusAccServBadAuthenticators = _RadiusAccServBadAuthenticators_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 8),
    _RadiusAccServBadAuthenticators_Type()
)
radiusAccServBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServBadAuthenticators.setStatus("current")
_RadiusAccServMalformedRequests_Type = Counter32
_RadiusAccServMalformedRequests_Object = MibTableColumn
radiusAccServMalformedRequests = _RadiusAccServMalformedRequests_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 9),
    _RadiusAccServMalformedRequests_Type()
)
radiusAccServMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServMalformedRequests.setStatus("current")
_RadiusAccServNoRecords_Type = Counter32
_RadiusAccServNoRecords_Object = MibTableColumn
radiusAccServNoRecords = _RadiusAccServNoRecords_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 10),
    _RadiusAccServNoRecords_Type()
)
radiusAccServNoRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServNoRecords.setStatus("current")
_RadiusAccServUnknownTypes_Type = Counter32
_RadiusAccServUnknownTypes_Object = MibTableColumn
radiusAccServUnknownTypes = _RadiusAccServUnknownTypes_Object(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 11),
    _RadiusAccServUnknownTypes_Type()
)
radiusAccServUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAccServUnknownTypes.setStatus("current")
_RadiusAccServMIBConformance_ObjectIdentity = ObjectIdentity
radiusAccServMIBConformance = _RadiusAccServMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2)
)
_RadiusAccServMIBCompliances_ObjectIdentity = ObjectIdentity
radiusAccServMIBCompliances = _RadiusAccServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1)
)
_RadiusAccServMIBGroups_ObjectIdentity = ObjectIdentity
radiusAccServMIBGroups = _RadiusAccServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2)
)

# Managed Objects groups

radiusAccServMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 1)
)
radiusAccServMIBGroup.setObjects(
      *(("RADIUS-ACC-SERVER-MIB", "radiusAccServIdent"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServUpTime"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServResetTime"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServConfigReset"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalInvalidRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalDupRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalResponses"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalMalformedRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalBadAuthenticators"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalPacketsDropped"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalNoRecords"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalUnknownTypes"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccClientAddress"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccClientID"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServPacketsDropped"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServDupRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServResponses"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServBadAuthenticators"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServMalformedRequests"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServNoRecords"),
        ("RADIUS-ACC-SERVER-MIB", "radiusAccServUnknownTypes"))
)
if mibBuilder.loadTexts:
    radiusAccServMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

radiusAccServMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1, 1)
)
radiusAccServMIBCompliance.setObjects(
    ("RADIUS-ACC-SERVER-MIB", "radiusAccServMIBGroup")
)
if mibBuilder.loadTexts:
    radiusAccServMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-ACC-SERVER-MIB",
    **{"radiusMIB": radiusMIB,
       "radiusAccounting": radiusAccounting,
       "radiusAccServMIB": radiusAccServMIB,
       "radiusAccServMIBObjects": radiusAccServMIBObjects,
       "radiusAccServ": radiusAccServ,
       "radiusAccServIdent": radiusAccServIdent,
       "radiusAccServUpTime": radiusAccServUpTime,
       "radiusAccServResetTime": radiusAccServResetTime,
       "radiusAccServConfigReset": radiusAccServConfigReset,
       "radiusAccServTotalRequests": radiusAccServTotalRequests,
       "radiusAccServTotalInvalidRequests": radiusAccServTotalInvalidRequests,
       "radiusAccServTotalDupRequests": radiusAccServTotalDupRequests,
       "radiusAccServTotalResponses": radiusAccServTotalResponses,
       "radiusAccServTotalMalformedRequests": radiusAccServTotalMalformedRequests,
       "radiusAccServTotalBadAuthenticators": radiusAccServTotalBadAuthenticators,
       "radiusAccServTotalPacketsDropped": radiusAccServTotalPacketsDropped,
       "radiusAccServTotalNoRecords": radiusAccServTotalNoRecords,
       "radiusAccServTotalUnknownTypes": radiusAccServTotalUnknownTypes,
       "radiusAccClientTable": radiusAccClientTable,
       "radiusAccClientEntry": radiusAccClientEntry,
       "radiusAccClientIndex": radiusAccClientIndex,
       "radiusAccClientAddress": radiusAccClientAddress,
       "radiusAccClientID": radiusAccClientID,
       "radiusAccServPacketsDropped": radiusAccServPacketsDropped,
       "radiusAccServRequests": radiusAccServRequests,
       "radiusAccServDupRequests": radiusAccServDupRequests,
       "radiusAccServResponses": radiusAccServResponses,
       "radiusAccServBadAuthenticators": radiusAccServBadAuthenticators,
       "radiusAccServMalformedRequests": radiusAccServMalformedRequests,
       "radiusAccServNoRecords": radiusAccServNoRecords,
       "radiusAccServUnknownTypes": radiusAccServUnknownTypes,
       "radiusAccServMIBConformance": radiusAccServMIBConformance,
       "radiusAccServMIBCompliances": radiusAccServMIBCompliances,
       "radiusAccServMIBCompliance": radiusAccServMIBCompliance,
       "radiusAccServMIBGroups": radiusAccServMIBGroups,
       "radiusAccServMIBGroup": radiusAccServMIBGroup}
)
