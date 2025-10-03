# SNMP MIB module (COLUBRIS-USER-ACCOUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hpmsm\COLUBRIS-USER-ACCOUNT-MIB.my
# Produced by pysmi-1.6.2 at Thu Oct  2 11:52:16 2025
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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

colubrisUserAccountMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisUserAccountMIBObjects_ObjectIdentity = ObjectIdentity
colubrisUserAccountMIBObjects = _ColubrisUserAccountMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1)
)
_CoUserAccountStatusGroup_ObjectIdentity = ObjectIdentity
coUserAccountStatusGroup = _CoUserAccountStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1)
)
_CoUserAccountStatusTable_Object = MibTable
coUserAccountStatusTable = _CoUserAccountStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coUserAccountStatusTable.setStatus("current")
_CoUserAccountStatusEntry_Object = MibTableRow
coUserAccountStatusEntry = _CoUserAccountStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1)
)
coUserAccountStatusEntry.setIndexNames(
    (0, "COLUBRIS-USER-ACCOUNT-MIB", "coUserAccIndex"),
)
if mibBuilder.loadTexts:
    coUserAccountStatusEntry.setStatus("current")


class _CoUserAccIndex_Type(Integer32):
    """Custom type coUserAccIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoUserAccIndex_Type.__name__ = "Integer32"
_CoUserAccIndex_Object = MibTableColumn
coUserAccIndex = _CoUserAccIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 1),
    _CoUserAccIndex_Type()
)
coUserAccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coUserAccIndex.setStatus("current")
_CoUserAccUserName_Type = DisplayString
_CoUserAccUserName_Object = MibTableColumn
coUserAccUserName = _CoUserAccUserName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 2),
    _CoUserAccUserName_Type()
)
coUserAccUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccUserName.setStatus("current")
_CoUserAccPlanName_Type = DisplayString
_CoUserAccPlanName_Object = MibTableColumn
coUserAccPlanName = _CoUserAccPlanName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 3),
    _CoUserAccPlanName_Type()
)
coUserAccPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccPlanName.setStatus("current")
_CoUserAccRemainingOnlineTime_Type = Integer32
_CoUserAccRemainingOnlineTime_Object = MibTableColumn
coUserAccRemainingOnlineTime = _CoUserAccRemainingOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 4),
    _CoUserAccRemainingOnlineTime_Type()
)
coUserAccRemainingOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccRemainingOnlineTime.setStatus("current")
if mibBuilder.loadTexts:
    coUserAccRemainingOnlineTime.setUnits("seconds")
_CoUserAccFirstLoginTime_Type = DisplayString
_CoUserAccFirstLoginTime_Object = MibTableColumn
coUserAccFirstLoginTime = _CoUserAccFirstLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 5),
    _CoUserAccFirstLoginTime_Type()
)
coUserAccFirstLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccFirstLoginTime.setStatus("current")
_CoUserAccRemainingSessionTime_Type = Integer32
_CoUserAccRemainingSessionTime_Object = MibTableColumn
coUserAccRemainingSessionTime = _CoUserAccRemainingSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 6),
    _CoUserAccRemainingSessionTime_Type()
)
coUserAccRemainingSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccRemainingSessionTime.setStatus("current")
if mibBuilder.loadTexts:
    coUserAccRemainingSessionTime.setUnits("seconds")


class _CoUserAccStatus_Type(Integer32):
    """Custom type coUserAccStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_CoUserAccStatus_Type.__name__ = "Integer32"
_CoUserAccStatus_Object = MibTableColumn
coUserAccStatus = _CoUserAccStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 7),
    _CoUserAccStatus_Type()
)
coUserAccStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccStatus.setStatus("current")
_CoUserAccExpirationTime_Type = DisplayString
_CoUserAccExpirationTime_Object = MibTableColumn
coUserAccExpirationTime = _CoUserAccExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 8),
    _CoUserAccExpirationTime_Type()
)
coUserAccExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUserAccExpirationTime.setStatus("current")
_ColubrisUserAccountMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisUserAccountMIBNotificationPrefix = _ColubrisUserAccountMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 2)
)
_ColubrisUserAccountMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisUserAccountMIBNotifications = _ColubrisUserAccountMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 2, 0)
)
_ColubrisUserAccountMIBConformance_ObjectIdentity = ObjectIdentity
colubrisUserAccountMIBConformance = _ColubrisUserAccountMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 3)
)
_ColubrisUserAccountMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisUserAccountMIBCompliances = _ColubrisUserAccountMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 1)
)
_ColubrisUserAccountMIBGroups_ObjectIdentity = ObjectIdentity
colubrisUserAccountMIBGroups = _ColubrisUserAccountMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 2)
)

# Managed Objects groups

colubrisUserAccountStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 2, 1)
)
colubrisUserAccountStatusMIBGroup.setObjects(
      *(("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccUserName"),
        ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccPlanName"),
        ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccRemainingOnlineTime"),
        ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccFirstLoginTime"),
        ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccRemainingSessionTime"),
        ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccStatus"),
        ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccExpirationTime"))
)
if mibBuilder.loadTexts:
    colubrisUserAccountStatusMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisUserAccountMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 1, 1)
)
colubrisUserAccountMIBCompliance.setObjects(
    ("COLUBRIS-USER-ACCOUNT-MIB", "colubrisUserAccountStatusMIBGroup")
)
if mibBuilder.loadTexts:
    colubrisUserAccountMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-USER-ACCOUNT-MIB",
    **{"colubrisUserAccountMIB": colubrisUserAccountMIB,
       "colubrisUserAccountMIBObjects": colubrisUserAccountMIBObjects,
       "coUserAccountStatusGroup": coUserAccountStatusGroup,
       "coUserAccountStatusTable": coUserAccountStatusTable,
       "coUserAccountStatusEntry": coUserAccountStatusEntry,
       "coUserAccIndex": coUserAccIndex,
       "coUserAccUserName": coUserAccUserName,
       "coUserAccPlanName": coUserAccPlanName,
       "coUserAccRemainingOnlineTime": coUserAccRemainingOnlineTime,
       "coUserAccFirstLoginTime": coUserAccFirstLoginTime,
       "coUserAccRemainingSessionTime": coUserAccRemainingSessionTime,
       "coUserAccStatus": coUserAccStatus,
       "coUserAccExpirationTime": coUserAccExpirationTime,
       "colubrisUserAccountMIBNotificationPrefix": colubrisUserAccountMIBNotificationPrefix,
       "colubrisUserAccountMIBNotifications": colubrisUserAccountMIBNotifications,
       "colubrisUserAccountMIBConformance": colubrisUserAccountMIBConformance,
       "colubrisUserAccountMIBCompliances": colubrisUserAccountMIBCompliances,
       "colubrisUserAccountMIBCompliance": colubrisUserAccountMIBCompliance,
       "colubrisUserAccountMIBGroups": colubrisUserAccountMIBGroups,
       "colubrisUserAccountStatusMIBGroup": colubrisUserAccountStatusMIBGroup}
)
