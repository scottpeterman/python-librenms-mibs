# SNMP MIB module (DLINKSW-AAA-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-AAA-ACCOUNTING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:34 2025
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
 DAaaPrivilegeLevel,
 DAaaSessionType,
 dAaaMIBObjects) = mibBuilder.importSymbols(
    "DLINKSW-AAA-COMMON-MIB",
    "DAaaMethodListName",
    "DAaaMethodName",
    "DAaaMethodPriority",
    "DAaaPrivilegeLevel",
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

dlinkSwAaaAccountingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3)
)
if mibBuilder.loadTexts:
    dlinkSwAaaAccountingMIB.setRevisions(
        ("2013-04-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DAaaAcctMIBNotifications_ObjectIdentity = ObjectIdentity
dAaaAcctMIBNotifications = _DAaaAcctMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 0)
)
_DAaaAcctMIBObjects_ObjectIdentity = ObjectIdentity
dAaaAcctMIBObjects = _DAaaAcctMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1)
)
_DAaaAcctGenericCfg_ObjectIdentity = ObjectIdentity
dAaaAcctGenericCfg = _DAaaAcctGenericCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 1)
)
_DAaaAcctGeneicAcctMethodTable_Object = MibTable
dAaaAcctGeneicAcctMethodTable = _DAaaAcctGeneicAcctMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dAaaAcctGeneicAcctMethodTable.setStatus("current")
_DAaaAcctGeneicAcctMethodEntry_Object = MibTableRow
dAaaAcctGeneicAcctMethodEntry = _DAaaAcctGeneicAcctMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 1, 1, 1)
)
dAaaAcctGeneicAcctMethodEntry.setIndexNames(
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctGenMethodLstType"),
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctGenMethodLstName"),
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctGenMethodPriority"),
)
if mibBuilder.loadTexts:
    dAaaAcctGeneicAcctMethodEntry.setStatus("current")


