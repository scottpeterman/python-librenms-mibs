# SNMP MIB module (TN-DEV-SYS-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-SYS-USER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:08 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY

tnDevSysUser = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19)
)
if mibBuilder.loadTexts:
    tnDevSysUser.setRevisions(
        ("2014-06-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevSysUserTable_Object = MibTable
tnDevSysUserTable = _TnDevSysUserTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    tnDevSysUserTable.setStatus("current")
_TnDevSysUserEntry_Object = MibTableRow
tnDevSysUserEntry = _TnDevSysUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 1, 1)
)
tnDevSysUserEntry.setIndexNames(
    (0, "TN-DEV-SYS-USER-MIB", "tnDevSysUserIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysUserEntry.setStatus("current")


class _TnDevSysUserIndex_Type(Integer32):
    """Custom type tnDevSysUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnDevSysUserIndex_Type.__name__ = "Integer32"
_TnDevSysUserIndex_Object = MibTableColumn
tnDevSysUserIndex = _TnDevSysUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 1, 1, 1),
    _TnDevSysUserIndex_Type()
)
tnDevSysUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevSysUserIndex.setStatus("current")


class _TnDevSysUserName_Type(DisplayString):
    """Custom type tnDevSysUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnDevSysUserName_Type.__name__ = "DisplayString"
_TnDevSysUserName_Object = MibTableColumn
tnDevSysUserName = _TnDevSysUserName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 1, 1, 2),
    _TnDevSysUserName_Type()
)
tnDevSysUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevSysUserName.setStatus("current")


class _TnDevSysUserPassword_Type(DisplayString):
    """Custom type tnDevSysUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDevSysUserPassword_Type.__name__ = "DisplayString"
_TnDevSysUserPassword_Object = MibTableColumn
tnDevSysUserPassword = _TnDevSysUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 1, 1, 3),
    _TnDevSysUserPassword_Type()
)
tnDevSysUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevSysUserPassword.setStatus("current")


class _TnDevSysUserLevel_Type(Integer32):
    """Custom type tnDevSysUserLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TnDevSysUserLevel_Type.__name__ = "Integer32"
_TnDevSysUserLevel_Object = MibTableColumn
tnDevSysUserLevel = _TnDevSysUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 1, 1, 4),
    _TnDevSysUserLevel_Type()
)
tnDevSysUserLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevSysUserLevel.setStatus("current")
_TnDevSysUserStatus_Type = RowStatus
_TnDevSysUserStatus_Object = MibTableColumn
tnDevSysUserStatus = _TnDevSysUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 1, 1, 20),
    _TnDevSysUserStatus_Type()
)
tnDevSysUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevSysUserStatus.setStatus("current")
_TnDevSysMethodTable_Object = MibTable
tnDevSysMethodTable = _TnDevSysMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    tnDevSysMethodTable.setStatus("current")
_TnDevSysMethodEntry_Object = MibTableRow
tnDevSysMethodEntry = _TnDevSysMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 3, 1)
)
tnDevSysMethodEntry.setIndexNames(
    (0, "TN-DEV-SYS-USER-MIB", "tnDevSysClientIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysMethodEntry.setStatus("current")


class _TnDevSysClientIndex_Type(Integer32):
    """Custom type tnDevSysClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnDevSysClientIndex_Type.__name__ = "Integer32"
_TnDevSysClientIndex_Object = MibTableColumn
tnDevSysClientIndex = _TnDevSysClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 3, 1, 1),
    _TnDevSysClientIndex_Type()
)
tnDevSysClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevSysClientIndex.setStatus("current")


class _TnDevSysMethodName_Type(DisplayString):
    """Custom type tnDevSysMethodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TnDevSysMethodName_Type.__name__ = "DisplayString"
_TnDevSysMethodName_Object = MibTableColumn
tnDevSysMethodName = _TnDevSysMethodName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 3, 1, 2),
    _TnDevSysMethodName_Type()
)
tnDevSysMethodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysMethodName.setStatus("current")


class _TnDevSysLoginMethod_Type(Integer32):
    """Custom type tnDevSysLoginMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("localLogin", 1),
          ("radius", 2),
          ("radiusLocal", 3),
          ("tacplus", 4),
          ("tacplusLocal", 5))
    )


_TnDevSysLoginMethod_Type.__name__ = "Integer32"
_TnDevSysLoginMethod_Object = MibTableColumn
tnDevSysLoginMethod = _TnDevSysLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 3, 1, 3),
    _TnDevSysLoginMethod_Type()
)
tnDevSysLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysLoginMethod.setStatus("current")


class _TnDevSysLoginMethod1_Type(Integer32):
    """Custom type tnDevSysLoginMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("localLogin", 1),
          ("radius", 2),
          ("radiusLocal", 3),
          ("tacplus", 4),
          ("tacplusLocal", 5))
    )


_TnDevSysLoginMethod1_Type.__name__ = "Integer32"
_TnDevSysLoginMethod1_Object = MibTableColumn
tnDevSysLoginMethod1 = _TnDevSysLoginMethod1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 3, 1, 4),
    _TnDevSysLoginMethod1_Type()
)
tnDevSysLoginMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysLoginMethod1.setStatus("current")


