# SNMP MIB module (TN-HTTPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-HTTPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:38 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnHttpsMib_ObjectIdentity = ObjectIdentity
tnHttpsMib = _TnHttpsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41)
)
_TnHttpsConfig_ObjectIdentity = ObjectIdentity
tnHttpsConfig = _TnHttpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 1)
)
_TnHttpsConfigMode_Type = TruthValue
_TnHttpsConfigMode_Object = MibScalar
tnHttpsConfigMode = _TnHttpsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 1, 1),
    _TnHttpsConfigMode_Type()
)
tnHttpsConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHttpsConfigMode.setStatus("current")
_TnHttpsConfigAutoRedirect_Type = TruthValue
_TnHttpsConfigAutoRedirect_Object = MibScalar
tnHttpsConfigAutoRedirect = _TnHttpsConfigAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 1, 2),
    _TnHttpsConfigAutoRedirect_Type()
)
tnHttpsConfigAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHttpsConfigAutoRedirect.setStatus("current")
_TnHttpsCertGene_ObjectIdentity = ObjectIdentity
tnHttpsCertGene = _TnHttpsCertGene_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 2)
)


class _TnHttpsCertGenerate_Type(Integer32):
    """Custom type tnHttpsCertGenerate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsa", 1),
          ("dsa", 2))
    )


_TnHttpsCertGenerate_Type.__name__ = "Integer32"
_TnHttpsCertGenerate_Object = MibScalar
tnHttpsCertGenerate = _TnHttpsCertGenerate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 2, 1),
    _TnHttpsCertGenerate_Type()
)
tnHttpsCertGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHttpsCertGenerate.setStatus("current")
_TnHttpsCertLoadTable_Object = MibTable
tnHttpsCertLoadTable = _TnHttpsCertLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 3)
)
if mibBuilder.loadTexts:
    tnHttpsCertLoadTable.setStatus("current")
_TnHttpsCertLoadEntry_Object = MibTableRow
tnHttpsCertLoadEntry = _TnHttpsCertLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 3, 1)
)
tnHttpsCertLoadEntry.setIndexNames(
    (0, "TN-HTTPS-MIB", "tnHttpsCertLoadId"),
)
if mibBuilder.loadTexts:
    tnHttpsCertLoadEntry.setStatus("current")
_TnHttpsCertLoadId_Type = Unsigned32
_TnHttpsCertLoadId_Object = MibTableColumn
tnHttpsCertLoadId = _TnHttpsCertLoadId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 3, 1, 1),
    _TnHttpsCertLoadId_Type()
)
tnHttpsCertLoadId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHttpsCertLoadId.setStatus("current")
_TnHttpsCertLoadAddrType_Type = InetAddressType
_TnHttpsCertLoadAddrType_Object = MibTableColumn
tnHttpsCertLoadAddrType = _TnHttpsCertLoadAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 3, 1, 2),
    _TnHttpsCertLoadAddrType_Type()
)
tnHttpsCertLoadAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnHttpsCertLoadAddrType.setStatus("current")
_TnHttpsCertLoadAddr_Type = InetAddress
_TnHttpsCertLoadAddr_Object = MibTableColumn
tnHttpsCertLoadAddr = _TnHttpsCertLoadAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 3, 1, 3),
    _TnHttpsCertLoadAddr_Type()
)
tnHttpsCertLoadAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnHttpsCertLoadAddr.setStatus("current")


class _TnHttpsCertLoadFileName_Type(DisplayString):
    """Custom type tnHttpsCertLoadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TnHttpsCertLoadFileName_Type.__name__ = "DisplayString"
_TnHttpsCertLoadFileName_Object = MibTableColumn
tnHttpsCertLoadFileName = _TnHttpsCertLoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 3, 1, 4),
    _TnHttpsCertLoadFileName_Type()
)
tnHttpsCertLoadFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnHttpsCertLoadFileName.setStatus("current")
_TnHttpsCertLoadStatus_Type = TruthValue
_TnHttpsCertLoadStatus_Object = MibTableColumn
tnHttpsCertLoadStatus = _TnHttpsCertLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 3, 1, 5),
    _TnHttpsCertLoadStatus_Type()
)
tnHttpsCertLoadStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnHttpsCertLoadStatus.setStatus("current")


class _TnHttpsCertLastLoad_Type(Integer32):
    """Custom type tnHttpsCertLastLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_TnHttpsCertLastLoad_Type.__name__ = "Integer32"
_TnHttpsCertLastLoad_Object = MibTableColumn
tnHttpsCertLastLoad = _TnHttpsCertLastLoad_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 3, 1, 6),
    _TnHttpsCertLastLoad_Type()
)
tnHttpsCertLastLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnHttpsCertLastLoad.setStatus("current")
_TnHttpsCertViewTable_Object = MibTable
tnHttpsCertViewTable = _TnHttpsCertViewTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 4)
)
if mibBuilder.loadTexts:
    tnHttpsCertViewTable.setStatus("current")
_TnHttpsCertViewEntry_Object = MibTableRow
tnHttpsCertViewEntry = _TnHttpsCertViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 4, 1)
)
tnHttpsCertViewEntry.setIndexNames(
    (0, "TN-HTTPS-MIB", "tnHttpsCertId"),
)
if mibBuilder.loadTexts:
    tnHttpsCertViewEntry.setStatus("current")
_TnHttpsCertId_Type = Unsigned32
_TnHttpsCertId_Object = MibTableColumn
tnHttpsCertId = _TnHttpsCertId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 4, 1, 1),
    _TnHttpsCertId_Type()
)
tnHttpsCertId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHttpsCertId.setStatus("current")


class _TnHttpsCertMessage_Type(DisplayString):
    """Custom type tnHttpsCertMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TnHttpsCertMessage_Type.__name__ = "DisplayString"
_TnHttpsCertMessage_Object = MibTableColumn
tnHttpsCertMessage = _TnHttpsCertMessage_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 41, 4, 1, 2),
    _TnHttpsCertMessage_Type()
)
tnHttpsCertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnHttpsCertMessage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-HTTPS-MIB",
    **{"tnHttpsMib": tnHttpsMib,
       "tnHttpsConfig": tnHttpsConfig,
       "tnHttpsConfigMode": tnHttpsConfigMode,
       "tnHttpsConfigAutoRedirect": tnHttpsConfigAutoRedirect,
       "tnHttpsCertGene": tnHttpsCertGene,
       "tnHttpsCertGenerate": tnHttpsCertGenerate,
       "tnHttpsCertLoadTable": tnHttpsCertLoadTable,
       "tnHttpsCertLoadEntry": tnHttpsCertLoadEntry,
       "tnHttpsCertLoadId": tnHttpsCertLoadId,
       "tnHttpsCertLoadAddrType": tnHttpsCertLoadAddrType,
       "tnHttpsCertLoadAddr": tnHttpsCertLoadAddr,
       "tnHttpsCertLoadFileName": tnHttpsCertLoadFileName,
       "tnHttpsCertLoadStatus": tnHttpsCertLoadStatus,
       "tnHttpsCertLastLoad": tnHttpsCertLastLoad,
       "tnHttpsCertViewTable": tnHttpsCertViewTable,
       "tnHttpsCertViewEntry": tnHttpsCertViewEntry,
       "tnHttpsCertId": tnHttpsCertId,
       "tnHttpsCertMessage": tnHttpsCertMessage}
)
