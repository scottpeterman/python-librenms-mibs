# SNMP MIB module (UBQS-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-SNMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:32 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpVersion(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("v1", 1),
          ("v2", 2),
          ("v3", 3),
          ("inform", 4))
    )



# MIB Managed Objects in the order of their OIDs

_UbiSnmpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiSnmpMIBNotificationPrefix = _UbiSnmpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 0)
)
_UbiSnmpMIBObjects_ObjectIdentity = ObjectIdentity
ubiSnmpMIBObjects = _UbiSnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1)
)
_UbiSnmpCommunityTable_Object = MibTable
ubiSnmpCommunityTable = _UbiSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 1)
)
if mibBuilder.loadTexts:
    ubiSnmpCommunityTable.setStatus("current")
_UbiSnmpCommunityEntry_Object = MibTableRow
ubiSnmpCommunityEntry = _UbiSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 1, 1)
)
ubiSnmpCommunityEntry.setIndexNames(
    (0, "UBQS-SNMP-MIB", "ubiSnmpCommunity"),
)
if mibBuilder.loadTexts:
    ubiSnmpCommunityEntry.setStatus("current")
_UbiSnmpCommunity_Type = DisplayString
_UbiSnmpCommunity_Object = MibTableColumn
ubiSnmpCommunity = _UbiSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 1, 1, 1),
    _UbiSnmpCommunity_Type()
)
ubiSnmpCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpCommunity.setStatus("current")


class _UbiSnmpCommunityType_Type(Integer32):
    """Custom type ubiSnmpCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_UbiSnmpCommunityType_Type.__name__ = "Integer32"
_UbiSnmpCommunityType_Object = MibTableColumn
ubiSnmpCommunityType = _UbiSnmpCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 1, 1, 2),
    _UbiSnmpCommunityType_Type()
)
ubiSnmpCommunityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpCommunityType.setStatus("current")
_UbiSnmpCommunityAclName_Type = DisplayString
_UbiSnmpCommunityAclName_Object = MibTableColumn
ubiSnmpCommunityAclName = _UbiSnmpCommunityAclName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 1, 1, 3),
    _UbiSnmpCommunityAclName_Type()
)
ubiSnmpCommunityAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpCommunityAclName.setStatus("current")
_UbiSnmpCommunityView_Type = DisplayString
_UbiSnmpCommunityView_Object = MibTableColumn
ubiSnmpCommunityView = _UbiSnmpCommunityView_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 1, 1, 4),
    _UbiSnmpCommunityView_Type()
)
ubiSnmpCommunityView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpCommunityView.setStatus("current")
_UbiSnmpCommunityRowStatus_Type = RowStatus
_UbiSnmpCommunityRowStatus_Object = MibTableColumn
ubiSnmpCommunityRowStatus = _UbiSnmpCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 1, 1, 5),
    _UbiSnmpCommunityRowStatus_Type()
)
ubiSnmpCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiSnmpCommunityRowStatus.setStatus("current")
_UbiSnmpUserTable_Object = MibTable
ubiSnmpUserTable = _UbiSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2)
)
if mibBuilder.loadTexts:
    ubiSnmpUserTable.setStatus("current")
_UbiSnmpUserEntry_Object = MibTableRow
ubiSnmpUserEntry = _UbiSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1)
)
ubiSnmpUserEntry.setIndexNames(
    (0, "UBQS-SNMP-MIB", "ubiSnmpUserVersion"),
    (0, "UBQS-SNMP-MIB", "ubiSnmpUserName"),
)
if mibBuilder.loadTexts:
    ubiSnmpUserEntry.setStatus("current")
_UbiSnmpUserVersion_Type = SnmpVersion
_UbiSnmpUserVersion_Object = MibTableColumn
ubiSnmpUserVersion = _UbiSnmpUserVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 1),
    _UbiSnmpUserVersion_Type()
)
ubiSnmpUserVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpUserVersion.setStatus("current")
_UbiSnmpUserName_Type = DisplayString
_UbiSnmpUserName_Object = MibTableColumn
ubiSnmpUserName = _UbiSnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 2),
    _UbiSnmpUserName_Type()
)
ubiSnmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpUserName.setStatus("current")
_UbiSnmpUserGroup_Type = DisplayString
_UbiSnmpUserGroup_Object = MibTableColumn
ubiSnmpUserGroup = _UbiSnmpUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 3),
    _UbiSnmpUserGroup_Type()
)
ubiSnmpUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpUserGroup.setStatus("current")


class _UbiSnmpUserAuthType_Type(Integer32):
    """Custom type ubiSnmpUserAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 1),
          ("sha", 2))
    )