class _TnDevSysLoginMethod2_Type(Integer32):
    """Custom type tnDevSysLoginMethod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("localLogin", 1),
          ("radius", 2),
          ("radiusLocal", 3),
          ("tacplus", 4),
          ("tacplusLocal", 5))
    )


_TnDevSysLoginMethod2_Type.__name__ = "Integer32"
_TnDevSysLoginMethod2_Object = MibTableColumn
tnDevSysLoginMethod2 = _TnDevSysLoginMethod2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 3, 1, 5),
    _TnDevSysLoginMethod2_Type()
)
tnDevSysLoginMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysLoginMethod2.setStatus("current")
_TnDevSysPrivilegeLevelTable_Object = MibTable
tnDevSysPrivilegeLevelTable = _TnDevSysPrivilegeLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 4)
)
if mibBuilder.loadTexts:
    tnDevSysPrivilegeLevelTable.setStatus("current")
_TnDevSysPrivilegeLevelEntry_Object = MibTableRow
tnDevSysPrivilegeLevelEntry = _TnDevSysPrivilegeLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 4, 1)
)
tnDevSysPrivilegeLevelEntry.setIndexNames(
    (0, "TN-DEV-SYS-USER-MIB", "tnDevSysPrivilegeLevelIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysPrivilegeLevelEntry.setStatus("current")


class _TnDevSysPrivilegeLevelIndex_Type(Integer32):
    """Custom type tnDevSysPrivilegeLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnDevSysPrivilegeLevelIndex_Type.__name__ = "Integer32"
_TnDevSysPrivilegeLevelIndex_Object = MibTableColumn
tnDevSysPrivilegeLevelIndex = _TnDevSysPrivilegeLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 4, 1, 1),
    _TnDevSysPrivilegeLevelIndex_Type()
)
tnDevSysPrivilegeLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevSysPrivilegeLevelIndex.setStatus("current")


class _TnDevSysPrivilegeLevelName_Type(DisplayString):
    """Custom type tnDevSysPrivilegeLevelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TnDevSysPrivilegeLevelName_Type.__name__ = "DisplayString"
_TnDevSysPrivilegeLevelName_Object = MibTableColumn
tnDevSysPrivilegeLevelName = _TnDevSysPrivilegeLevelName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 4, 1, 2),
    _TnDevSysPrivilegeLevelName_Type()
)
tnDevSysPrivilegeLevelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysPrivilegeLevelName.setStatus("current")


class _TnDevSysConfigReadLevel_Type(Integer32):
    """Custom type tnDevSysConfigReadLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TnDevSysConfigReadLevel_Type.__name__ = "Integer32"
_TnDevSysConfigReadLevel_Object = MibTableColumn
tnDevSysConfigReadLevel = _TnDevSysConfigReadLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 4, 1, 3),
    _TnDevSysConfigReadLevel_Type()
)
tnDevSysConfigReadLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysConfigReadLevel.setStatus("current")


class _TnDevSysConfigWriteLevel_Type(Integer32):
    """Custom type tnDevSysConfigWriteLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TnDevSysConfigWriteLevel_Type.__name__ = "Integer32"
_TnDevSysConfigWriteLevel_Object = MibTableColumn
tnDevSysConfigWriteLevel = _TnDevSysConfigWriteLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 4, 1, 4),
    _TnDevSysConfigWriteLevel_Type()
)
tnDevSysConfigWriteLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysConfigWriteLevel.setStatus("current")


class _TnDevSysStatusReadLevel_Type(Integer32):
    """Custom type tnDevSysStatusReadLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TnDevSysStatusReadLevel_Type.__name__ = "Integer32"
_TnDevSysStatusReadLevel_Object = MibTableColumn
tnDevSysStatusReadLevel = _TnDevSysStatusReadLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 4, 1, 5),
    _TnDevSysStatusReadLevel_Type()
)
tnDevSysStatusReadLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysStatusReadLevel.setStatus("current")


class _TnDevSysStatusWriteLevel_Type(Integer32):
    """Custom type tnDevSysStatusWriteLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TnDevSysStatusWriteLevel_Type.__name__ = "Integer32"
_TnDevSysStatusWriteLevel_Object = MibTableColumn
tnDevSysStatusWriteLevel = _TnDevSysStatusWriteLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 19, 4, 1, 6),
    _TnDevSysStatusWriteLevel_Type()
)
tnDevSysStatusWriteLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysStatusWriteLevel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-SYS-USER-MIB",
    **{"tnDevSysUser": tnDevSysUser,
       "tnDevSysUserTable": tnDevSysUserTable,
       "tnDevSysUserEntry": tnDevSysUserEntry,
       "tnDevSysUserIndex": tnDevSysUserIndex,
       "tnDevSysUserName": tnDevSysUserName,
       "tnDevSysUserPassword": tnDevSysUserPassword,
       "tnDevSysUserLevel": tnDevSysUserLevel,
       "tnDevSysUserStatus": tnDevSysUserStatus,
       "tnDevSysMethodTable": tnDevSysMethodTable,
       "tnDevSysMethodEntry": tnDevSysMethodEntry,
       "tnDevSysClientIndex": tnDevSysClientIndex,
       "tnDevSysMethodName": tnDevSysMethodName,
       "tnDevSysLoginMethod": tnDevSysLoginMethod,
       "tnDevSysLoginMethod1": tnDevSysLoginMethod1,
       "tnDevSysLoginMethod2": tnDevSysLoginMethod2,
       "tnDevSysPrivilegeLevelTable": tnDevSysPrivilegeLevelTable,
       "tnDevSysPrivilegeLevelEntry": tnDevSysPrivilegeLevelEntry,
       "tnDevSysPrivilegeLevelIndex": tnDevSysPrivilegeLevelIndex,
       "tnDevSysPrivilegeLevelName": tnDevSysPrivilegeLevelName,
       "tnDevSysConfigReadLevel": tnDevSysConfigReadLevel,
       "tnDevSysConfigWriteLevel": tnDevSysConfigWriteLevel,
       "tnDevSysStatusReadLevel": tnDevSysStatusReadLevel,
       "tnDevSysStatusWriteLevel": tnDevSysStatusWriteLevel}
)
