# SNMP MIB module (DLINKSW-AAA-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-AAA-AUTH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:35 2025
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

(DAaaMethodListName,
 DAaaMethodName,
 DAaaMethodPriority,
 DAaaSessionType,
 dAaaMIBObjects) = mibBuilder.importSymbols(
    "DLINKSW-AAA-COMMON-MIB",
    "DAaaMethodListName",
    "DAaaMethodName",
    "DAaaMethodPriority",
    "DAaaSessionType",
    "dAaaMIBObjects")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwAaaAuthenticationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4)
)
if mibBuilder.loadTexts:
    dlinkSwAaaAuthenticationMIB.setRevisions(
        ("2013-04-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DAaaAuthMIBNotifications_ObjectIdentity = ObjectIdentity
dAaaAuthMIBNotifications = _DAaaAuthMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 0)
)
_DAaaAuthMIBObjects_ObjectIdentity = ObjectIdentity
dAaaAuthMIBObjects = _DAaaAuthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1)
)
_DAaaAuthGenericMethodTable_Object = MibTable
dAaaAuthGenericMethodTable = _DAaaAuthGenericMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dAaaAuthGenericMethodTable.setStatus("current")
_DAaaAuthGenericMethodEntry_Object = MibTableRow
dAaaAuthGenericMethodEntry = _DAaaAuthGenericMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 1, 1)
)
dAaaAuthGenericMethodEntry.setIndexNames(
    (0, "DLINKSW-AAA-AUTH-MIB", "dAaaAuthGenMethodLstType"),
    (0, "DLINKSW-AAA-AUTH-MIB", "dAaaAuthGenMethodLstName"),
    (0, "DLINKSW-AAA-AUTH-MIB", "dAaaAuthGenMethodPriority"),
)
if mibBuilder.loadTexts:
    dAaaAuthGenericMethodEntry.setStatus("current")


class _DAaaAuthGenMethodLstType_Type(Integer32):
    """Custom type dAaaAuthGenMethodLstType based on Integer32"""
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
        *(("enable", 1),
          ("login", 2),
          ("dot1x", 3),
          ("jwac", 4),
          ("macAuth", 5),
          ("web", 6),
          ("igmpAuth", 7),
          ("mldAuth", 8))
    )


_DAaaAuthGenMethodLstType_Type.__name__ = "Integer32"
_DAaaAuthGenMethodLstType_Object = MibTableColumn
dAaaAuthGenMethodLstType = _DAaaAuthGenMethodLstType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 1, 1, 1),
    _DAaaAuthGenMethodLstType_Type()
)
dAaaAuthGenMethodLstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAuthGenMethodLstType.setStatus("current")
_DAaaAuthGenMethodLstName_Type = DAaaMethodListName
_DAaaAuthGenMethodLstName_Object = MibTableColumn
dAaaAuthGenMethodLstName = _DAaaAuthGenMethodLstName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 1, 1, 2),
    _DAaaAuthGenMethodLstName_Type()
)
dAaaAuthGenMethodLstName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAuthGenMethodLstName.setStatus("current")
_DAaaAuthGenMethodPriority_Type = DAaaMethodPriority
_DAaaAuthGenMethodPriority_Object = MibTableColumn
dAaaAuthGenMethodPriority = _DAaaAuthGenMethodPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 1, 1, 3),
    _DAaaAuthGenMethodPriority_Type()
)
dAaaAuthGenMethodPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAuthGenMethodPriority.setStatus("current")
_DAaaAuthGenMethodName_Type = DAaaMethodName
_DAaaAuthGenMethodName_Object = MibTableColumn
dAaaAuthGenMethodName = _DAaaAuthGenMethodName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 1, 1, 4),
    _DAaaAuthGenMethodName_Type()
)
dAaaAuthGenMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAuthGenMethodName.setStatus("current")
_DAaaAuthGenMethodRowStatus_Type = RowStatus
_DAaaAuthGenMethodRowStatus_Object = MibTableColumn
dAaaAuthGenMethodRowStatus = _DAaaAuthGenMethodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 1, 1, 5),
    _DAaaAuthGenMethodRowStatus_Type()
)
dAaaAuthGenMethodRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAuthGenMethodRowStatus.setStatus("current")
_DAaaAuthLogin_ObjectIdentity = ObjectIdentity
dAaaAuthLogin = _DAaaAuthLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 2)
)
_DAaaAuthLoginApplyTable_Object = MibTable
dAaaAuthLoginApplyTable = _DAaaAuthLoginApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dAaaAuthLoginApplyTable.setStatus("current")
_DAaaAuthLoginApplyEntry_Object = MibTableRow
dAaaAuthLoginApplyEntry = _DAaaAuthLoginApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 2, 1, 1)
)
dAaaAuthLoginApplyEntry.setIndexNames(
    (0, "DLINKSW-AAA-AUTH-MIB", "dAaaAuthLoginApplySession"),
)
if mibBuilder.loadTexts:
    dAaaAuthLoginApplyEntry.setStatus("current")