class _DAaaAcctGenMethodLstType_Type(Integer32):
    """Custom type dAaaAcctGenMethodLstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exec", 1),
          ("network", 2),
          ("system", 3))
    )


_DAaaAcctGenMethodLstType_Type.__name__ = "Integer32"
_DAaaAcctGenMethodLstType_Object = MibTableColumn
dAaaAcctGenMethodLstType = _DAaaAcctGenMethodLstType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 1, 1, 1, 1),
    _DAaaAcctGenMethodLstType_Type()
)
dAaaAcctGenMethodLstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctGenMethodLstType.setStatus("current")
_DAaaAcctGenMethodLstName_Type = DAaaMethodListName
_DAaaAcctGenMethodLstName_Object = MibTableColumn
dAaaAcctGenMethodLstName = _DAaaAcctGenMethodLstName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 1, 1, 1, 2),
    _DAaaAcctGenMethodLstName_Type()
)
dAaaAcctGenMethodLstName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctGenMethodLstName.setStatus("current")
_DAaaAcctGenMethodPriority_Type = DAaaMethodPriority
_DAaaAcctGenMethodPriority_Object = MibTableColumn
dAaaAcctGenMethodPriority = _DAaaAcctGenMethodPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 1, 1, 1, 3),
    _DAaaAcctGenMethodPriority_Type()
)
dAaaAcctGenMethodPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctGenMethodPriority.setStatus("current")
_DAaaAcctGenMethodName_Type = DAaaMethodName
_DAaaAcctGenMethodName_Object = MibTableColumn
dAaaAcctGenMethodName = _DAaaAcctGenMethodName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 1, 1, 1, 4),
    _DAaaAcctGenMethodName_Type()
)
dAaaAcctGenMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAcctGenMethodName.setStatus("current")
_DAaaAcctGenMethodRowStatus_Type = RowStatus
_DAaaAcctGenMethodRowStatus_Object = MibTableColumn
dAaaAcctGenMethodRowStatus = _DAaaAcctGenMethodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 1, 1, 1, 5),
    _DAaaAcctGenMethodRowStatus_Type()
)
dAaaAcctGenMethodRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAcctGenMethodRowStatus.setStatus("current")
_DAaaAcctCommandsAcct_ObjectIdentity = ObjectIdentity
dAaaAcctCommandsAcct = _DAaaAcctCommandsAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2)
)
_DAaaAcctCommandsAcctMethodTable_Object = MibTable
dAaaAcctCommandsAcctMethodTable = _DAaaAcctCommandsAcctMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctMethodTable.setStatus("current")
_DAaaAcctCommandsAcctMethodEntry_Object = MibTableRow
dAaaAcctCommandsAcctMethodEntry = _DAaaAcctCommandsAcctMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 1, 1)
)
dAaaAcctCommandsAcctMethodEntry.setIndexNames(
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctPrivLevel"),
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctListName"),
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctPriority"),
)
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctMethodEntry.setStatus("current")
_DAaaAcctCommandsAcctPrivLevel_Type = DAaaPrivilegeLevel
_DAaaAcctCommandsAcctPrivLevel_Object = MibTableColumn
dAaaAcctCommandsAcctPrivLevel = _DAaaAcctCommandsAcctPrivLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 1, 1, 1),
    _DAaaAcctCommandsAcctPrivLevel_Type()
)
dAaaAcctCommandsAcctPrivLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctPrivLevel.setStatus("current")
_DAaaAcctCommandsAcctListName_Type = DAaaMethodListName
_DAaaAcctCommandsAcctListName_Object = MibTableColumn
dAaaAcctCommandsAcctListName = _DAaaAcctCommandsAcctListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 1, 1, 2),
    _DAaaAcctCommandsAcctListName_Type()
)
dAaaAcctCommandsAcctListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctListName.setStatus("current")
_DAaaAcctCommandsAcctPriority_Type = DAaaMethodPriority
_DAaaAcctCommandsAcctPriority_Object = MibTableColumn
dAaaAcctCommandsAcctPriority = _DAaaAcctCommandsAcctPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 1, 1, 3),
    _DAaaAcctCommandsAcctPriority_Type()
)
dAaaAcctCommandsAcctPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctPriority.setStatus("current")
_DAaaAcctCommandsAcctMethodName_Type = DAaaMethodName
_DAaaAcctCommandsAcctMethodName_Object = MibTableColumn
dAaaAcctCommandsAcctMethodName = _DAaaAcctCommandsAcctMethodName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 1, 1, 4),
    _DAaaAcctCommandsAcctMethodName_Type()
)
dAaaAcctCommandsAcctMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctMethodName.setStatus("current")
_DAaaAcctCommandsAcctRowStatus_Type = RowStatus
_DAaaAcctCommandsAcctRowStatus_Object = MibTableColumn
dAaaAcctCommandsAcctRowStatus = _DAaaAcctCommandsAcctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 1, 1, 5),
    _DAaaAcctCommandsAcctRowStatus_Type()
)
dAaaAcctCommandsAcctRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctRowStatus.setStatus("current")
_DAaaAcctCommandsAcctApplyTable_Object = MibTable
dAaaAcctCommandsAcctApplyTable = _DAaaAcctCommandsAcctApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctApplyTable.setStatus("current")
_DAaaAcctCommandsAcctApplyEntry_Object = MibTableRow
dAaaAcctCommandsAcctApplyEntry = _DAaaAcctCommandsAcctApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 2, 1)
)
dAaaAcctCommandsAcctApplyEntry.setIndexNames(
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctApplySession"),
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctApplyPrivLevel"),
)
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctApplyEntry.setStatus("current")
_DAaaAcctCommandsAcctApplySession_Type = DAaaSessionType
_DAaaAcctCommandsAcctApplySession_Object = MibTableColumn
dAaaAcctCommandsAcctApplySession = _DAaaAcctCommandsAcctApplySession_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 2, 1, 1),
    _DAaaAcctCommandsAcctApplySession_Type()
)
dAaaAcctCommandsAcctApplySession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctApplySession.setStatus("current")
_DAaaAcctCommandsAcctApplyPrivLevel_Type = DAaaPrivilegeLevel
_DAaaAcctCommandsAcctApplyPrivLevel_Object = MibTableColumn
dAaaAcctCommandsAcctApplyPrivLevel = _DAaaAcctCommandsAcctApplyPrivLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 2, 1, 2),
    _DAaaAcctCommandsAcctApplyPrivLevel_Type()
)
dAaaAcctCommandsAcctApplyPrivLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctApplyPrivLevel.setStatus("current")
_DAaaAcctCommandsAcctApplyListName_Type = DAaaMethodListName
_DAaaAcctCommandsAcctApplyListName_Object = MibTableColumn
dAaaAcctCommandsAcctApplyListName = _DAaaAcctCommandsAcctApplyListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 2, 1, 3),
    _DAaaAcctCommandsAcctApplyListName_Type()
)
dAaaAcctCommandsAcctApplyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctApplyListName.setStatus("current")
_DAaaAcctCommandsAcctApplyRowStatus_Type = RowStatus
_DAaaAcctCommandsAcctApplyRowStatus_Object = MibTableColumn
dAaaAcctCommandsAcctApplyRowStatus = _DAaaAcctCommandsAcctApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 2, 2, 1, 4),
    _DAaaAcctCommandsAcctApplyRowStatus_Type()
)
dAaaAcctCommandsAcctApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAcctCommandsAcctApplyRowStatus.setStatus("current")
_DAaaAcctExecAcct_ObjectIdentity = ObjectIdentity
dAaaAcctExecAcct = _DAaaAcctExecAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 3)
)
_DAaaAcctExecAcctApplyTable_Object = MibTable
dAaaAcctExecAcctApplyTable = _DAaaAcctExecAcctApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dAaaAcctExecAcctApplyTable.setStatus("current")
_DAaaAcctExecAcctApplyEntry_Object = MibTableRow
dAaaAcctExecAcctApplyEntry = _DAaaAcctExecAcctApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 3, 1, 1)
)
dAaaAcctExecAcctApplyEntry.setIndexNames(
    (0, "DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctExecAcctApplySession"),
)
if mibBuilder.loadTexts:
    dAaaAcctExecAcctApplyEntry.setStatus("current")
_DAaaAcctExecAcctApplySession_Type = DAaaSessionType
_DAaaAcctExecAcctApplySession_Object = MibTableColumn
dAaaAcctExecAcctApplySession = _DAaaAcctExecAcctApplySession_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 3, 1, 1, 1),
    _DAaaAcctExecAcctApplySession_Type()
)
dAaaAcctExecAcctApplySession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAaaAcctExecAcctApplySession.setStatus("current")
_DAaaAcctExecAcctApplyListName_Type = DAaaMethodListName
_DAaaAcctExecAcctApplyListName_Object = MibTableColumn
dAaaAcctExecAcctApplyListName = _DAaaAcctExecAcctApplyListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 3, 1, 1, 2),
    _DAaaAcctExecAcctApplyListName_Type()
)
dAaaAcctExecAcctApplyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAcctExecAcctApplyListName.setStatus("current")
_DAaaAcctExecAcctApplyRowStatus_Type = RowStatus
_DAaaAcctExecAcctApplyRowStatus_Object = MibTableColumn
dAaaAcctExecAcctApplyRowStatus = _DAaaAcctExecAcctApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 1, 3, 1, 1, 3),
    _DAaaAcctExecAcctApplyRowStatus_Type()
)
dAaaAcctExecAcctApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAaaAcctExecAcctApplyRowStatus.setStatus("current")
_DAaaAcctMIBConformance_ObjectIdentity = ObjectIdentity
dAaaAcctMIBConformance = _DAaaAcctMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 2)
)
_DAaaAcctMIBCompliances_ObjectIdentity = ObjectIdentity
dAaaAcctMIBCompliances = _DAaaAcctMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 2, 1)
)
_DAaaAcctMIBGroups_ObjectIdentity = ObjectIdentity
dAaaAcctMIBGroups = _DAaaAcctMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 2, 2)
)

# Managed Objects groups

dAaaAcctAccountingCommandsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 2, 2, 1)
)
dAaaAcctAccountingCommandsGroup.setObjects(
      *(("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctMethodName"),
        ("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctRowStatus"),
        ("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctApplyListName"),
        ("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctCommandsAcctApplyRowStatus"))
)
if mibBuilder.loadTexts:
    dAaaAcctAccountingCommandsGroup.setStatus("current")

dAaaAcctGenericMethodLstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 2, 2, 2)
)
dAaaAcctGenericMethodLstGroup.setObjects(
      *(("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctGenMethodName"),
        ("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctGenMethodRowStatus"))
)
if mibBuilder.loadTexts:
    dAaaAcctGenericMethodLstGroup.setStatus("current")

dAaaAcctExecApplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 2, 2, 3)
)
dAaaAcctExecApplyGroup.setObjects(
      *(("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctExecAcctApplyListName"),
        ("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctExecAcctApplyRowStatus"))
)
if mibBuilder.loadTexts:
    dAaaAcctExecApplyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dAaaAcctMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 3, 2, 1, 1)
)
dAaaAcctMIBCompliance.setObjects(
      *(("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctGenericMethodLstGroup"),
        ("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctExecApplyGroup"),
        ("DLINKSW-AAA-ACCOUNTING-MIB", "dAaaAcctAccountingCommandsGroup"))
)
if mibBuilder.loadTexts:
    dAaaAcctMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-AAA-ACCOUNTING-MIB",
    **{"dlinkSwAaaAccountingMIB": dlinkSwAaaAccountingMIB,
       "dAaaAcctMIBNotifications": dAaaAcctMIBNotifications,
       "dAaaAcctMIBObjects": dAaaAcctMIBObjects,
       "dAaaAcctGenericCfg": dAaaAcctGenericCfg,
       "dAaaAcctGeneicAcctMethodTable": dAaaAcctGeneicAcctMethodTable,
       "dAaaAcctGeneicAcctMethodEntry": dAaaAcctGeneicAcctMethodEntry,
       "dAaaAcctGenMethodLstType": dAaaAcctGenMethodLstType,
       "dAaaAcctGenMethodLstName": dAaaAcctGenMethodLstName,
       "dAaaAcctGenMethodPriority": dAaaAcctGenMethodPriority,
       "dAaaAcctGenMethodName": dAaaAcctGenMethodName,
       "dAaaAcctGenMethodRowStatus": dAaaAcctGenMethodRowStatus,
       "dAaaAcctCommandsAcct": dAaaAcctCommandsAcct,
       "dAaaAcctCommandsAcctMethodTable": dAaaAcctCommandsAcctMethodTable,
       "dAaaAcctCommandsAcctMethodEntry": dAaaAcctCommandsAcctMethodEntry,
       "dAaaAcctCommandsAcctPrivLevel": dAaaAcctCommandsAcctPrivLevel,
       "dAaaAcctCommandsAcctListName": dAaaAcctCommandsAcctListName,
       "dAaaAcctCommandsAcctPriority": dAaaAcctCommandsAcctPriority,
       "dAaaAcctCommandsAcctMethodName": dAaaAcctCommandsAcctMethodName,
       "dAaaAcctCommandsAcctRowStatus": dAaaAcctCommandsAcctRowStatus,
       "dAaaAcctCommandsAcctApplyTable": dAaaAcctCommandsAcctApplyTable,
       "dAaaAcctCommandsAcctApplyEntry": dAaaAcctCommandsAcctApplyEntry,
       "dAaaAcctCommandsAcctApplySession": dAaaAcctCommandsAcctApplySession,
       "dAaaAcctCommandsAcctApplyPrivLevel": dAaaAcctCommandsAcctApplyPrivLevel,
       "dAaaAcctCommandsAcctApplyListName": dAaaAcctCommandsAcctApplyListName,
       "dAaaAcctCommandsAcctApplyRowStatus": dAaaAcctCommandsAcctApplyRowStatus,
       "dAaaAcctExecAcct": dAaaAcctExecAcct,
       "dAaaAcctExecAcctApplyTable": dAaaAcctExecAcctApplyTable,
       "dAaaAcctExecAcctApplyEntry": dAaaAcctExecAcctApplyEntry,
       "dAaaAcctExecAcctApplySession": dAaaAcctExecAcctApplySession,
       "dAaaAcctExecAcctApplyListName": dAaaAcctExecAcctApplyListName,
       "dAaaAcctExecAcctApplyRowStatus": dAaaAcctExecAcctApplyRowStatus,
       "dAaaAcctMIBConformance": dAaaAcctMIBConformance,
       "dAaaAcctMIBCompliances": dAaaAcctMIBCompliances,
       "dAaaAcctMIBCompliance": dAaaAcctMIBCompliance,
       "dAaaAcctMIBGroups": dAaaAcctMIBGroups,
       "dAaaAcctAccountingCommandsGroup": dAaaAcctAccountingCommandsGroup,
       "dAaaAcctGenericMethodLstGroup": dAaaAcctGenericMethodLstGroup,
       "dAaaAcctExecApplyGroup": dAaaAcctExecApplyGroup}
)
