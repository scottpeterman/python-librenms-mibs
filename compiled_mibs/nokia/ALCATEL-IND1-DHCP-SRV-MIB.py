# SNMP MIB module (ALCATEL-IND1-DHCP-SRV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-DHCP-SRV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:11 2025
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

(softentIND1DhcpSrv,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1DhcpSrv")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1DhcpSrvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DhcpSrvMIB.setRevisions(
        ("2009-10-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1DhcpSrvMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1DhcpSrvMIBNotifications = _AlcatelIND1DhcpSrvMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1DhcpSrvMIBNotifications.setStatus("current")
_AlcatelIND1DhcpSrvMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1DhcpSrvMIBObjects = _AlcatelIND1DhcpSrvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DhcpSrvMIBObjects.setStatus("current")


class _AlaDhcpSrvGlobalConfigStatus_Type(Integer32):
    """Custom type alaDhcpSrvGlobalConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaDhcpSrvGlobalConfigStatus_Type.__name__ = "Integer32"
_AlaDhcpSrvGlobalConfigStatus_Object = MibScalar
alaDhcpSrvGlobalConfigStatus = _AlaDhcpSrvGlobalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 1),
    _AlaDhcpSrvGlobalConfigStatus_Type()
)
alaDhcpSrvGlobalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDhcpSrvGlobalConfigStatus.setStatus("current")


class _AlaDhcpSrvGlobalRestart_Type(Integer32):
    """Custom type alaDhcpSrvGlobalRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("restart", 2))
    )


_AlaDhcpSrvGlobalRestart_Type.__name__ = "Integer32"
_AlaDhcpSrvGlobalRestart_Object = MibScalar
alaDhcpSrvGlobalRestart = _AlaDhcpSrvGlobalRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 2),
    _AlaDhcpSrvGlobalRestart_Type()
)
alaDhcpSrvGlobalRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDhcpSrvGlobalRestart.setStatus("current")


class _AlaDhcpSrvGlobalClearStat_Type(Integer32):
    """Custom type alaDhcpSrvGlobalClearStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaDhcpSrvGlobalClearStat_Type.__name__ = "Integer32"
_AlaDhcpSrvGlobalClearStat_Object = MibScalar
alaDhcpSrvGlobalClearStat = _AlaDhcpSrvGlobalClearStat_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 3),
    _AlaDhcpSrvGlobalClearStat_Type()
)
alaDhcpSrvGlobalClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDhcpSrvGlobalClearStat.setStatus("current")
_AlaDhcpSrvLease_ObjectIdentity = ObjectIdentity
alaDhcpSrvLease = _AlaDhcpSrvLease_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4)
)
_AlaDhcpSrvLeaseTable_Object = MibTable
alaDhcpSrvLeaseTable = _AlaDhcpSrvLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseTable.setStatus("current")
_AlaDhcpSrvLeaseEntry_Object = MibTableRow
alaDhcpSrvLeaseEntry = _AlaDhcpSrvLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4, 1, 1)
)
alaDhcpSrvLeaseEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseInetAddressType"),
    (0, "ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseInetAddress"),
)
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseEntry.setStatus("current")
_AlaDhcpSrvLeaseInetAddressType_Type = InetAddressType
_AlaDhcpSrvLeaseInetAddressType_Object = MibTableColumn
alaDhcpSrvLeaseInetAddressType = _AlaDhcpSrvLeaseInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4, 1, 1, 1),
    _AlaDhcpSrvLeaseInetAddressType_Type()
)
alaDhcpSrvLeaseInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseInetAddressType.setStatus("current")


class _AlaDhcpSrvLeaseInetAddress_Type(InetAddress):
    """Custom type alaDhcpSrvLeaseInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AlaDhcpSrvLeaseInetAddress_Type.__name__ = "InetAddress"