_UbiSnmpUserAuthType_Type.__name__ = "Integer32"
_UbiSnmpUserAuthType_Object = MibTableColumn
ubiSnmpUserAuthType = _UbiSnmpUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 4),
    _UbiSnmpUserAuthType_Type()
)
ubiSnmpUserAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpUserAuthType.setStatus("current")
_UbiSnmpUserAuthPasswd_Type = DisplayString
_UbiSnmpUserAuthPasswd_Object = MibTableColumn
ubiSnmpUserAuthPasswd = _UbiSnmpUserAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 5),
    _UbiSnmpUserAuthPasswd_Type()
)
ubiSnmpUserAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpUserAuthPasswd.setStatus("current")


class _UbiSnmpUserPrivacyType_Type(Integer32):
    """Custom type ubiSnmpUserPrivacyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("aes", 1),
          ("des", 2))
    )


_UbiSnmpUserPrivacyType_Type.__name__ = "Integer32"
_UbiSnmpUserPrivacyType_Object = MibTableColumn
ubiSnmpUserPrivacyType = _UbiSnmpUserPrivacyType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 6),
    _UbiSnmpUserPrivacyType_Type()
)
ubiSnmpUserPrivacyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpUserPrivacyType.setStatus("current")
_UbiSnmpUserPrivacyPasswd_Type = DisplayString
_UbiSnmpUserPrivacyPasswd_Object = MibTableColumn
ubiSnmpUserPrivacyPasswd = _UbiSnmpUserPrivacyPasswd_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 7),
    _UbiSnmpUserPrivacyPasswd_Type()
)
ubiSnmpUserPrivacyPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpUserPrivacyPasswd.setStatus("current")
_UbiSnmpUserAclName_Type = DisplayString
_UbiSnmpUserAclName_Object = MibTableColumn
ubiSnmpUserAclName = _UbiSnmpUserAclName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 8),
    _UbiSnmpUserAclName_Type()
)
ubiSnmpUserAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpUserAclName.setStatus("current")
_UbiSnmpUserRowStatus_Type = RowStatus
_UbiSnmpUserRowStatus_Object = MibTableColumn
ubiSnmpUserRowStatus = _UbiSnmpUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 2, 1, 9),
    _UbiSnmpUserRowStatus_Type()
)
ubiSnmpUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiSnmpUserRowStatus.setStatus("current")
_UbiSnmpGroupTable_Object = MibTable
ubiSnmpGroupTable = _UbiSnmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3)
)
if mibBuilder.loadTexts:
    ubiSnmpGroupTable.setStatus("current")
_UbiSnmpGroupEntry_Object = MibTableRow
ubiSnmpGroupEntry = _UbiSnmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3, 1)
)
ubiSnmpGroupEntry.setIndexNames(
    (0, "UBQS-SNMP-MIB", "ubiSnmpGroupVersion"),
    (0, "UBQS-SNMP-MIB", "ubiSnmpGroupName"),
)
if mibBuilder.loadTexts:
    ubiSnmpGroupEntry.setStatus("current")
_UbiSnmpGroupVersion_Type = SnmpVersion
_UbiSnmpGroupVersion_Object = MibTableColumn
ubiSnmpGroupVersion = _UbiSnmpGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3, 1, 1),
    _UbiSnmpGroupVersion_Type()
)
ubiSnmpGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpGroupVersion.setStatus("current")
_UbiSnmpGroupName_Type = DisplayString
_UbiSnmpGroupName_Object = MibTableColumn
ubiSnmpGroupName = _UbiSnmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3, 1, 2),
    _UbiSnmpGroupName_Type()
)
ubiSnmpGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpGroupName.setStatus("current")


class _UbiSnmpGroupSecLevel_Type(Integer32):
    """Custom type ubiSnmpGroupSecLevel based on Integer32"""
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
        *(("none", 0),
          ("noAuthen", 1),
          ("authen", 2),
          ("privacy", 3))
    )


_UbiSnmpGroupSecLevel_Type.__name__ = "Integer32"
_UbiSnmpGroupSecLevel_Object = MibTableColumn
ubiSnmpGroupSecLevel = _UbiSnmpGroupSecLevel_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3, 1, 3),
    _UbiSnmpGroupSecLevel_Type()
)
ubiSnmpGroupSecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpGroupSecLevel.setStatus("current")
_UbiSnmpGroupReadView_Type = DisplayString
_UbiSnmpGroupReadView_Object = MibTableColumn
ubiSnmpGroupReadView = _UbiSnmpGroupReadView_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3, 1, 4),
    _UbiSnmpGroupReadView_Type()
)
ubiSnmpGroupReadView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpGroupReadView.setStatus("current")
_UbiSnmpGroupWriteView_Type = DisplayString
_UbiSnmpGroupWriteView_Object = MibTableColumn
ubiSnmpGroupWriteView = _UbiSnmpGroupWriteView_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3, 1, 5),
    _UbiSnmpGroupWriteView_Type()
)
ubiSnmpGroupWriteView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpGroupWriteView.setStatus("current")
_UbiSnmpGroupNotifyView_Type = DisplayString
_UbiSnmpGroupNotifyView_Object = MibTableColumn
ubiSnmpGroupNotifyView = _UbiSnmpGroupNotifyView_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3, 1, 6),
    _UbiSnmpGroupNotifyView_Type()
)
ubiSnmpGroupNotifyView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpGroupNotifyView.setStatus("current")
_UbiSnmpGroupRowStatus_Type = RowStatus
_UbiSnmpGroupRowStatus_Object = MibTableColumn
ubiSnmpGroupRowStatus = _UbiSnmpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 3, 1, 7),
    _UbiSnmpGroupRowStatus_Type()
)
ubiSnmpGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiSnmpGroupRowStatus.setStatus("current")
_UbiSnmpViewTable_Object = MibTable
ubiSnmpViewTable = _UbiSnmpViewTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 4)
)
if mibBuilder.loadTexts:
    ubiSnmpViewTable.setStatus("current")
_UbiSnmpViewEntry_Object = MibTableRow
ubiSnmpViewEntry = _UbiSnmpViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 4, 1)
)
ubiSnmpViewEntry.setIndexNames(
    (0, "UBQS-SNMP-MIB", "ubiSnmpViewName"),
    (0, "UBQS-SNMP-MIB", "ubiSnmpViewVariable"),
)
if mibBuilder.loadTexts:
    ubiSnmpViewEntry.setStatus("current")
_UbiSnmpViewName_Type = DisplayString
_UbiSnmpViewName_Object = MibTableColumn
ubiSnmpViewName = _UbiSnmpViewName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 4, 1, 1),
    _UbiSnmpViewName_Type()
)
ubiSnmpViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpViewName.setStatus("current")
_UbiSnmpViewVariable_Type = DisplayString
_UbiSnmpViewVariable_Object = MibTableColumn
ubiSnmpViewVariable = _UbiSnmpViewVariable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 4, 1, 2),
    _UbiSnmpViewVariable_Type()
)
ubiSnmpViewVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpViewVariable.setStatus("current")


class _UbiSnmpViewType_Type(Integer32):
    """Custom type ubiSnmpViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("excluded", 1),
          ("included", 2))
    )