_DAaaAuthLoginApplySession_Type = DAaaSessionType
_DAaaAuthLoginApplySession_Object = MibTableColumn
dAaaAuthLoginApplySession = _DAaaAuthLoginApplySession_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 2, 1, 1, 1),
    _DAaaAuthLoginApplySession_Type()
)
dAaaAuthLoginApplySession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAuthLoginApplySession.setStatus("current")
_DAaaAuthLoginApplyListName_Type = DAaaMethodListName
_DAaaAuthLoginApplyListName_Object = MibTableColumn
dAaaAuthLoginApplyListName = _DAaaAuthLoginApplyListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 2, 1, 1, 2),
    _DAaaAuthLoginApplyListName_Type()
)
dAaaAuthLoginApplyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAuthLoginApplyListName.setStatus("current")
_DAaaAuthLoginApplyRowStatus_Type = RowStatus
_DAaaAuthLoginApplyRowStatus_Object = MibTableColumn
dAaaAuthLoginApplyRowStatus = _DAaaAuthLoginApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 1, 2, 1, 1, 3),
    _DAaaAuthLoginApplyRowStatus_Type()
)
dAaaAuthLoginApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAuthLoginApplyRowStatus.setStatus("current")
_DAaaAuthMIBConformance_ObjectIdentity = ObjectIdentity
dAaaAuthMIBConformance = _DAaaAuthMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 2)
)
_DAaaAuthMIBCompliances_ObjectIdentity = ObjectIdentity
dAaaAuthMIBCompliances = _DAaaAuthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 2, 1)
)
_DAaaAuthMIBGroups_ObjectIdentity = ObjectIdentity
dAaaAuthMIBGroups = _DAaaAuthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 2, 2)
)

# Managed Objects groups

dAaaAuthMethodListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 2, 2, 1)
)
dAaaAuthMethodListGroup.setObjects(
      *(("DLINKSW-AAA-AUTH-MIB", "dAaaAuthGenMethodName"),
        ("DLINKSW-AAA-AUTH-MIB", "dAaaAuthGenMethodRowStatus"))
)
if mibBuilder.loadTexts:
    dAaaAuthMethodListGroup.setStatus("current")

dAaaAuthcLoginMethodApplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 2, 2, 2)
)
dAaaAuthcLoginMethodApplyGroup.setObjects(
      *(("DLINKSW-AAA-AUTH-MIB", "dAaaAuthLoginApplyListName"),
        ("DLINKSW-AAA-AUTH-MIB", "dAaaAuthLoginApplyRowStatus"))
)
if mibBuilder.loadTexts:
    dAaaAuthcLoginMethodApplyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dAaaAuthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 4, 2, 1, 1)
)
dAaaAuthMIBCompliance.setObjects(
      *(("DLINKSW-AAA-AUTH-MIB", "dAaaAuthMethodListGroup"),
        ("DLINKSW-AAA-AUTH-MIB", "dAaaAuthcLoginMethodApplyGroup"))
)
if mibBuilder.loadTexts:
    dAaaAuthMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-AAA-AUTH-MIB",
    **{"dlinkSwAaaAuthenticationMIB": dlinkSwAaaAuthenticationMIB,
       "dAaaAuthMIBNotifications": dAaaAuthMIBNotifications,
       "dAaaAuthMIBObjects": dAaaAuthMIBObjects,
       "dAaaAuthGenericMethodTable": dAaaAuthGenericMethodTable,
       "dAaaAuthGenericMethodEntry": dAaaAuthGenericMethodEntry,
       "dAaaAuthGenMethodLstType": dAaaAuthGenMethodLstType,
       "dAaaAuthGenMethodLstName": dAaaAuthGenMethodLstName,
       "dAaaAuthGenMethodPriority": dAaaAuthGenMethodPriority,
       "dAaaAuthGenMethodName": dAaaAuthGenMethodName,
       "dAaaAuthGenMethodRowStatus": dAaaAuthGenMethodRowStatus,
       "dAaaAuthLogin": dAaaAuthLogin,
       "dAaaAuthLoginApplyTable": dAaaAuthLoginApplyTable,
       "dAaaAuthLoginApplyEntry": dAaaAuthLoginApplyEntry,
       "dAaaAuthLoginApplySession": dAaaAuthLoginApplySession,
       "dAaaAuthLoginApplyListName": dAaaAuthLoginApplyListName,
       "dAaaAuthLoginApplyRowStatus": dAaaAuthLoginApplyRowStatus,
       "dAaaAuthMIBConformance": dAaaAuthMIBConformance,
       "dAaaAuthMIBCompliances": dAaaAuthMIBCompliances,
       "dAaaAuthMIBCompliance": dAaaAuthMIBCompliance,
       "dAaaAuthMIBGroups": dAaaAuthMIBGroups,
       "dAaaAuthMethodListGroup": dAaaAuthMethodListGroup,
       "dAaaAuthcLoginMethodApplyGroup": dAaaAuthcLoginMethodApplyGroup}
)
