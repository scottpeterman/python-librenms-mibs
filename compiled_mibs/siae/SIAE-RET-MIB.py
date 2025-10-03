# SNMP MIB module (SIAE-RET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-RET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:34 2025
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

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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


# MODULE-IDENTITY

remElement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70)
)
if mibBuilder.loadTexts:
    remElement.setRevisions(
        ("2014-06-23 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RemoteElementMibVersion_Type(Integer32):
    """Custom type remoteElementMibVersion based on Integer32"""
    defaultValue = 1


_RemoteElementMibVersion_Type.__name__ = "Integer32"
_RemoteElementMibVersion_Object = MibScalar
remoteElementMibVersion = _RemoteElementMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 1),
    _RemoteElementMibVersion_Type()
)
remoteElementMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteElementMibVersion.setStatus("current")
_RemoteElementTable_Object = MibTable
remoteElementTable = _RemoteElementTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2)
)
if mibBuilder.loadTexts:
    remoteElementTable.setStatus("current")
_RemoteElementEntry_Object = MibTableRow
remoteElementEntry = _RemoteElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1)
)
remoteElementEntry.setIndexNames(
    (0, "SIAE-RET-MIB", "remoteElementIpAddress"),
)
if mibBuilder.loadTexts:
    remoteElementEntry.setStatus("current")
_RemoteElementIpAddress_Type = IpAddress
_RemoteElementIpAddress_Object = MibTableColumn
remoteElementIpAddress = _RemoteElementIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 1),
    _RemoteElementIpAddress_Type()
)
remoteElementIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteElementIpAddress.setStatus("current")


class _RemoteElementGosipAddress_Type(OctetString):
    """Custom type remoteElementGosipAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RemoteElementGosipAddress_Type.__name__ = "OctetString"
_RemoteElementGosipAddress_Object = MibTableColumn
remoteElementGosipAddress = _RemoteElementGosipAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 2),
    _RemoteElementGosipAddress_Type()
)
remoteElementGosipAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteElementGosipAddress.setStatus("current")


class _RemoteElementLabel_Type(DisplayString):
    """Custom type remoteElementLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RemoteElementLabel_Type.__name__ = "DisplayString"
_RemoteElementLabel_Object = MibTableColumn
remoteElementLabel = _RemoteElementLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 3),
    _RemoteElementLabel_Type()
)
remoteElementLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteElementLabel.setStatus("current")


class _RemoteElementType_Type(Integer32):
    """Custom type remoteElementType based on Integer32"""
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
        *(("elemManager", 1),
          ("external", 2),
          ("remote", 3),
          ("snm", 4))
    )


_RemoteElementType_Type.__name__ = "Integer32"
_RemoteElementType_Object = MibTableColumn
remoteElementType = _RemoteElementType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 4),
    _RemoteElementType_Type()
)
remoteElementType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteElementType.setStatus("current")
_RemoteElementRadioBranchId_Type = Integer32
_RemoteElementRadioBranchId_Object = MibTableColumn
remoteElementRadioBranchId = _RemoteElementRadioBranchId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 5),
    _RemoteElementRadioBranchId_Type()
)
remoteElementRadioBranchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteElementRadioBranchId.setStatus("current")
_RemoteElementRowStatus_Type = RowStatus
_RemoteElementRowStatus_Object = MibTableColumn
remoteElementRowStatus = _RemoteElementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 6),
    _RemoteElementRowStatus_Type()
)
remoteElementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteElementRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-RET-MIB",
    **{"remElement": remElement,
       "remoteElementMibVersion": remoteElementMibVersion,
       "remoteElementTable": remoteElementTable,
       "remoteElementEntry": remoteElementEntry,
       "remoteElementIpAddress": remoteElementIpAddress,
       "remoteElementGosipAddress": remoteElementGosipAddress,
       "remoteElementLabel": remoteElementLabel,
       "remoteElementType": remoteElementType,
       "remoteElementRadioBranchId": remoteElementRadioBranchId,
       "remoteElementRowStatus": remoteElementRowStatus}
)