_UbiSnmpViewType_Type.__name__ = "Integer32"
_UbiSnmpViewType_Object = MibTableColumn
ubiSnmpViewType = _UbiSnmpViewType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 4, 1, 3),
    _UbiSnmpViewType_Type()
)
ubiSnmpViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpViewType.setStatus("current")
_UbiSnmpViewRowStatus_Type = RowStatus
_UbiSnmpViewRowStatus_Object = MibTableColumn
ubiSnmpViewRowStatus = _UbiSnmpViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 4, 1, 4),
    _UbiSnmpViewRowStatus_Type()
)
ubiSnmpViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiSnmpViewRowStatus.setStatus("current")
_UbiSnmpTrapHostTable_Object = MibTable
ubiSnmpTrapHostTable = _UbiSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5)
)
if mibBuilder.loadTexts:
    ubiSnmpTrapHostTable.setStatus("current")
_UbiSnmpTrapHostEntry_Object = MibTableRow
ubiSnmpTrapHostEntry = _UbiSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1)
)
ubiSnmpTrapHostEntry.setIndexNames(
    (0, "UBQS-SNMP-MIB", "ubiSnmpTrapHostType"),
    (0, "UBQS-SNMP-MIB", "UbiSnmpTrapHostVersion"),
    (0, "UBQS-SNMP-MIB", "UbiSnmpTrapHostAddrType"),
    (0, "UBQS-SNMP-MIB", "UbiSnmpTrapHostAddress"),
    (0, "UBQS-SNMP-MIB", "ubiSnmpTrapHostCommunity"),
)
if mibBuilder.loadTexts:
    ubiSnmpTrapHostEntry.setStatus("current")