_AlaDhcpSrvLeaseInetAddress_Object = MibTableColumn
alaDhcpSrvLeaseInetAddress = _AlaDhcpSrvLeaseInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4, 1, 1, 2),
    _AlaDhcpSrvLeaseInetAddress_Type()
)
alaDhcpSrvLeaseInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseInetAddress.setStatus("current")
_AlaDhcpSrvLeaseMACAddress_Type = MacAddress
_AlaDhcpSrvLeaseMACAddress_Object = MibTableColumn
alaDhcpSrvLeaseMACAddress = _AlaDhcpSrvLeaseMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4, 1, 1, 3),
    _AlaDhcpSrvLeaseMACAddress_Type()
)
alaDhcpSrvLeaseMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseMACAddress.setStatus("current")
_AlaDhcpSrvLeaseLeaseGrant_Type = DateAndTime
_AlaDhcpSrvLeaseLeaseGrant_Object = MibTableColumn
alaDhcpSrvLeaseLeaseGrant = _AlaDhcpSrvLeaseLeaseGrant_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4, 1, 1, 4),
    _AlaDhcpSrvLeaseLeaseGrant_Type()
)
alaDhcpSrvLeaseLeaseGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseLeaseGrant.setStatus("current")
_AlaDhcpSrvLeaseLeaseExpiry_Type = DateAndTime
_AlaDhcpSrvLeaseLeaseExpiry_Object = MibTableColumn
alaDhcpSrvLeaseLeaseExpiry = _AlaDhcpSrvLeaseLeaseExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4, 1, 1, 5),
    _AlaDhcpSrvLeaseLeaseExpiry_Type()
)
alaDhcpSrvLeaseLeaseExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseLeaseExpiry.setStatus("current")


class _AlaDhcpSrvLeaseType_Type(Integer32):
    """Custom type alaDhcpSrvLeaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("dynamic", 2),
          ("manual", 3))
    )


_AlaDhcpSrvLeaseType_Type.__name__ = "Integer32"
_AlaDhcpSrvLeaseType_Object = MibTableColumn
alaDhcpSrvLeaseType = _AlaDhcpSrvLeaseType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 4, 1, 1, 6),
    _AlaDhcpSrvLeaseType_Type()
)
alaDhcpSrvLeaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseType.setStatus("current")
_AlaDhcpSrvTrapsObj_ObjectIdentity = ObjectIdentity
alaDhcpSrvTrapsObj = _AlaDhcpSrvTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 5)
)


class _AlaDhcpSrvLeaseThresholdStatus_Type(Integer32):
    """Custom type alaDhcpSrvLeaseThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelow80Threshold", 1),
          ("crossedAbove80Threshold", 2),
          ("reached100Threshold", 3))
    )


_AlaDhcpSrvLeaseThresholdStatus_Type.__name__ = "Integer32"
_AlaDhcpSrvLeaseThresholdStatus_Object = MibScalar
alaDhcpSrvLeaseThresholdStatus = _AlaDhcpSrvLeaseThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 5, 1),
    _AlaDhcpSrvLeaseThresholdStatus_Type()
)
alaDhcpSrvLeaseThresholdStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseThresholdStatus.setStatus("current")
_AlaDhcpSrvSubnetDescriptor_Type = DisplayString
_AlaDhcpSrvSubnetDescriptor_Object = MibScalar
alaDhcpSrvSubnetDescriptor = _AlaDhcpSrvSubnetDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 1, 5, 2),
    _AlaDhcpSrvSubnetDescriptor_Type()
)
alaDhcpSrvSubnetDescriptor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpSrvSubnetDescriptor.setStatus("current")
_AlcatelIND1DhcpSrvMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1DhcpSrvMIBConformance = _AlcatelIND1DhcpSrvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1DhcpSrvMIBConformance.setStatus("current")
_AlcatelIND1DhcpSrvMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1DhcpSrvMIBGroups = _AlcatelIND1DhcpSrvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1DhcpSrvMIBGroups.setStatus("current")
_AlcatelIND1DhcpSrvMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1DhcpSrvMIBCompliances = _AlcatelIND1DhcpSrvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1DhcpSrvMIBCompliances.setStatus("current")

# Managed Objects groups

alaDhcpSrvGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 2, 1, 1)
)
alaDhcpSrvGlobalConfigGroup.setObjects(
      *(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvGlobalConfigStatus"),
        ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvGlobalRestart"),
        ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvGlobalClearStat"))
)
if mibBuilder.loadTexts:
    alaDhcpSrvGlobalConfigGroup.setStatus("current")

alaDhcpSrvLeaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 2, 1, 2)
)
alaDhcpSrvLeaseGroup.setObjects(
      *(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseMACAddress"),
        ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseLeaseGrant"),
        ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseLeaseExpiry"),
        ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseType"))
)
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseGroup.setStatus("current")


# Notification objects

alaDhcpSrvLeaseUtilizationThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 0, 1)
)
alaDhcpSrvLeaseUtilizationThresholdTrap.setObjects(
      *(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseThresholdStatus"),
        ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvSubnetDescriptor"))
)
if mibBuilder.loadTexts:
    alaDhcpSrvLeaseUtilizationThresholdTrap.setStatus(
        "current"
    )


# Notifications groups

alaDhcpSrvNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 2, 1, 3)
)
alaDhcpSrvNotificationGroup.setObjects(
    ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseUtilizationThresholdTrap")
)
if mibBuilder.loadTexts:
    alaDhcpSrvNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1DhcpSrvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 59, 1, 2, 2, 1)
)
alcatelIND1DhcpSrvMIBCompliance.setObjects(
      *(("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvGlobalConfigGroup"),
        ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvLeaseGroup"),
        ("ALCATEL-IND1-DHCP-SRV-MIB", "alaDhcpSrvNotificationGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1DhcpSrvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DHCP-SRV-MIB",
    **{"alcatelIND1DhcpSrvMIB": alcatelIND1DhcpSrvMIB,
       "alcatelIND1DhcpSrvMIBNotifications": alcatelIND1DhcpSrvMIBNotifications,
       "alaDhcpSrvLeaseUtilizationThresholdTrap": alaDhcpSrvLeaseUtilizationThresholdTrap,
       "alcatelIND1DhcpSrvMIBObjects": alcatelIND1DhcpSrvMIBObjects,
       "alaDhcpSrvGlobalConfigStatus": alaDhcpSrvGlobalConfigStatus,
       "alaDhcpSrvGlobalRestart": alaDhcpSrvGlobalRestart,
       "alaDhcpSrvGlobalClearStat": alaDhcpSrvGlobalClearStat,
       "alaDhcpSrvLease": alaDhcpSrvLease,
       "alaDhcpSrvLeaseTable": alaDhcpSrvLeaseTable,
       "alaDhcpSrvLeaseEntry": alaDhcpSrvLeaseEntry,
       "alaDhcpSrvLeaseInetAddressType": alaDhcpSrvLeaseInetAddressType,
       "alaDhcpSrvLeaseInetAddress": alaDhcpSrvLeaseInetAddress,
       "alaDhcpSrvLeaseMACAddress": alaDhcpSrvLeaseMACAddress,
       "alaDhcpSrvLeaseLeaseGrant": alaDhcpSrvLeaseLeaseGrant,
       "alaDhcpSrvLeaseLeaseExpiry": alaDhcpSrvLeaseLeaseExpiry,
       "alaDhcpSrvLeaseType": alaDhcpSrvLeaseType,
       "alaDhcpSrvTrapsObj": alaDhcpSrvTrapsObj,
       "alaDhcpSrvLeaseThresholdStatus": alaDhcpSrvLeaseThresholdStatus,
       "alaDhcpSrvSubnetDescriptor": alaDhcpSrvSubnetDescriptor,
       "alcatelIND1DhcpSrvMIBConformance": alcatelIND1DhcpSrvMIBConformance,
       "alcatelIND1DhcpSrvMIBGroups": alcatelIND1DhcpSrvMIBGroups,
       "alaDhcpSrvGlobalConfigGroup": alaDhcpSrvGlobalConfigGroup,
       "alaDhcpSrvLeaseGroup": alaDhcpSrvLeaseGroup,
       "alaDhcpSrvNotificationGroup": alaDhcpSrvNotificationGroup,
       "alcatelIND1DhcpSrvMIBCompliances": alcatelIND1DhcpSrvMIBCompliances,
       "alcatelIND1DhcpSrvMIBCompliance": alcatelIND1DhcpSrvMIBCompliance}
)