class _UbiSnmpTrapHostType_Type(Integer32):
    """Custom type ubiSnmpTrapHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trap", 1),
          ("inform", 2))
    )


_UbiSnmpTrapHostType_Type.__name__ = "Integer32"
_UbiSnmpTrapHostType_Object = MibTableColumn
ubiSnmpTrapHostType = _UbiSnmpTrapHostType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1, 1),
    _UbiSnmpTrapHostType_Type()
)
ubiSnmpTrapHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpTrapHostType.setStatus("current")
_UbiSnmpTrapHostVersion_Type = SnmpVersion
_UbiSnmpTrapHostVersion_Object = MibTableColumn
ubiSnmpTrapHostVersion = _UbiSnmpTrapHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1, 2),
    _UbiSnmpTrapHostVersion_Type()
)
ubiSnmpTrapHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpTrapHostVersion.setStatus("current")
_UbiSnmpTrapHostAddrType_Type = InetAddressType
_UbiSnmpTrapHostAddrType_Object = MibTableColumn
ubiSnmpTrapHostAddrType = _UbiSnmpTrapHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1, 3),
    _UbiSnmpTrapHostAddrType_Type()
)
ubiSnmpTrapHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpTrapHostAddrType.setStatus("current")
_UbiSnmpTrapHostAddress_Type = InetAddress
_UbiSnmpTrapHostAddress_Object = MibTableColumn
ubiSnmpTrapHostAddress = _UbiSnmpTrapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1, 4),
    _UbiSnmpTrapHostAddress_Type()
)
ubiSnmpTrapHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpTrapHostAddress.setStatus("current")
_UbiSnmpTrapHostCommunity_Type = DisplayString
_UbiSnmpTrapHostCommunity_Object = MibTableColumn
ubiSnmpTrapHostCommunity = _UbiSnmpTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1, 5),
    _UbiSnmpTrapHostCommunity_Type()
)
ubiSnmpTrapHostCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSnmpTrapHostCommunity.setStatus("current")


class _UbiSnmpTrapHostSecLevel_Type(Integer32):
    """Custom type ubiSnmpTrapHostSecLevel based on Integer32"""
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
        *(("none", 0),
          ("noAuthen", 1),
          ("authen", 2),
          ("privacy", 3))
    )


_UbiSnmpTrapHostSecLevel_Type.__name__ = "Integer32"
_UbiSnmpTrapHostSecLevel_Object = MibTableColumn
ubiSnmpTrapHostSecLevel = _UbiSnmpTrapHostSecLevel_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1, 6),
    _UbiSnmpTrapHostSecLevel_Type()
)
ubiSnmpTrapHostSecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpTrapHostSecLevel.setStatus("current")


class _UbiSnmpTrapHostPort_Type(Integer32):
    """Custom type ubiSnmpTrapHostPort based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UbiSnmpTrapHostPort_Type.__name__ = "Integer32"
_UbiSnmpTrapHostPort_Object = MibTableColumn
ubiSnmpTrapHostPort = _UbiSnmpTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1, 7),
    _UbiSnmpTrapHostPort_Type()
)
ubiSnmpTrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSnmpTrapHostPort.setStatus("current")
_UbiSnmpTrapHostRowStatus_Type = RowStatus
_UbiSnmpTrapHostRowStatus_Object = MibTableColumn
ubiSnmpTrapHostRowStatus = _UbiSnmpTrapHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 1, 5, 1, 8),
    _UbiSnmpTrapHostRowStatus_Type()
)
ubiSnmpTrapHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ubiSnmpTrapHostRowStatus.setStatus("current")
_UbiSnmpMIBConformance_ObjectIdentity = ObjectIdentity
ubiSnmpMIBConformance = _UbiSnmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 2)
)
_UbiSnmpMIBCompliances_ObjectIdentity = ObjectIdentity
ubiSnmpMIBCompliances = _UbiSnmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 2, 1)
)
_UbiSnmpMIBGroups_ObjectIdentity = ObjectIdentity
ubiSnmpMIBGroups = _UbiSnmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 2, 2)
)

# Managed Objects groups

ubiSnmpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 2, 2, 1)
)
ubiSnmpConfigGroup.setObjects(
      *(("UBQS-SNMP-MIB", "ubiSnmpCommunity"),
        ("UBQS-SNMP-MIB", "ubiSnmpCommunityType"),
        ("UBQS-SNMP-MIB", "ubiSnmpCommunityRowStatus"),
        ("UBQS-SNMP-MIB", "ubiSnmpTrapHostVersion"),
        ("UBQS-SNMP-MIB", "ubiSnmpTrapHostAddrType"),
        ("UBQS-SNMP-MIB", "ubiSnmpTrapHostAddress"),
        ("UBQS-SNMP-MIB", "ubiSnmpTrapHostCommunity"),
        ("UBQS-SNMP-MIB", "ubiSnmpTrapHostRowStatus"))
)
if mibBuilder.loadTexts:
    ubiSnmpConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubiSnmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 19, 2, 1, 1)
)
ubiSnmpMIBCompliance.setObjects(
      *(("UBQS-SNMP-MIB", "ubiSnmpConfigGroup"),
        ("UBQS-SNMP-MIB", "ubiSnmpConfigGroup"))
)
if mibBuilder.loadTexts:
    ubiSnmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-SNMP-MIB",
    **{"SnmpVersion": SnmpVersion,
       "ubiSnmpMIB": ubiSnmpMIB,
       "ubiSnmpMIBNotificationPrefix": ubiSnmpMIBNotificationPrefix,
       "ubiSnmpMIBObjects": ubiSnmpMIBObjects,
       "ubiSnmpCommunityTable": ubiSnmpCommunityTable,
       "ubiSnmpCommunityEntry": ubiSnmpCommunityEntry,
       "ubiSnmpCommunity": ubiSnmpCommunity,
       "ubiSnmpCommunityType": ubiSnmpCommunityType,
       "ubiSnmpCommunityAclName": ubiSnmpCommunityAclName,
       "ubiSnmpCommunityView": ubiSnmpCommunityView,
       "ubiSnmpCommunityRowStatus": ubiSnmpCommunityRowStatus,
       "ubiSnmpUserTable": ubiSnmpUserTable,
       "ubiSnmpUserEntry": ubiSnmpUserEntry,
       "ubiSnmpUserVersion": ubiSnmpUserVersion,
       "ubiSnmpUserName": ubiSnmpUserName,
       "ubiSnmpUserGroup": ubiSnmpUserGroup,
       "ubiSnmpUserAuthType": ubiSnmpUserAuthType,
       "ubiSnmpUserAuthPasswd": ubiSnmpUserAuthPasswd,
       "ubiSnmpUserPrivacyType": ubiSnmpUserPrivacyType,
       "ubiSnmpUserPrivacyPasswd": ubiSnmpUserPrivacyPasswd,
       "ubiSnmpUserAclName": ubiSnmpUserAclName,
       "ubiSnmpUserRowStatus": ubiSnmpUserRowStatus,
       "ubiSnmpGroupTable": ubiSnmpGroupTable,
       "ubiSnmpGroupEntry": ubiSnmpGroupEntry,
       "ubiSnmpGroupVersion": ubiSnmpGroupVersion,
       "ubiSnmpGroupName": ubiSnmpGroupName,
       "ubiSnmpGroupSecLevel": ubiSnmpGroupSecLevel,
       "ubiSnmpGroupReadView": ubiSnmpGroupReadView,
       "ubiSnmpGroupWriteView": ubiSnmpGroupWriteView,
       "ubiSnmpGroupNotifyView": ubiSnmpGroupNotifyView,
       "ubiSnmpGroupRowStatus": ubiSnmpGroupRowStatus,
       "ubiSnmpViewTable": ubiSnmpViewTable,
       "ubiSnmpViewEntry": ubiSnmpViewEntry,
       "ubiSnmpViewName": ubiSnmpViewName,
       "ubiSnmpViewVariable": ubiSnmpViewVariable,
       "ubiSnmpViewType": ubiSnmpViewType,
       "ubiSnmpViewRowStatus": ubiSnmpViewRowStatus,
       "ubiSnmpTrapHostTable": ubiSnmpTrapHostTable,
       "ubiSnmpTrapHostEntry": ubiSnmpTrapHostEntry,
       "ubiSnmpTrapHostType": ubiSnmpTrapHostType,
       "ubiSnmpTrapHostVersion": ubiSnmpTrapHostVersion,
       "ubiSnmpTrapHostAddrType": ubiSnmpTrapHostAddrType,
       "ubiSnmpTrapHostAddress": ubiSnmpTrapHostAddress,
       "ubiSnmpTrapHostCommunity": ubiSnmpTrapHostCommunity,
       "ubiSnmpTrapHostSecLevel": ubiSnmpTrapHostSecLevel,
       "ubiSnmpTrapHostPort": ubiSnmpTrapHostPort,
       "ubiSnmpTrapHostRowStatus": ubiSnmpTrapHostRowStatus,
       "ubiSnmpMIBConformance": ubiSnmpMIBConformance,
       "ubiSnmpMIBCompliances": ubiSnmpMIBCompliances,
       "ubiSnmpMIBCompliance": ubiSnmpMIBCompliance,
       "ubiSnmpMIBGroups": ubiSnmpMIBGroups,
       "ubiSnmpConfigGroup": ubiSnmpConfigGroup}
)
